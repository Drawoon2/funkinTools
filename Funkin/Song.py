from Constants import Character, Events, BaseData
from Funkin.ModFolder import VsliceMod, PsychMod, CodenameMod
import Paths
class Song:
    def __init__(self, intern_name = "test"):
        self.internName = intern_name
        self.charts:dict[str, Chart] = {}
    def addChart(self, diff):
        chart = Chart()
        self.charts[diff] = chart
        return chart
    def getChart(self, diff:str = "hard"):
        return self.charts.get(diff, None)
                
        
        
class Chart:
    def __init__(self):
        self.songName:str = "test"
        self.lanes:list[ChartLane]  = []
        self.events:list[ChartEvent] = []
        self.metadata:dict = {}
        self.stage:str = ""
        self.songVoices:list[str] = []
        self.songInst:str = ""
        self.bpm:int = 100
        self.scrollSpeed:float = 1
    def getMeta(self, key:str, ifNone = None):
        return self.metadata.get(key, ifNone)
    def setMeta(self, key:str, value):
        self.metadata[key] = value
    def setMetaFromDict(self, dict):
        self.metadata = dict
    def getLane(self, characterID:int = Character.DAD):
        return self.lanes[characterID]
    def addLane(self, charName = "dad", pos:int = Character.DAD):
        newLane = ChartLane(charName)
        self.lanes.insert(pos, newLane)
        return newLane
    @staticmethod
    def sortEventsFunc(event):
        event:ChartEvent = event
        return event.strum
    def sortEvents(self):
        self.events.sort(key=Chart.sortEventsFunc)

    

class ChartEvent:
    def __init__(self, strum:float = 0, name = "", vars:dict = None):
        self.strum = strum
        self.name = name
        self.vars:dict = vars or {}
    def getValue(self, key:str, default = None):
        return self.vars.get(key, default)

class ChartLane:
    def __init__(self, character = None):
        self.character = character or Character.getName(Character.DAD)
        self.notes = []
        self.metadata = {}
    def getMeta(self, key:str, ifNone = None):
        return self.metadata.get(key, ifNone)
    def setMeta(self, key:str, value):
        self.metadata[key] = value

    def addNote(self, strum:float, noteData:int = 0, length:float = 0, noteType:str = None):
        noteInfo = {
            "strum": strum,
            "noteData": noteData,
            "length": length,
            "noteType": noteType
        }
        self.notes.append(noteInfo)