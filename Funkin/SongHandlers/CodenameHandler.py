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
    def renameParam(self, rename, original):
        return self.renameDefaultEvents and rename or original
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
                case "Alt Animation Toggle":
                    newparams[self.renameParam("altSing", "Enable On Sing Poses")] = self.getEventParam(event, 0, True)
                    newparams[self.renameParam("altIdle", "Enable On Idle")] = self.getEventParam(event, 1, True)
                    newparams[self.renameParam("character", "Strumline")] = self.getEventParam(event, 2, 0)
                case "HScript Call":
                    newparams[self.renameParam("func", "Function Name")] = self.getEventParam(event, 0, "myFunc")
                    newparams[self.renameParam("params", "Function Parameters (String split with commas)")] = self.getEventParam(event, 1, "")
                case "Play Animation":
                    if self.renameDefaultEvents:
                        name = Events.PLAY_ANIMATION
                    
                    newparams[self.renameParam("character", "Character")] = self.getEventParam(event, 0, Character.DAD)
                    newparams[self.renameParam("animation", "Animation")] = self.getEventParam(event, 1, "animation")
                    newparams[self.renameParam("forced", "Is forced?")] = self.getEventParam(event, 2, True)
                    newparams[self.renameParam("context", "Animation Context")] = self.getEventParam(event, 3, "NONE")
                case "Camera Modulo Change":
                    if self.renameDefaultEvents:
                        name = Events.CHANGE_BUMP_INTERVAL
                    
                    newparams[self.renameParam("interval", "Modulo Interval")] = self.getEventParam(event, 0, 4)
                    newparams[self.renameParam("strength", "Bump Strength")] = self.getEventParam(event, 1, 1)
                    newparams[self.renameParam("unit", "Every Beat Type")] = self.getEventParam(event, 2, "BEAT")
                    newparams[self.renameParam("offset", "Beat Offset")] = self.getEventParam(event, 2, 0)
                case "Camera Position":
                    if self.renameDefaultEvents:
                        name = Events.CAMERA_FOCUS
                        newparams["char"] = -1

                    newparams[self.renameParam("x", "X")] = self.getEventParam(event, 0, 0)
                    newparams[self.renameParam("y", "Y")] = self.getEventParam(event, 1, 0)
                    newparams[self.renameParam("tweenMovement", "Tween Movement?")] = self.getEventParam(event, 2, True)
                    newparams[self.renameParam("duration", "Tween Time (Steps, IF NOT CLASSIC)")] = self.getEventParam(event, 3, 4)
                    newparams[self.renameParam("ease", "Tween Ease (ex: circ, quad, cube)")] = self.getEventParam(event, 4, "CLASSIC")
                    newparams[self.renameParam("type", "Tween Type (excluded if CLASSIC or linear, ex: InOut)")] = self.getEventParam(event, 5, "In")
                    newparams[self.renameParam("isOffset", "Is Offset?")] = self.getEventParam(event, 6, False)
                case "Camera Movement":
                    if self.renameDefaultEvents:
                        name = Events.CAMERA_FOCUS
                    newparams[self.renameParam("char", "Camera Target")] = self.getEventParam(event, 0, 0)
                    newparams[self.renameParam("tweenMovement", "Tween Movement?")] = self.getEventParam(event, 1, False)
                    newparams[self.renameParam("duration", "Tween Time (Steps, IF NOT CLASSIC)")] = self.getEventParam(event, 2, 4)
                    newparams[self.renameParam("ease", "Tween Ease (ex: circ, quad, cube)")] = self.getEventParam(event, 3, "CLASSIC")
                    newparams[self.renameParam("type", "Tween Type (excluded if CLASSIC or linear, ex: InOut)")] = self.getEventParam(event, 3, "In")
                case "Camera Bop":
                    newparams[self.renameParam("amount", "Amount")] = self.getEventParam(event, 0, 0.1)
                case "Camera Zoom":
                    newparams[self.renameParam("tweenZoom", "Tween Zoom?")] = self.getEventParam(event, 0, True)
                    newparams[self.renameParam("zoom", "New Zoom")] = self.getEventParam(event, 1, 1)
                    newparams[self.renameParam("cam", "Camera")] = self.getEventParam(event, 2, "camGame")
                    newparams[self.renameParam("duration", "Tween Time (Steps)")] = self.getEventParam(event, 3, 4)
                    newparams[self.renameParam("ease", "Tween Ease (ex: circ, quad, cube)")] = self.getEventParam(event, 4, "linear")
                    newparams[self.renameParam("type", "Tween Type (excluded if linear, ex: InOut)")] = self.getEventParam(event, 5, "In")
                    newparams[self.renameParam("mode", "Mode")] = self.getEventParam(event, 6, "direct")
                    newparams[self.renameParam("multiplive", "Multiplicative?")] = self.getEventParam(event, 7, True)
                case "Camera Flash":
                    newparams[self.renameParam("reverse", "Reversed?")] = self.getEventParam(event, 0, False)
                    newparams[self.renameParam("color", "Color")] = self.getEventParam(event, 1, "#FFFFFF")
                    newparams[self.renameParam("duration", "Time (Steps)")] = self.getEventParam(event, 2, 4)
                    newparams[self.renameParam("cam", "Camera")] = self.getEventParam(event, 3, "camHUD")
                case "Add Camera Zoom":
                    if self.renameDefaultEvents:
                        name = Events.ADD_ZOOM
                        match self.getEventParam(event, 1, "camGame"):
                            case "camGame":
                                cam = Camera.GAME
                            case "camHUD":
                                cam = Camera.HUD
                        newparams["camera"] = cam
                    else:
                        newparams["Camera"] = self.getEventParam(event, 1, "camGame")
                    newparams[self.renameParam("amount", "Amount")] = self.getEventParam(event, 0, 0)
                case "BPM Change":
                    if self.renameDefaultEvents:
                        name = Events.CHANGE_BPM
                    newparams[self.renameParam("bpm", "Target BPM")] = self.getEventParam(event, 0, 100)
                case "Continuous BPM Change":
                    newparams[self.renameParam("bpm", "Target BPM")] = self.getEventParam(event, 0, 100)
                    newparams[self.renameParam("duration", "Time (steps)")] = self.getEventParam(event, 1, 4)
                case "Time Signature Change":
                    newparams[self.renameParam("numerator", "Target Numerator")] = self.getEventParam(event, 0, 4)
                    newparams[self.renameParam("denominator", "Target Denominator")] = self.getEventParam(event, 1, 4)
                    newparams[self.renameParam("stepPerBeat", "Denominator is Steps Per Beat")] = self.getEventParam(event, 2, False)
                case "Scroll Speed Change" | "Change Scroll Speed":
                    if self.renameDefaultEvents:
                        name = Events.CHANGE_SCROLL_SPEED   
                    newparams[self.renameParam("tweenSpeed", "Tween Speed?")] = self.getEventParam(event, 0, True)
                    newparams[self.renameParam("speed", "New Speed")] = self.getEventParam(event, 1, 1)
                    newparams[self.renameParam("time", "Tween Time (Steps)")] = self.getEventParam(event, 2, 4)
                    newparams[self.renameParam("ease", "Tween Type (excluded if linear, ex: InOut)")] = self.getEventParam(event, 3, "linear")
                    newparams[self.renameParam("type", "New Speed")] = self.getEventParam(event, 4, "In")
                    newparams[self.renameParam("multiplive", "Multiplicative?")] = self.getEventParam(event, 5, False)
                case __:
                    newparams = self.customEventsParamParser(name, params)

            eventObj = ChartEvent(event["time"], name, newparams)
            eventObj.setMeta("codenameOriginalParams", params) #This will user for no lose data when reimporter
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
            vocalSuffix:str = strumline.get("vocalsSuffix", "")
            if vocalSuffix != "" and vocalSuffix is not None:
                voicesSuffix.insert(i, vocalSuffix)
                lane.setMeta("vocalSuffix", vocalSuffix.removeprefix("-"))

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
        
