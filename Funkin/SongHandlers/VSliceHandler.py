from .SongHandler import SongHandler
from Funkin.Song import Song, ChartEvent, Chart, ChartLane
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
    def generateChart(self, song:Song, diff:str = "hard", chartdata:dict = None):
        if chartdata is None:
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
        chartdata["notes"][chart.getDifficult()] = diffChart
        chartdata["scrollSpeed"][chart.getDifficult()] = chart.scrollSpeed

        chartdata["events"] = self.exportEvents(chart)
        return chartdata
    def generateMetadata(self, song:Song, diff:str = "hard", metadata:dict = None):
        if metadata is None:
            metadata = VSliceHandler.getMetaBase()
        chart = song.getChart(diff)
        characterList = {}
        bfLane = chart.getLane(Character.BOYFRIEND)
        dadLane = chart.getLane(Character.DAD)

        characterList["player"] = bfLane.character
        if bfLane.getMeta("vocalSuffix") is not None:
            characterList["playerVocals"] = [bfLane.getMeta("vocalSuffix")]

        characterList["opponent"] = dadLane.character
        if dadLane.getMeta("vocalSuffix") is not None:
            characterList["opponentVocals"] = [dadLane.getMeta("vocalSuffix")]

        characterList["girlfriend"] = chart.getLane(Character.GF).character

        
        metadata["playData"]["characters"] = characterList
        metadata["playData"]["stage"] = chart.stage
        metadata["playData"]["difficulties"].append(chart.getDifficult())
        metadata["playData"]["ratings"][chart.getDifficult()] = chart.getMeta("rating", 5)
        metadata["songName"] = chart.songName
        metadata["timeChanges"][0]["bpm"] = chart.bpm
        return metadata
    def saveMusic(self, path:str, song:Song, diff:str = "hard"):
        chart = song.getChart(diff)
        variant = ""
        if chart.isVariant:
            variant = chart.variantTag

        instSuffix = chart.getMeta("instSuffix", "")
        if instSuffix != "":
            instSuffix = f"-{instSuffix}" 
        #Localized insts
        Paths.copyFile(chart.songInst, f"{path}/Inst{instSuffix}.ogg")

        #Localized voices
        if len(chart.songVoices) > 0:
            Paths.copyFile(chart.songVoices[0], f"{path}/{self.getVoicesName(chart.getLane(Character.DAD), variant)}")

        if len(chart.songVoices) > 1:
            Paths.copyFile(chart.songVoices[1], f"{path}/{self.getVoicesName(chart.getLane(Character.BOYFRIEND), variant)}")

        
    def getVoicesName(self, lane:ChartLane, variant:str = ""):
        suffix = lane.character
        if lane.getMeta("vocalSuffix") is not None:
            suffix = lane.getMeta("vocalSuffix")
        
        if variant != "":
            variant = f"-{variant}"
        newName = f"Voices-{suffix}{variant}.ogg"
        
        return newName
    def exportSong(self, modFolder:VsliceMod, song:Song, diffs:list = []) -> bool:
        Paths.createFolder(modFolder.getPath(f"data/songs"))
        songDataPath = modFolder.getPath(f"data/songs/{song.internName}")
        songPath = modFolder.getPath(f"songs/{song.internName}")
        Paths.createFolder(songDataPath)
        Paths.createFolder(songPath)
        self.exportData(song, diffs, songPath, songDataPath)

        return True
    def exportData(self, song:Song, diffs:list[str], songPath:str, songDataPath:str):
        metadatas = {}
        chartdatas = {}
        for diff in diffs:
            chart = song.getChart(diff)
            variant = "default"
            if chart.isVariant:
                variant = chart.variantTag

            metadata = metadatas.get(variant)
            chartdata = chartdatas.get(variant)
            
            metadatas[variant] = self.generateMetadata(song, diff, metadata)
            chartdatas[variant] = self.generateChart(song, diff, chartdata)
            self.saveMusic(songPath, song, diff)
        
        variants = list(metadatas.keys())
        variants.remove("default")
        metadata = metadatas["default"]
        metadata["playData"]["songVariations"] = variants
        for variant, metadata in metadatas.items():
            Paths.saveJson(f"{songDataPath}/{song.internName}-metadata{VSliceHandler.getSuffix(variant)}.json", metadata)

        for variant, metadata in chartdatas.items():
            Paths.saveJson(f"{songDataPath}/{song.internName}-chart{VSliceHandler.getSuffix(variant)}.json", metadata)

    @staticmethod
    def getSuffix(suffix):
        if suffix == "default":
            suffix = ""
        if suffix != "":
            suffix = f"-{suffix}"
        return suffix
    def exportFNFC(self, song:Song, diffs:list[str] = ["hard"], filePath:str = None):
        temp = f"temp/{song.internName}"
        Paths.createFolder(temp)

        self.exportData(song, diffs, temp, temp)


        if filePath is None:
            filePath = f"temp/{song.internName}.fnfc"
        with zipfile.ZipFile(filePath, "w") as zip:
            for file in Paths.listFolder(temp):
                fullPath = f"{temp}/{file}"
                zip.write(fullPath, file)

    def importSong(self, modFolder:VsliceMod, songName:str) -> Song:
        self.songDataFolder = modFolder.getPath(f"data/songs/{songName}")
        self.songFolder = modFolder.getPath(f"songs/{songName}")
        defaultChart = Paths.getJsonData(Paths.join(self.songDataFolder, f"{songName}-chart.json"))
        defaultMeta = Paths.getJsonData(Paths.join(self.songDataFolder, f"{songName}-metadata.json"))
        self.song = Song(songName)
        Paths.join(self.songDataFolder, f"{songName}-metadata.json")
        #get Audio Files    
        voices = self.getVoices(defaultMeta)
        insts = self.getInst(defaultMeta)

        metaData = self.getMetaData(defaultMeta, defaultChart)
        #Events
        events = self.importEvents(defaultChart)
        #Chart 
        characters:dict = defaultMeta["playData"]["characters"]
        bpm = defaultMeta["timeChanges"][0]["bpm"]
        for diff in defaultMeta["playData"]["difficulties"]:
            chart = self.importChart(diff, defaultChart, characters)
            chart.events = events
            chart.bpm = bpm
            chart.songVoices = voices

            chart.songInst = insts
            chart.stage = defaultMeta["playData"]["stage"]
            chart.setMetaFromDict(metaData)
            chart.songName = defaultMeta["songName"]
            chart.setMeta("rating", defaultMeta["playData"]["ratings"][diff])
            chart.setMeta("instSuffix", characters["instrumental"])

        #Variants
        for variant in defaultMeta["playData"]["songVariations"]:
            variantChart = Paths.getJsonData(Paths.join(self.songDataFolder, f"{songName}-chart-{variant}.json"))
            variantMeta = Paths.getJsonData(Paths.join(self.songDataFolder, f"{songName}-metadata-{variant}.json"))

            variant_voices = self.getVoices(variantMeta, variant)
            variant_insts = self.getInst(variantMeta)
            

            variant_metaData = self.getMetaData(variantMeta, variantChart)
            variant_bpm = variantMeta["timeChanges"][0]["bpm"]
            variant_events = self.importEvents(variantChart)
            variant_characters:dict = variantMeta["playData"]["characters"]

            for diff in variantMeta["playData"]["difficulties"]:
                
                chart = self.importChart(diff, variantChart, variant_characters, variant)
                chart.events = variant_events
                chart.bpm = variant_bpm
                chart.songVoices = variant_voices

                chart.songInst = variant_insts
                chart.stage = variantMeta["playData"]["stage"]
                chart.setMetaFromDict(variant_metaData)
                chart.songName = variantMeta["songName"]
                chart.setMeta("rating", variantMeta["playData"]["ratings"][diff])
                chart.setMeta("instSuffix", variant_characters["instrumental"])

                chart.isVariant = True
                chart.variantTag = variant


        
        #Maybe Save Variants Too

        return self.song
    def importChart(self, diff:str, chartData:dict, character:dict, variant:str = None) -> Chart:
        chartNotes = chartData["notes"][diff]
        if variant is not None:
            chart = self.song.addChart(f"{diff}-{variant}")
        else:
            chart = self.song.addChart(diff)
        
        chart.scrollSpeed = chartData["scrollSpeed"][diff]

        dadLane = chart.addLane(character["opponent"], Character.DAD)
        opponentVocals = character.get("opponentVocals", [])
        if len(opponentVocals) > 0:
            dadLane.setMeta("vocalSuffix", opponentVocals[0])

        bfLane = chart.addLane(character["player"], Character.BOYFRIEND)
        playerVocals = character.get("playerVocals", [])
        if len(playerVocals) > 0:
            bfLane.setMeta("vocalSuffix", playerVocals[0])

        chart.addLane(character["girlfriend"], Character.GF)
        for note in chartNotes:
            noteData = note["d"] % 4
            lane = chart.getLane(Character.BOYFRIEND)
            if note["d"] > 3:
                lane = chart.getLane(Character.DAD)
                
            lane.addNote(note["t"], noteData, note.get("l", 0), note.get("k", Notes.DEFAULT))
        


        return chart

    def getMetaData(self, metaData:dict, chartData:dict) -> dict:
        meta = {}
        meta["charter"] = metaData.get("charter")
        meta["artist"] = metaData.get("artist")
        meta["metaVersion"] = metaData["version"]
        meta["metaGeneratedBy"] = metaData["generatedBy"]
        meta["chartVersion"] = chartData["version"]
        meta["chartGeneratedBy"] = chartData["generatedBy"]
        return meta
    def getVoices(self, metaData:dict, variant:str = None) -> list:
        voices = []
        characters:dict = metaData["playData"]["characters"]
        voices.insert(Character.BOYFRIEND, self.getVoicePath(metaData, "player", characters.get("playerVocals"), variant))
        voices.insert(Character.DAD, self.getVoicePath(metaData, "opponent", characters.get("opponentVocals"), variant))
        return voices

    def getVoicePath(self, metaData, character:str, vocals:list[str] = None, variant:str = None):
        characterName = metaData["playData"]["characters"][character]
        suffix = ""
        if variant is not None and variant != "" and variant != "default":
            suffix = f"-{variant}"
        if vocals is None:
            charid = characterName
            charVoice = Paths.join(self.songFolder, f"Voices-{charid}{suffix}.ogg")
            while not Paths.exists(charVoice):
                suffixes = charid.split("-")
                suffixes.pop()
                charid = "-".join(suffixes)
                if charid == "":
                    charVoice = None
                    break
                charVoice = Paths.join(self.songFolder, f"Voices-{charid}{suffix}.ogg")

            if charVoice is None:
                charid = characterName
                charVoice = Paths.join(self.songFolder, f"Voices-{charid}.ogg")
                while not Paths.exists(charVoice):
                    suffixes = charid.split("-")
                    suffixes.pop()
                    charid = "-".join(suffixes)
                    if charid == "":
                        charVoice = None
                        break
                    charVoice = Paths.join(self.songFolder, f"Voices-{charid}.ogg")
            if charVoice is None:
                print(f"VOICES for {characterName} in {metaData["songName"]} not found")
                return 
            return charVoice
        else:
            for vocal in vocals:
                charVoice = Paths.join(self.songFolder, f"Voices-{vocal}{suffix}.ogg")
                if Paths.exists(charVoice):
                    return charVoice

        print(f"VOICES for {characterName} in {metaData["songName"]} not found")
        return
    def getInst(self, metaData:dict):
        variant = metaData["playData"]["characters"].get("instrumental", "")
        if variant != "":
            variant = "-" + variant
        return Paths.join(self.songFolder, f"Inst{variant}.ogg")
    
    def exportEvents(self, chart:Chart) -> list:
        events = []
        for event in chart.events:
            name = event.name
            args = {}
            match name:
                case Events.CHANGE_BUMP_INTERVAL:
                    name = "SetCameraBop"
                    args["intensity"] = event.getValue("strength")
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
            
            name, args = self.renameEvents(name, args)
            newEvent = ChartEvent(strum, name, args)
            events.append(newEvent)
        return events
    def renameEvents(self, name:str, args:dict):
        if not self.renameDefaultEvents:
            if type(args) is not dict:
                args = {"value1": args}
            return name, args
        
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

        return name, args

    
