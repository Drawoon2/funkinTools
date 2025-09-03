from .SongHandler import SongHandler
from Funkin.Song import Song, ChartEvent, Chart
from Funkin.ModFolder import VsliceMod
from Constants import Character, Events, Engine, Notes
import Paths, zipfile

class VSliceHandler(SongHandler):
    def __init__(self):
        super().__init__(Engine.VSLICE)
    @staticmethod
    def getChartBase():
        return {
            "version": "2.0.0",
            "scrollSpeed": {},
            "events": [],
            "notes": {},
            "generatedBy": "FunkinTools VSlice Imported"
        }
    @staticmethod
    def getMetaBase():
        return {
            "version": "2.2.4",
            "artist": "UNKNOWN",
            "charter": "UNKNOWN",
            "timeFormat": "ms",
            "playData": {
                "songVariations": [],
                "stage": "stage",
                "characters": {
                    "player": "bf",
                    "girlfriend": "gf",
                    "opponent": "dad"
                },
                "difficulties": [],
                "noteStyle": "funkin",
                "ratings": {},
                "album": "volume1",
                "previewStart": 0,
                "previewEnd": 15000
            },
            "songName": "Test",
            "timeChanges": [{ "d": 4, "n": 4, "t": -1, "bt": [4, 4, 4, 4], "bpm": 100 }],
            "generatedBy": "FunkinTools VSlice Imported"
        }
    @staticmethod
    def getManifest(interName:str = "test", version:str = "2.0.0"):
        return {"version": version, "songId": interName}
    @staticmethod
    def sortNotes(note):
        return note["t"]
    def generateChart(self, song:Song, diff:str = "hard"):
        chartdata = VSliceHandler.getChartBase()
        chart = song.getChart(diff)
        diffChart = []
        for lane in range(2):
            for note in chart.getLane(lane).notes:
                addNote = {}
                noteData = note["noteData"]
                noteType = note["noteType"]
                if lane == Character.DAD:
                    noteData += 4
                addNote["t"] = note["strum"]
                addNote["d"] = noteData
                addNote["l"] = note["length"]
                if noteType != Notes.DEFAULT:
                    addNote["k"] = noteType
                diffChart.append(addNote)
        
        diffChart.sort(key=VSliceHandler.sortNotes)
        chartdata["notes"][diff] = diffChart
        chartdata["scrollSpeed"][diff] = chart.scrollSpeed

        chartdata["events"] = self.exportEvents(chart)
        return chartdata
    def generateMetadata(self, song:Song, diff:str = "hard"):
        metadata = VSliceHandler.getMetaBase()
        chart = song.getChart(diff)
        characterList = {}
        characterList["player"] = chart.getLane(Character.BOYFRIEND).character
        characterList["opponent"] = chart.getLane(Character.DAD).character
        characterList["girlfriend"] = chart.getLane(Character.GF).character
        characterList["girlfriend"] = chart.getLane(Character.GF).character
        metadata["playData"]["characters"] = characterList
        metadata["playData"]["stage"] = chart.stage
        metadata["playData"]["difficulties"].append(diff)
        metadata["playData"]["ratings"][diff] = 5
        metadata["songName"] = chart.songName
        metadata["timeChanges"][0]["bpm"] = chart.bpm
        return metadata
    def saveMusic(self, path, song:Song, diff:str = "hard"):
        chart = song.getChart(diff)
        #Localized voices
        if len(chart.songVoices) > 1:
            for i in range(2): #VSlice have a max of 2 voices per song
                file = chart.songVoices[i]
                newName = f"Voices-{chart.getLane(i).character}.ogg"
                Paths.copyFile(file, f"{path}/{newName}")
        elif len(chart.songVoices) > 0:
            #VSlice doesn't play Voices.ogg if only there is 1 voices file
            Paths.copyFile(chart.songVoices[0], f"{path}/Voices-{chart.getLane(Character.DAD).character}.ogg")
        #Localized insts
        Paths.copyFile(chart.songInst, f"{path}/Inst.ogg")

    def exportSong(self, modFolder:VsliceMod, song:Song, diff:str = "hard"):
        Paths.createFolder(modFolder.getPath(f"data/songs"))
        songDataPath = modFolder.getPath(f"data/songs/{song.internName}")
        songPath = modFolder.getPath(f"songs/{song.internName}")
        Paths.createFolder(songDataPath)
        Paths.createFolder(songPath)

        metadata = self.generateMetadata(song, diff)
        chartdata = self.generateChart(song, diff)
        self.saveMusic(songPath, song, diff)

        Paths.saveJson(f"{songDataPath}/{song.internName}-chart.json", chartdata)
        Paths.saveJson(f"{songDataPath}/{song.internName}-metadata.json", metadata)

        return True
    def exportFNFC(self, song:Song, diff:str = "hard", path:str = "temp"):
        temp = f"temp/{song.internName}"
        Paths.createFolder(temp)
        metadata = self.generateMetadata(song, diff)
        chartdata = self.generateChart(song, diff)
        self.saveMusic(temp, song, diff)
        Paths.saveJson(f"{temp}/{song.internName}-chart.json", chartdata)
        Paths.saveJson(f"{temp}/{song.internName}-metadata.json", metadata)
        Paths.saveJson(f"{temp}/manifest.json", VSliceHandler.getManifest(song.internName))

        filePath = Paths.join(path, f"{song.internName}.fnfc")
        with zipfile.ZipFile(filePath, "w") as zip:
            for file in Paths.listFolder(temp):
                fullPath = f"{temp}/{file}"
                zip.write(fullPath, file)

    def importSong(self, modFolder:VsliceMod, songName:str) -> Song:
        songDataFolder = modFolder.getPath(f"data/songs/{songName}")
        songFolder = modFolder.getPath(f"songs/{songName}")

        defaultChart = Paths.getJsonData(modFolder.getPath(f"data/songs/{songName}/{songName}-chart.json"))
        defaultMeta = Paths.getJsonData(modFolder.getPath(f"data/songs/{songName}/{songName}-metadata.json"))
        newSong = Song(songName)
        #Events
        events = self.importEvents(defaultChart)
        #get Audio Files    
        voices = self.getVoices(songFolder, defaultMeta)
        insts = self.getInst(songFolder, defaultMeta)

        metaData = self.getMetaData(defaultMeta, defaultChart)
        #Chart 
        characters:dict = defaultMeta["playData"]["characters"]
        bpm = defaultMeta["timeChanges"][0]["bpm"]
        for diff in defaultMeta["playData"]["difficulties"]:
            
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
                
                lane.addNote(note["t"], noteData, note.get("l", 0), note.get("k", Notes.DEFAULT))
            chart.events = events
            chart.bpm = bpm
            chart.songVoices = voices

            variant = characters.get("instrumental", "")
            if variant != "":
                variant = "-" + variant
            chart.songInst = insts
            chart.stage = defaultMeta["playData"]["stage"]
            chart.setMetaFromDict(metaData)
            chart.songName = defaultMeta["songName"]
        
        #Maybe Save Variants Too

        return newSong

    def getMetaData(self, metaData:dict, chartData:dict) -> dict:
        meta = {}
        meta["charter"] = metaData.get("charter")
        meta["artist"] = metaData.get("artist")
        meta["metaVersion"] = metaData["version"]
        meta["metaGeneratedBy"] = metaData["generatedBy"]
        meta["chartVersion"] = chartData["version"]
        meta["chartGeneratedBy"] = chartData["generatedBy"]
        return meta
    def getVoices(self, songFolder:str, metaData:dict) -> list:
        voices = []
        characters:dict = metaData["playData"]["characters"]
        def checkVoice(suffix):
            return Paths.exists(Paths.join(songFolder, f"Voices-{suffix}.ogg"))
        def getVoicePath(character:str, vocals:list[str] = None):
            suffix = ""
            if vocals is not None:
                for vocal in vocals:
                    if checkVoice(vocal):
                        suffix = vocal
                        break
            else:
                suffix = character

            if not checkVoice(vocal):
                print(f"VOICES for {character} in {metaData["songName"]} not found")
                return
                
            return Paths.join(songFolder, f"Voices-{suffix}.ogg")
        voices.insert(Character.BOYFRIEND, getVoicePath("player", characters.get("playerVocals")))
        voices.insert(Character.DAD, getVoicePath("opponent", characters.get("opponentVocals")))
        return voices
    def getInst(self, songFolder:str, metaData:dict):
        variant = metaData["playData"]["characters"].get("instrumental", "")
        if variant != "":
            variant = "-" + variant
        return Paths.join(songFolder, f"Inst{variant}.ogg")
    
    def exportEvents(self, chart:Chart) -> list:
        events = []
        for event in chart.events:
            name = event.name
            args = {}
            match name:
                case Events.CHANGE_BUMP_INTERVAL:
                    name = "SetCameraBop"
                    args["intensity"] = event.getValue("stregth")
                    interval = event.getValue("interval")
                    offset = event.getValue("offset")
                    if event.getValue("unit") is not None:
                        match event.getValue("unit"):
                            case "MESURE": # Section
                                interval *= 4
                                offset *= 4
                            case "STEP":
                                interval /= 4 #VSlice can't hold step precision
                                interval = int(interval + .5) # This work something like a round
                                offset /= 4
                                offset = int(offset + .5)
                    args["rate"] = interval #Vslice unit is beat
                    args["offset"] = offset #Vslice unit is beat
                case Events.CAMERA_FOCUS:
                    name = "FocusCamera"
                    match event.getValue("char"):
                        case Character.BOYFRIEND:
                            args["char"] = 0
                        case Character.DAD:
                            args["char"] = 1
                        case __:
                            args["char"] = event.getValue("char")
                    if event.getValue("x") is not None:
                        args["x"] = event.getValue("x")

                    if event.getValue("y") is not None:
                        args["y"] = event.getValue("y")

                    if event.getValue("duration") is not None:
                        args["duration"] = event.getValue("duration")

                    if event.getValue("ease") is not None:
                        args["ease"] = event.getValue("ease")
                case Events.CHANGE_SCROLL_SPEED:
                    name = "ScrollSpeed"

                    args["scroll"] = event.getValue("speed")
                    if event.getValue("multiplive") is not None:
                        args["absolute"] = not event.getValue("multiplive")

                    if event.getValue("time") is not None:
                        args["duration"] = event.getValue("time") 
                    elif event.getValue("timeSec") is not None:
                        args["duration"] = event.getValue("timeSec") / ((60 / chart.bpm) / 4)
                    ease = event.getValue("ease", "linear")
                    if event.getValue("type") is not None and ease != "linear" and ease != "INSTANT":
                        ease += event.getValue("type")
                case Events.PLAY_ANIMATION:
                    name = "PlayAnimation"
                    args["target"] = Character.getName(event.getValue("character"))
                    args["anim"] = event.getValue("animation")
                    if event.getValue("forced") is not None:
                        args["force"] = event.getValue("forced")
                case __:
                    args = event.vars

            eventData = {
                "t": event.strum,
                "e": name,
                "v": args
            }
            events.append(eventData)
        return events
    def importEvents(self, chart) -> list:
        events = []
        for event in chart["events"]:
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
        return events
    
    
