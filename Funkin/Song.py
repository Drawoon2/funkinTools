from Constants import Character, Notes
from Funkin.ModFolder import VsliceMod, PsychMod, CodenameMod
import Paths
class Song:
    def __init__(self, intern_name = "test"):
        self.internName = intern_name
        self.charts:dict[str, Chart] = {}
    def addChart(self, diff):
        chart = Chart(diff)
        self.charts[diff] = chart
        return chart
    def getChart(self, diff:str = "hard"):
        return self.charts.get(diff, None)
    def getDifficults(self) -> list:
        return list(self.charts.keys())
    def getEventsName(self) -> list:
        eventsList = []
        for key, chart in self.charts.items():
            eventsList += chart.getAllEventsName()
        return list(dict.fromkeys(eventsList).keys())
    def getNotetypes(self) -> list:
        notesList = []
        for key, chart in self.charts.items():
            notesList += chart.getAllNoteTypes()
        return list(dict.fromkeys(notesList).keys())
                
        
        
class Chart:
    def __init__(self, diff):
        self.songName:str = "test"
        self.lanes:list[ChartLane]  = []
        self.events:list[ChartEvent] = []
        self.metadata:dict = {}
        self.stage:str = ""
        self.songVoices:list[str] = []
        self.songInst:str = ""
        self.bpm:int = 100
        self.scrollSpeed:float = 1
        self.difficult:str = diff
        self.isVariant = False
        self.variantTag:str = None
    def getMeta(self, key:str, ifNone = None):
        return self.metadata.get(key, ifNone)
    def setMeta(self, key:str, value):
        self.metadata[key] = value
    def setMetaFromDict(self, dict):
        self.metadata = dict
    def getLane(self, characterID:int = Character.DAD):
        if len(self.lanes) < (characterID +1):
            return None
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
    def renameEvents(self, renameDict:dict = None): # {oldName: newName}
        for event in self.events:
            if renameDict.get(event.name) is None:
                continue
            event.name = renameDict.get(event.name)
    def removeNoteType(self, name):
        for lane in self.lanes:
            toRemoveNotes = []
            for note in lane.notes:
                if note["noteType"] == name:
                    toRemoveNotes.append(note)
            for remove in toRemoveNotes:
                lane.notes.remove(remove)
        pass
    def renameNoteType(self, renameDict:dict = None): # {oldName: newName}
        for lane in self.lanes:
            for note in lane.notes:
                if renameDict.get(note["noteType"]) is None:
                    continue
                note["noteType"] = renameDict.get(note["noteType"])
    def getAllNoteTypes(self) -> list:
        noteTypesDict = {}
        for lane in self.lanes:
            for note in lane.notes:
                noteTypesDict[note["noteType"]] = True
        
        return list(noteTypesDict.keys())
    def getAllEventsName(self) -> list:
        eventsDict = {}
        for event in self.events:
            eventsDict[event.name] = True
        return list(eventsDict.keys())
    def exportLane(index):
        pass
    

class ChartEvent:
    def __init__(self, strum:float = 0, name = "", vars:dict = None):
        self.strum = strum
        self.name = name
        self.vars:dict = vars or {}
        self.metadata = {}
    def getValue(self, key:str, default = None):
        return self.vars.get(key, default)
    def setMeta(self, key:str, value):
        self.metadata[key] = value
    def getMetadata(self, key:str, default):
        return self.metadata.get(key, default)

class ChartLane:
    def __init__(self, character = None):
        self.character = character or Character.getName(Character.DAD)
        self.notes = []
        self.metadata = {}
    def getMeta(self, key:str, ifNone = None):
        return self.metadata.get(key, ifNone)
    def setMeta(self, key:str, value):
        self.metadata[key] = value

    def addNote(self, strum:float, noteData:int = 0, length:float = 0, noteType:str = Notes.DEFAULT):
        noteInfo = {
            "strum": strum,
            "noteData": noteData,
            "length": length,
            "noteType": noteType
        }
        self.notes.append(noteInfo)
    def __repr__(self):
        return f"(ChartLane) Character = {self.character}"