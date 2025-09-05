from .SongHandler import SongHandler
from Funkin.Song import Song, ChartEvent, Chart
from Funkin.ModFolder import PsychMod
from Constants import Character, Events, Notes, Engine
import Paths

class PsychHandler(SongHandler):
    def __init__(self):
        super().__init__(Engine.PSYCH)
    @staticmethod
    def getSongBase():
        return {"song": {
			"player1": "bf",
			"events": [],
			"gfVersion": None,
			"notes": [],
			"player2": "dad",
			"stage": "stage",
			"bpm": 100,
			"speed": 3,
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
    def importSong(self, modFolder:PsychMod, songName:str):
        
        songDataPath = modFolder.getPath(f"data/{songName}")
        eventsFile = Paths.join(songDataPath, "events.json")
        song = Song(songName)
        externalEvents:list[ChartEvent] = []
        if Paths.exists(eventsFile):
            eventsData = Paths.getJsonData(eventsFile)
            externalEvents = self.importEvents(eventsData.get("song", eventsData)["events"])

        songPath = modFolder.getPath(f"songs/{songName}")
        insts = Paths.join(songPath, "Inst.ogg")
        possiblePlayerVoices = ["Voices-Player.ogg", "Voices.ogg"]
        voicesList = []
        for voice in possiblePlayerVoices:
            path = Paths.join(songPath, voice)
            if Paths.exists(path):
                voicesList.insert(Character.BOYFRIEND, path)
                break
        opponetVoices = Paths.join(songPath, "Voices-Opponent.ogg")
        if Paths.exists(opponetVoices):
            voicesList.insert(Character.DAD, opponetVoices)

        for file in Paths.listFolder(songDataPath):
            if file.startswith(songName):
                chart = self.addChart(song, Paths.join(songDataPath, file), externalEvents)
                chart.songInst = insts
                chart.songVoices = voicesList
        return song
    def addChart(self, song:Song, filePath:str, externalEvents:list[ChartEvent]):
        chartData = Paths.getJsonData(filePath)
        if chartData.get("notes") is None:
            chartData = chartData.get("song")
        diff = Paths.getFileName(filePath).removeprefix(song.internName).removesuffix(".json")
        if diff.strip() == "":
            diff = "normal"
        else:
            diff = diff.removeprefix("-")
        print(diff)
        chart = song.addChart(diff)
        chart.scrollSpeed = chartData["speed"]
        chart.bpm = chartData["bpm"]
        chart.songName = chartData["song"]
        chart.stage = chartData["stage"]
        chart.addLane(chartData["player2"], Character.DAD)
        chart.addLane(chartData["player1"], Character.BOYFRIEND)
        chart.addLane(chartData.get("gfVersion", "gf"), Character.GF)
        lastMustHitSection = None
        sectionsLength = ((60 / chart.bpm) * 1000) * 4
        sectionEvents = []
        for i, section in enumerate(chartData["notes"]):
            gfSection = section.get("gfSection", False)
            mustHitSection = section.get("mustHitSection", False)

            for note in section["sectionNotes"]:
                if note[1] > 3:
                    if gfSection and not mustHitSection:
                        char = Character.GF
                    else:
                        char = Character.DAD
                elif gfSection and mustHitSection:
                    char = Character.GF
                else:
                    char = Character.BOYFRIEND

                strum = note[0]
                noteData = note[1] % 4
                length = note[2]
                if len(note) < 4:
                    noteType = Notes.DEFAULT
                else:
                    noteType = note[3]
                match noteType:
                    case "":
                        noteType = Notes.DEFAULT
                    case "GF Sing":
                        noteType = Notes.DEFAULT
                        char = Character.GF
                    case "Alt Animation":
                        noteType = Notes.ALT_ANIM
                    case "No Animation":
                        noteType = Notes.NO_ANIM
                lane = chart.getLane(char)
                lane.addNote(strum, noteData, length, noteType)

            #Section Events
            if lastMustHitSection is None or lastMustHitSection != mustHitSection:
                values = {}
                if mustHitSection:
                    values["char"] = Character.BOYFRIEND
                else:
                    values["char"] = Character.DAD
                if gfSection:
                    values["char"] = Character.GF
                event = ChartEvent(sectionsLength * (i -1), Events.CAMERA_FOCUS, values)
                sectionEvents.append(event)
                lastMustHitSection == mustHitSection

        events = self.importEvents(chartData["events"])
        chart.events = events + sectionEvents + externalEvents
        chart.sortEvents()
        return chart

    def importEvents(self, eventsList):
        events = []
        for eventGroup in eventsList:
            strum = eventGroup[0]
            for event in eventGroup[1]:
                name = event[0]
                value1 = event[1]
                value2 = event[2]
                args = {}
                if not self.renameDefaultEvents:
                    args["value1"] = value1
                    args["value2"] = value2
                    event = ChartEvent(strum, name, args)
                    events.append(event)
                    continue
                match name:
                    case "Play Animation":
                        name = Events.PLAY_ANIMATION
                        args["animation"] = value1
                        args["character"] = value2
                    case "Camera Follow Pos":
                        if value1 == "" and value2 == "":
                            continue
                        name = Events.CAMERA_FOCUS
                        args["char"] = -1
                        args["x"] = float(value1)
                        args["y"] = float(value2)
                    case "Change Scroll Speed":
                        name = Events.CHANGE_SCROLL_SPEED
                        args["speed"] = value1
                        args["multiplive"] = True
                        args["timeSec"] = value2
                    case __:
                        args["value1"] = value1
                        args["value2"] = value2
                event = ChartEvent(strum, name, args)
                events.append(event)


        return events
    def exportSong(self, modFolder:PsychMod, song:Song, diffs:list[str] = []) -> bool:
        Paths.createFolder(modFolder.getPath("songs"))
        Paths.createFolder(modFolder.getPath("data"))

        
        for diff in diffs:
            chartData = self.createChart(song, diff)
            chart = song.getChart(diff)
            songName = f"{song.internName}"
            if chart.isVariant:
                songName = f"{song.internName}-{chart.variantTag}"

            songDataPath:str = modFolder.getPath(f"data/{songName}")
            songPath:str = modFolder.getPath(f"songs/{songName}")
            
            Paths.createFolder(songDataPath)
            Paths.createFolder(songPath)

            diffTag = chart.getDifficult()
            if diffTag == "normal":
                diffTag = ""
            else:
                diffTag = f"-{diffTag}"
            
            Paths.saveJson(Paths.join(songDataPath, f"{songName}{diffTag}.json"), chartData)
            self.saveMusic(song, diff, songPath)
            

        return True
    
    def saveMusic(self, song:Song, diff:str, songPath:str):
        chart = song.getChart(diff)

        Paths.copyFile(chart.songInst, Paths.join(songPath, "Inst.ogg"))

        if len(chart.songVoices) > 1:
            Paths.copyFile(chart.songVoices[Character.DAD], Paths.join(songPath, "Voices-Opponent.ogg"))
            Paths.copyFile(chart.songVoices[Character.BOYFRIEND], Paths.join(songPath, "Voices-Player.ogg"))
        elif len(chart.songVoices) > 0:
            Paths.copyFile(chart.songVoices[0], Paths.join(songPath, "Voices.ogg"))

    def createChart(self, song:Song, diff:str) -> dict:
        chart = song.getChart(diff)
        chartFile = PsychHandler.getSongBase()
        chartSong = chartFile["song"]
        if chart.isVariant:
            songName = f"{song.internName} {chart.variantTag}".title()
            chartSong["song"] = songName
        else:
            chartSong["song"] = chart.songName
        chartSong["needsVoices"] = len(chart.songVoices) > 0
        chartSong["speed"] = chart.scrollSpeed
        chartSong["bpm"] = chart.bpm
        chartSong["player2"] = chart.getLane().character
        chartSong["player1"] = chart.getLane(Character.BOYFRIEND).character
        chartSong["gfVersion"] = chart.getLane(Character.GF).character or "gf"

        notes = []
        sectionsLength = ((60 / chart.bpm) * 1000) * 4
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
                if noteType != Notes.DEFAULT:
                    newNote.append(noteType)

                sectionIdx = int(strum // sectionsLength)
                #print(f"Division: {strum / sectionsLength} / Index: {sectionIdx} / Section Length: {sectionsLength} / Strum: {strum}")
                PsychHandler.resizeSectionsTo(notes, sectionIdx)
                notes[sectionIdx]["sectionNotes"].append(newNote)

        def sortFunc(note): 
            return note[0]
        
        for section in notes:
            section["sectionNotes"].sort(key = sortFunc)

        events = self.exportEvents(chart, notes)
        chartSong["notes"] = notes
        chartSong["events"] = events
        return chartFile

    def exportEvents(self, chart:Chart, notes:list) -> list:
        eventsData = []
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
            eventsData.append(event)
        sectionsLength = ((60 / chart.bpm) * 1000) * 4
        lastFocusIdx = 0
        forceCameraZoomActive = False
        for event in chart.events:
            match event.name:
                case Events.CHANGE_SCROLL_SPEED: #Lose: tweenSpeed, ease, type
                    newSpeedMult = 1
                    if event.getValue("multiplive", False):
                        newSpeedMult = event.getValue("speed", 1)
                    else:
                        newSpeedMult = event.getValue("speed", 1) / chart.scrollSpeed
                    if event.getValue("timeSec") is not None:
                        duration = event.getValue("timeSec")
                    else:
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
                        PsychHandler.resizeSectionsTo(notes, sectionIdx)
                        notes[sectionIdx]["mustHitSection"] = mustHitSection
                        #print(f"newFocus {mustHitSection} / {sectionIdx}")
                        lastHitSection = notes[lastFocusIdx]["mustHitSection"]
                        for sections in range(lastFocusIdx + 1, sectionIdx):
                            notes[sections]["mustHitSection"] = lastHitSection

                        lastFocusIdx = sectionIdx
                        if forceCameraZoomActive:
                            forceCameraZoomActive = False
                            addEvent(event.strum, "Camera Follow Pos", "", "")
                    else:
                        if character == -1:
                            addEvent(event.strum, "Camera Follow Pos", str(event.getValue("x")), str(event.getValue("y")))
                            forceCameraZoomActive = True
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
        return eventsData
    @staticmethod
    def resizeSectionsTo(notes:list, num:int):
        if len(notes) < num + 1:
            for setionsToAdd in range(num - len(notes) + 1):
                notes.append(PsychHandler.getSection())
            print(f"NUM SECTION: {len(notes)}")
