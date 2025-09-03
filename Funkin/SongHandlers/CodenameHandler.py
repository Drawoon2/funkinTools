from .SongHandler import SongHandler
from Funkin.Song import Song, ChartEvent, Chart
from Funkin.ModFolder import CodenameMod
from Constants import Character, Events, Camera, Notes, Engine
import Paths

class CodenameHandler(SongHandler):
    def __init__(self):
        super().__init__(Engine.CODENAME)
        self.songFolder:str = None
        self.eventsFolder:str = None

    def importSong(self, modFolder:CodenameMod, songName):
        self.songFolder = modFolder.getPath(f"songs/{songName}")
        self.eventsFolder = modFolder.getPath(f"data/events")
        metaData = Paths.getJsonData(Paths.join(self.songFolder, "meta.json"))
        
        song = Song(songName)

        charts = Paths.listFolder(Paths.join(self.songFolder, "charts"))
        for chartFile in charts:
            diff = chartFile.removesuffix(".json")
            chartData = Paths.getJsonData(Paths.join(self.songFolder, f"charts/{chartFile}"))
            chartObj = song.addChart(diff)
            self.importChart(chartObj, metaData, chartData)

            chartObj.songInst = Paths.join(self.songFolder, "song/Inst.ogg")

        return song
    def getEventParam(self, event, index:int, default = None):
        params = event["params"]
        if len(params) < index + 1:
            return default
        return params[index]
    def customEventsParamParser(self, event:str, params:list) -> dict:
        eventDataPath = Paths.join(self.eventsFolder, f"{event}.json")
        newparams:dict = {}
        if not Paths.exists(eventDataPath):
            for i, value in enumerate(params):
                newparams[str(i)] = value
            return newparams
        
        eventData = Paths.getJsonData(eventDataPath)
        for i, paramData in enumerate(eventData["params"]):
            value = paramData.get("defaultValue")
            if len(params) >= i +1:
                value = params[i]
            newparams[paramData.get("name", str(i))] = value
        return newparams
            
    def importChart(self, chart:Chart, metaData:dict, chartData:dict):
        #Other
        chart.bpm = metaData["bpm"]
        chart.songName = metaData["displayName"]
        chart.stage = chartData["stage"]
        chart.scrollSpeed = chartData["scrollSpeed"]
        chart.setMeta("version", chartData.get("chartVersion"))
        #Events
        for event in chartData["events"]:
            name = event["name"]
            params = event["params"]
            newparams = {}
            match event["name"]:
                case "Play Animation":
                    name = Events.PLAY_ANIMATION
                    
                    newparams["character"] = self.getEventParam(event, 0, Character.DAD)
                    newparams["animation"] = self.getEventParam(event, 1, "animation")
                    newparams["forced"] = self.getEventParam(event, 2, True)
                    newparams["context"] = self.getEventParam(event, 3, "NONE")
                case "Camera Modulo Change":
                    name = Events.CHANGE_BUMP_INTERVAL
                    newparams["interval"] = self.getEventParam(event, 0, 4)
                    newparams["stregth"] = self.getEventParam(event, 1, 1)
                    newparams["unit"] = self.getEventParam(event, 2, "BEAT")
                    newparams["offset"] = self.getEventParam(event, 2, 0)
                case "Camera Position":
                    name = Events.CAMERA_FOCUS
                    newparams["char"] = -1
                    newparams["x"] = self.getEventParam(event, 0, 0)
                    newparams["y"] = self.getEventParam(event, 1, 0)
                    newparams["tweenMovement"] = self.getEventParam(event, 2, True)
                    newparams["duration"] = self.getEventParam(event, 3, 4)
                    newparams["ease"] = self.getEventParam(event, 4, "CLASSIC")
                    newparams["isOffset"] = self.getEventParam(event, 5, False)
                case "Camera Movement":
                    name = Events.CAMERA_FOCUS
                    newparams["char"] = params[0]
                case "Add Camera Zoom":
                    name = Events.ADD_ZOOM
                    newparams["amount"] = self.getEventParam(event, 0, 0)
                    match self.getEventParam(event, 1, "camGame"):
                        case "camGame":
                            cam = Camera.GAME
                        case "camHUD":
                            cam = Camera.HUD
                    newparams["camera"] = cam
                case "BPM Change":
                    name = Events.CHANGE_BPM
                    newparams["bpm"] = self.getEventParam(event, 0, 100)
                case "Scroll Speed Change" | "Change Scroll Speed":
                    name = Events.CHANGE_SCROLL_SPEED
                    newparams["tweenSpeed"] = self.getEventParam(event, 0, True)
                    newparams["speed"] = self.getEventParam(event, 1, 1)
                    newparams["time"] = self.getEventParam(event, 2, 4)
                    newparams["ease"] = self.getEventParam(event, 3, "linear")
                    newparams["type"] = self.getEventParam(event, 4, "In")
                    newparams["multiplive"] = self.getEventParam(event, 5, False)
                case __:
                    newparams = self.customEventsParamParser(name, params)

            eventObj = ChartEvent(event["time"], name, newparams)
            eventObj.setMeta("codenameOriginalParams", params) #This will user for no lose data or mix
            chart.events.append(eventObj)
        voicesSuffix = []

        noteTypes = chartData.get("noteTypes", [])
        #Notes
        for i, strumline in enumerate(chartData["strumLines"]):
            strumType = strumline["type"]
            index = 0
            chartLane = chart.getLane(strumType)
            match strumType:
                case Character.DAD:
                    if chartLane is None or chartLane.getMeta("type") != Character.DAD:
                        index = Character.DAD
                    else:
                        index = Character.EXTRA
                case Character.BOYFRIEND:
                    if chartLane is None or chartLane.getMeta("type") != Character.BOYFRIEND:
                        index = Character.BOYFRIEND
                    else:
                        index = Character.EXTRA
                case Character.GF:
                    if chartLane is None or chartLane.getMeta("type") != Character.GF:
                        index = Character.GF
                    else:
                        index = Character.EXTRA
                case __:
                    index = Character.EXTRA

                
            lane = chart.addLane(strumline["characters"][0], index)
            lane.setMeta("type", strumType)
            vocalSuffix = strumline.get("vocalsSuffix", "")
            if vocalSuffix != "":
                voicesSuffix.insert(i, vocalSuffix)
            lane.setMeta("vocalsSuffix", vocalSuffix)

            lane.setMeta("position", strumline["position"])

            for note in strumline["notes"]:
                noteData = note["id"]
                length = note["sLen"]
                strum = note["time"]
                noteType = note["type"]
                
                match noteType:
                    case 0:
                        noteType = Notes.DEFAULT
                    case __:
                        if len(noteTypes) < noteType:
                            noteType = str(noteType)
                        else:
                            noteType = noteTypes[noteType -1]

                lane.addNote(strum, noteData, length, noteType)
        if len(chart.lanes) < 3:
            chart.addLane("gf", Character.GF)
        #Voices
        for suffix in voicesSuffix:
            if suffix is None:
                continue
            path = Paths.join(self.songFolder, f"song/Voices{suffix}.ogg")
            if Paths.exists(path):
                chart.songVoices.append(path)

        if len(chart.songVoices) < 1:
            chart.songVoices.append(Paths.join(self.songFolder, f"song/Voices.ogg"))
            print("Not found voices with suffix")
        
