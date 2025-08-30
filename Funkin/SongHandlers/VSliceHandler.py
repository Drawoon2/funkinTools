from .SongHandler import SongHandler
from Funkin.Song import Song, ChartEvent
from Funkin.ModFolder import VsliceMod
from Constants import Character, Events
import Paths, zipfile

class VSliceHandler(SongHandler):
    @staticmethod
    def getChartBase():
        return {
            "version": "1.0.0",
            "scrollSpeed": {},
            "events": [],
            "notes": {},
            "generatedBy": "FunkinTools VSlice Imported"
        }
    @staticmethod
    def getMetaBase():
        return {
            "version": "1.0.0",
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
    def getManifest(interName:str = "test", version:str = "1.0.0"):
        return {"version": version, "songId": interName}
    @staticmethod
    def sortNotes(note):
        return note["t"]
    @staticmethod
    def exportSong(modFolder:VsliceMod, song:Song, diff:str = "hard"):
        Paths.createFolder(modFolder.getPath(f"data/songs"))
        Paths.createFolder(modFolder.getPath(f"data/songs/{song.internName}"))
        Paths.createFolder(modFolder.getPath(f"song/{song.internName}"))

        metadata = VSliceHandler.getMetaBase()
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
                if noteType is not None:
                    addNote["k"] = noteType
                diffChart.append(addNote)
        characterList = {}
        characterList["player"] = chart.getLane(Character.BOYFRIEND).character
        characterList["opponent"] = chart.getLane(Character.DAD).character
        characterList["girlfriend"] = chart.getLane(Character.GF).character
        metadata["playData"]["characters"] = characterList
        
        diffChart.sort(key=VSliceHandler.sortNotes)



        return True
    @staticmethod
    def importSong(modFolder:VsliceMod, songName:str) -> Song:
        songDataFolder = modFolder.getPath(f"data/songs/{songName}")
        songFolder = modFolder.getPath(f"songs/{songName}")

        defaultChart = Paths.getJsonData(modFolder.getPath(f"data/songs/{songName}/{songName}-chart.json"))
        defaultMeta = Paths.getJsonData(modFolder.getPath(f"data/songs/{songName}/{songName}-metadata.json"))
        newSong = Song(songName)
        #Events
        events = VSliceHandler.getEvents(defaultChart)
        #get Audio Files    
        voices = VSliceHandler.getVoices(songFolder, defaultMeta)
        insts = VSliceHandler.getInst(songFolder, defaultMeta)

        metaData = VSliceHandler.getMetaData(defaultMeta, defaultChart)
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
                
                lane.addNote(note["t"], noteData, note.get("l", 0), note.get("k", None))
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
    
    @staticmethod
    def getMetaData(metaData:dict, chartData:dict) -> dict:
        meta = {}
        meta["charter"] = metaData.get("charter")
        meta["artist"] = metaData.get("artist")
        meta["metaVersion"] = metaData["version"]
        meta["metaGeneratedBy"] = metaData["generatedBy"]
        meta["chartVersion"] = chartData["version"]
        meta["chartGeneratedBy"] = chartData["generatedBy"]
        return meta
    @staticmethod
    def getVoices(songFolder:str, metaData:dict) -> list:
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
    @staticmethod
    def getInst(songFolder:str, metaData:dict):
        variant = metaData["playData"]["characters"].get("instrumental", "")
        if variant != "":
            variant = "-" + variant
        return Paths.join(songFolder, f"Inst{variant}.ogg")
       
    @staticmethod
    def getEvents(chart) -> list:
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
    
    
