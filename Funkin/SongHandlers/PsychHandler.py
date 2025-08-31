from .SongHandler import SongHandler
from Funkin.Song import Song, ChartEvent
from Funkin.ModFolder import PsychMod
from Constants import Character, Events, Notes
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
    def importSong(modFolder:PsychMod, songName:str):
        
        songDataPath = modFolder.getPath(f"data/{songName}")
        eventsFile = Paths.join(songDataPath, "events.json")
        song = Song(songName)
        externalEvents:list[ChartEvent] = []
        if Paths.exists(eventsFile):
            eventsData = Paths.getJsonData(eventsFile)
            externalEvents = PsychHandler.importEvents(eventsData.get("song", eventsData)["events"])

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
                chart = PsychHandler.addChart(song, Paths.join(songDataPath, file), externalEvents)
                chart.songInst = insts
                chart.songVoices = voicesList
        return song
    @staticmethod
    def addChart(song:Song, filePath:str, externalEvents:list[ChartEvent]):
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
                    noteType = None
                else:
                    noteType = note[3]
                match noteType:
                    case "":
                        noteType = None
                    case "GF Sing":
                        noteType = None
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

        events = PsychHandler.importEvents(chartData["events"])
        chart.events = events + sectionEvents + externalEvents
        chart.sortEvents()
        return chart
    
    @staticmethod
    def importEvents(eventsList):
        events = []
        for eventGroup in eventsList:
            strum = eventGroup[0]
            for event in eventGroup[1]:
                name = event[0]
                value1 = event[1]
                value2 = event[2]
                args = {}
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
                event = ChartEvent(strum, name, args)
                events.append(event)


        return events
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