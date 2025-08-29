from Constants import Character, Events, BaseData
from . import ModFolder
import Paths
class Song:
    def __init__(self):
        self.internName = "test"
        self.charts:dict[str, Chart] = {}

    def exportToVSlice(self, modFolder:ModFolder.VsliceMod, diff:str = "hard"):
        pass
    def exportToPsych(self, modFolder:ModFolder.PsychMod, diff:str = "hard"):
        Paths.createFolder(modFolder.getPath("songs"))
        Paths.createFolder(modFolder.getPath(f"songs/{self.internName}"))
        Paths.createFolder(modFolder.getPath("data"))
        Paths.createFolder(modFolder.getPath(f"data/{self.internName}"))

        chart = self.charts.get(diff)
        #copy the voices and inst
        Paths.copyFile(chart.songInst, modFolder.getPath(f"songs/{self.internName}/Inst.ogg"))

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
                Paths.copyFile(voice, modFolder.getPath(f"songs/{self.internName}/Voices{suffix}.ogg"))
        elif len(chart.songVoices) > 0:
            Paths.copyFile(chart.songVoices[0], modFolder.getPath(f"songs/{self.internName}/Voices.ogg"))

        #Chart Convertion
        chartFile = BaseData.PSYCH_SONG_BASE.copy()
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
                    notes.append({
				        "sectionBeats": 4,
				        "sectionNotes": [],
				        "mustHitSection": True
			        })
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
            print(len(lane.notes))
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
                    newNote.append(note["noteType"])

                sectionIdx = int(strum // sectionsLength)
                print(f"Division: {strum / sectionsLength} / Index: {sectionIdx} / Section Length: {sectionsLength} / Strum: {strum}")
                resizeSectionsTo(sectionIdx)
                notes[sectionIdx]["sectionNotes"].append(newNote)
                
        
        def sortFunc(note): 
            return note[0]
        
        for section in notes:
            section["sectionNotes"].sort(key = sortFunc)

        lastFocusIdx = 0
        for event in chart.events:
            match event.name:
                case Events.CAMERA_FOCUS:
                    character = event.vars.get("char", Character.DAD)
                    havePosSettings = event.vars.get("x", 0) != 0 and event.vars.get("y", 0) != 0
                    haveCustomEase = event.vars.get("ease", "CLASSIC") != "CLASSIC"
                    if not havePosSettings and not haveCustomEase:
                        
                        sectionIdx = int(event.strum // sectionsLength)
                        
                        mustHitSection = character == Character.BOYFRIEND
                        resizeSectionsTo(sectionIdx)
                        notes[sectionIdx]["mustHitSection"] = mustHitSection
                        print(f"newFocus {mustHitSection} / {sectionIdx}")
                        lastHitSection = notes[lastFocusIdx]["mustHitSection"]
                        for sections in range(lastFocusIdx + 1, sectionIdx):
                            notes[sections]["mustHitSection"] = lastHitSection

                        lastFocusIdx = sectionIdx
                    else:
                        if character == -1:
                            addEvent(event.strum, "Camera Follow Pos", str(event.vars.get("x")), str(event.vars.get("y")))
                        else:
                            args = event.vars.copy()
                            args.pop("char")
                            value2 = []
                            for key, item in args.items():
                                value2.append(f"{key}={item}")
                            addEvent(event.strum, Events.CAMERA_FOCUS, character, "::".join(value2))
                case __:
                    value1 = event.vars.get("value1", "")
                    value2 = event.vars.get("value2", "")

                    addEvent(event.strum, event.name, value1, value2)
        chartSong["notes"] = notes
        chartSong["events"] = events
        suffix = "-" + diff
        if diff == "normal":
            suffix = ""
        Paths.saveJson(modFolder.getPath(f"data/{self.internName}/{self.internName}{suffix}.json"), chartFile)


        
    def exportToCodename(self, modFolder:ModFolder.CodenameMod, diff:str = "hard"):
        pass
    def addChart(self, diff):
        chart = Chart()
        self.charts[diff] = chart
        return chart
    
    @classmethod
    def fromVSlice(cls, modFolder:ModFolder.VsliceMod, songName = "test"):
        songDataFolder = modFolder.getPath(f"data/songs/{songName}")
        songFolder = modFolder.getPath(f"songs/{songName}")

        defaultChart = Paths.getJsonData(modFolder.getPath(f"data/songs/{songName}/{songName}-chart.json"))
        defaultMeta = Paths.getJsonData(modFolder.getPath(f"data/songs/{songName}/{songName}-metadata.json"))
        newSong = cls()
        newSong.internName = songName
        #Events
        events = []
        for event in defaultChart["events"]:
            strum = event["t"]
            name = event["e"]
            args = event["v"]
            
            
            match name:
                case "FocusCamera":
                    name = Events.CAMERA_FOCUS
                    if type(args) is not dict:
                        args = {"char": args}

                    match args["char"]:
                        case 1:
                            args["char"] = Character.DAD
                        case 0:
                            args["char"] = Character.BOYFRIEND

            if type(args) is not dict:
                args = {"value1": args}
            newEvent = ChartEvent(strum, name, args)
            events.append(newEvent)
        #Chart 
        bpm = defaultMeta["timeChanges"][0]["bpm"]
        for diff in defaultMeta["playData"]["difficulties"]:
            characters:dict = defaultMeta["playData"]["characters"]
            chartNotes = defaultChart["notes"][diff]
            chart = newSong.addChart(diff)
            chart.scrollSpeed = defaultChart["scrollSpeed"][diff]
            chart.addLane(characters["opponent"], Character.DAD)
            chart.addLane(characters["player"], Character.BOYFRIEND)
            chart.addLane(characters["girlfriend"], Character.GF)
            for note in chartNotes:
                noteData = note["d"] % 4
                lane = chart.getLane(Character.BOYFRIEND)
                if note["d"] > 3:
                    lane = chart.getLane(Character.DAD)

                lane.addNote(note["t"], noteData, note.get("l", 0))
            chart.events = events
            chart.bpm = bpm
            def checkVoice(suffix):
                return Paths.exists(Paths.join(songFolder, f"Voices-{suffix}.ogg"))
            def addCharacterVoice(index, character:str, vocals:list[str] = None):
                suffix = ""
                if vocals is not None:
                    for vocal in vocals:
                        if checkVoice(vocal):
                            suffix = vocal
                            break
                else:
                    suffix = character

                if not checkVoice(vocal):
                    print(f"VOICES for {character} in {songName} not found")
                    return
                
                chart.songVoices.insert(index, Paths.join(songFolder, f"Voices-{suffix}.ogg"))

            addCharacterVoice(Character.BOYFRIEND, "player", characters.get("playerVocals"))
            addCharacterVoice(Character.DAD, "opponent", characters.get("opponentVocals"))

            print(chart.songVoices)
            variant = characters.get("instrumental", "")
            if variant != "":
                variant = "-" + variant
            chart.songInst = Paths.join(songFolder, f"Inst{variant}.ogg")
            chart.stage = defaultMeta["playData"]["stage"]

            chart.setMeta("charter", defaultMeta.get("charter", "Unknown"))
            chart.setMeta("artist", defaultMeta.get("artist", "Unknown"))
            chart.setMeta("metaVersion", defaultMeta["version"])
            chart.setMeta("metaGeneratedBy", defaultMeta["generatedBy"])
            chart.setMeta("chartVersion", defaultChart["version"])
            chart.setMeta("chartGeneratedBy", defaultChart["generatedBy"])
            chart.songName = defaultMeta["songName"]
        
        #Maybe Save Variants Too

        return newSong
                



        
class Chart:
    def __init__(self):
        self.songName:str = "test"
        self.lanes:list[ChartLane]  = []
        self.events:list[ChartEvent] = []
        self.metadata = {}
        self.stage:str = ""
        self.songVoices:list[str] = []
        self.songInst:str = ""
        self.bpm:int = 100
        self.scrollSpeed:float = 1
    def getMeta(self, key:str, ifNone = None):
        return self.metadata.get(key, ifNone)
    def setMeta(self, key:str, value):
        self.metadata[key] = value
    def getLane(self, characterID:int = Character.DAD):
        return self.lanes[characterID]
    def addLane(self, charName = "dad", pos:int = Character.DAD):
        newLane = ChartLane(charName)
        self.lanes.insert(pos, newLane)

class ChartEvent:
    def __init__(self, strum:float = 0, name = "", vars:dict = None):
        self.strum = strum
        self.name = name
        self.vars = vars or {}

class ChartLane:
    def __init__(self, character = None):
        self.character = character or Character.getName(Character.DAD)
        self.notes = []

    def addNote(self, strum:float, noteData:int = 0, length:float = 0, noteType:str = None):
        noteInfo = {
            "strum": strum,
            "noteData": noteData,
            "length": length,
            "noteType": noteType
        }
        self.notes.append(noteInfo)