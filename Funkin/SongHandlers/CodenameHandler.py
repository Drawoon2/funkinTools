from .SongHandler import SongHandler
from Funkin.Song import Song, ChartEvent, Chart
from Funkin.ModFolder import CodenameMod
from Constants import Character, Events, Camera, Notes
import Paths

class CodenameHandler(SongHandler):
    
    @staticmethod
    def importSong(modFolder:CodenameMod, songName):
        songFolder = modFolder.getPath(f"songs/{songName}")
        metaData = Paths.getJsonData(Paths.join(songFolder, "meta.json"))
        
        song = Song(songName)

        charts = Paths.listFolder(Paths.join(songFolder, "charts"))
        for chartFile in charts:
            diff = chartFile.removesuffix(".json")
            chartData = Paths.getJsonData(Paths.join(songFolder, f"charts/{chartFile}"))
            chartObj = song.addChart(diff)
            CodenameHandler.importChart(chartObj, metaData, chartData)

            chartObj.songInst = Paths.join(songFolder, "song/Inst.ogg")
            chartObj.songVoices.append(Paths.join(songFolder, "song/Voices.ogg"))

        return song
    @staticmethod
    def getEventParam(event, index:int, default = None):
        params = event["params"]
        if len(params) < index + 1:
            return default
        return params[index]

    @staticmethod
    def importChart(chart:Chart, metaData:dict, chartData:dict):
        #Other
        chart.bpm = metaData["bpm"]
        chart.songName = metaData["displayName"]
        chart.stage = chartData["stage"]
        chart.scrollSpeed = chartData["scrollSpeed"]
        chart.setMeta("version", chartData["chartVersion"])
        #Events
        for event in chartData["events"]:
            name = event["name"]
            params = event["params"]
            newparams = {}
            match event["name"]:
                case "Play Animation":
                    name = Events.PLAY_ANIMATION
                    
                    newparams["character"] = CodenameHandler.getEventParam(event, 0, Character.DAD)
                    newparams["animation"] = CodenameHandler.getEventParam(event, 1, "animation")
                    newparams["forced"] = CodenameHandler.getEventParam(event, 2, True)
                    newparams["context"] = CodenameHandler.getEventParam(event, 3, "NONE")

                case "Camera Position":
                    name = Events.CAMERA_FOCUS
                    newparams["char"] = -1
                    newparams["x"] = CodenameHandler.getEventParam(event, 0, 0)
                    newparams["y"] = CodenameHandler.getEventParam(event, 1, 0)
                    newparams["tweenMovement"] = CodenameHandler.getEventParam(event, 2, True)
                    newparams["duration"] = CodenameHandler.getEventParam(event, 3, 4)
                    newparams["ease"] = CodenameHandler.getEventParam(event, 4, "CLASSIC")
                    newparams["isOffset"] = CodenameHandler.getEventParam(event, 5, False)
                case "Camera Movement":
                    name = Events.CAMERA_FOCUS
                    newparams["char"] = params
                case "Add Camera Zoom":
                    name = Events.ADD_ZOOM
                    newparams["amount"] = CodenameHandler.getEventParam(event, 0, 0)
                    match CodenameHandler.getEventParam(event, 1, "camGame"):
                        case "camGame":
                            cam = Camera.GAME
                        case "camHUD":
                            cam = Camera.HUD
                    newparams["camera"] = cam
                case "BPM Change":
                    name = Events.CHANGE_BPM
                    newparams["bpm"] = CodenameHandler.getEventParam(event, 0, 100)
                case "Scroll Speed Change" | 'Change Scroll Speed':
                    name = Events.CHANGE_SCROLL_SPEED
                    newparams["tweenSpeed"] = CodenameHandler.getEventParam(event, 0, True)
                    newparams["speed"] = CodenameHandler.getEventParam(event, 1, 1)
                    newparams["time"] = CodenameHandler.getEventParam(event, 2, 4)
                    newparams["ease"] = CodenameHandler.getEventParam(event, 3, "linear")
                    newparams["type"] = CodenameHandler.getEventParam(event, 4, "In")
                    newparams["multiplive"] = CodenameHandler.getEventParam(event, 5, False)
                case __:
                    for i, value in enumerate(params):
                        newparams[str(i)] = value
            eventObj = ChartEvent(event["time"], name, newparams)
            chart.events.append(eventObj)
        #Notes
        for i, strumline in enumerate(chartData["strumLines"]):
            lane = chart.addLane(strumline["characters"][0], i)
            lane.setMeta("position", strumline["position"])
            for note in strumline["notes"]:
                noteData = note["id"]
                length = note["sLen"]
                strum = note["time"]
                noteType = note["type"]
                match noteType:
                    case 0:
                        noteType = None

                lane.addNote(strum, noteData, length, noteType)
        
        if len(chart.lanes) < 3:
            chart.addLane("gf", Character.GF)
