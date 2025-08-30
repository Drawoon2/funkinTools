from .SongHandler import SongHandler
from Funkin.Song import Song, ChartEvent
from Funkin.ModFolder import PsychMod
from Constants import Character, Events, BaseData
import Paths

class PsychHandler(SongHandler):
    @staticmethod
    def getSongBase():
        return {"song": {
			"player1": "bf",
			"events": [],
			"gfVersion": None,
			"notes": [],
			"player2": "dad",
			"stage": "stage",
			"bpm": "stage",
			"speed": "stage",
			"song": "Test",
			"needsVoices": True,
			"format": "psych_v1_funkintools_convert"
		}
	}
    @staticmethod
    def getSection():
        return {
		    "sectionBeats": 4,
		    "sectionNotes": [],
		    "mustHitSection": True
	    }
    @staticmethod
    def exportSong(modFolder:PsychMod, song:Song, diff) -> bool:
        Paths.createFolder(modFolder.getPath("songs"))
        Paths.createFolder(modFolder.getPath(f"songs/{song.internName}"))
        Paths.createFolder(modFolder.getPath("data"))
        Paths.createFolder(modFolder.getPath(f"data/{song.internName}"))

        chart = song.charts.get(diff)
        #copy the voices and inst
        Paths.copyFile(chart.songInst, modFolder.getPath(f"songs/{song.internName}/Inst.ogg"))

        if len(chart.songVoices) > 1:
            for char, voice in enumerate(chart.songVoices):
                suffix = ""
                match char:
                    case Character.DAD:
                        suffix = "-Opponent"
                    case Character.BOYFRIEND:
                        suffix = "-Player"
                    case __:
                        suffix = "-" + chart.getLane(char).character
                Paths.copyFile(voice, modFolder.getPath(f"songs/{song.internName}/Voices{suffix}.ogg"))
        elif len(chart.songVoices) > 0:
            Paths.copyFile(chart.songVoices[0], modFolder.getPath(f"songs/{song.internName}/Voices.ogg"))

        #Chart Convertion
        chartFile = PsychHandler.getSongBase()
        chartSong = chartFile["song"]
        chartSong["song"] = chart.songName
        chartSong["needsVoices"] = len(chart.songVoices) > 0
        chartSong["speed"] = chart.scrollSpeed
        chartSong["bpm"] = chart.bpm
        chartSong["player2"] = chart.getLane().character
        chartSong["player1"] = chart.getLane(Character.BOYFRIEND).character
        chartSong["gfVersion"] = chart.getLane(Character.GF).character or "gf"
        sectionsLength = ((60 / chart.bpm) * 1000) * 4
        notes = []
        def resizeSectionsTo(num:int):
            if len(notes) < num + 1:
                for setionsToAdd in range(num - len(notes) + 1):
                    notes.append(PsychHandler.getSection())
                print(f"NUM SECTION: {len(notes)}")
        events = []
        def addEvent(strum:float, name:str, value1:str = "", value2:str = ""):
            event = [
                strum,
                [
                    [
                        name,
                        value1,
                        value2
                    ]
                ]
            ]
            events.append(event)
        for i in range(3):
            lane = chart.getLane(i)
            #print(len(lane.notes))
            for note in lane.notes:
                strum = note["strum"]
                noteData = note["noteData"]
                length = note["length"]
                noteType = note["noteType"]
                if i == Character.DAD:
                    noteData += 4
                elif i == Character.GF: 
                    noteType = "GF Sing"
                    noteData += 4

                newNote = [strum, noteData, length]
                if noteType is not None:
                    newNote.append(noteType)

                sectionIdx = int(strum // sectionsLength)
                #print(f"Division: {strum / sectionsLength} / Index: {sectionIdx} / Section Length: {sectionsLength} / Strum: {strum}")
                resizeSectionsTo(sectionIdx)
                notes[sectionIdx]["sectionNotes"].append(newNote)
                
        
        def sortFunc(note): 
            return note[0]
        
        for section in notes:
            section["sectionNotes"].sort(key = sortFunc)

        lastFocusIdx = 0
        for event in chart.events:
            match event.name:
                case Events.CHANGE_SCROLL_SPEED: #Lose: tweenSpeed, ease, type
                    newSpeedMult = 1
                    if event.getValue("multiplive", False):
                        newSpeedMult = event.getValue("speed", 1)
                    else:
                        newSpeedMult = event.getValue("speed", 1) / chart.scrollSpeed
                    duration = (event.getValue("time", 1) * ((60 / chart.bpm) * 250)) / 1000

                    addEvent(event.strum, "Change Scroll Speed", str(newSpeedMult), str(duration))
                case Events.PLAY_ANIMATION:
                    value1 = event.getValue("animation")
                    match event.getValue("character", Character.DAD):
                        case Character.DAD:
                            value2 = "dad"
                        case Character.BOYFRIEND:
                            value2 = "boyfriend"
                        case Character.GF:
                            value2 = "gf"
                    addEvent(event.strum, "Play Animation", value1, value2)
                case Events.CAMERA_FOCUS:
                    character = event.getValue("char", Character.DAD)
                    havePosSettings = event.getValue("x", 0) != 0 and event.getValue("y", 0) != 0
                    haveCustomEase = event.getValue("ease", "CLASSIC") != "CLASSIC"
                    if not havePosSettings and not haveCustomEase:
                        
                        sectionIdx = int(event.strum // sectionsLength)
                        
                        mustHitSection = character == Character.BOYFRIEND
                        resizeSectionsTo(sectionIdx)
                        notes[sectionIdx]["mustHitSection"] = mustHitSection
                        #print(f"newFocus {mustHitSection} / {sectionIdx}")
                        lastHitSection = notes[lastFocusIdx]["mustHitSection"]
                        for sections in range(lastFocusIdx + 1, sectionIdx):
                            notes[sections]["mustHitSection"] = lastHitSection

                        lastFocusIdx = sectionIdx
                    else:
                        if character == -1:
                            addEvent(event.strum, "Camera Follow Pos", str(event.getValue("x")), str(event.getValue("y")))
                        else:
                            args = event.vars.copy()
                            args.pop("char")
                            value2 = []
                            for key, item in args.items():
                                value2.append(f"{key}={item}")
                            addEvent(event.strum, Events.CAMERA_FOCUS, character, "::".join(value2))
                case __:
                    value1 = event.getValue("value1", "")
                    value2 = event.getValue("value2", "")

                    addEvent(event.strum, event.name, value1, value2)
        chartSong["notes"] = notes
        chartSong["events"] = events
        suffix = "-" + diff
        if diff == "normal":
            suffix = ""
        Paths.saveJson(modFolder.getPath(f"data/{song.internName}/{song.internName}{suffix}.json"), chartFile)
        return True