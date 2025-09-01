from PySide6.QtGui import QPixmap
from .ModFolder import ModFolder
import Paths, Constants
from Constants import Engine

class PsychMod(ModFolder):
    @staticmethod
    def generatePackData():
        return {
		    "name": Constants.DEFAULT_MOD_NAME,
		    "description": "",
		    "restart": False,
		    "runsGlobally": False,
	 	    "color": [212, 212, 212]
	    }
    def __init__(self, path = ""):
        super().__init__(path)
        self.pack = PsychMod.generatePackData()

    def getEngine(self):
        return Engine.PSYCH
    def setIcon(self, iconPath):
        Paths.copyFile(iconPath, self.getIconPath())
    def getIconPath(self):
        return self.getPath("pack.png")
    def setModName(self, newName:str):
        super().setModName(newName)
        self.pack["name"] = newName
        Paths.saveJson(self.getPath("pack.json"), self.pack)
    def getModName(self):
        return self.pack["name"]
    def setDescription(self, new):
        self.pack["description"] = new
        Paths.saveJson(self.getPath("pack.json"), self.pack)
    def getDescription(self):
        return self.pack["description"]
    def update(self):
        self.pack = Paths.getJsonData(self.getPath("pack.json"))
    @classmethod
    def generate(cls, engineFolder:str):
        modFolder = Paths.join(engineFolder, f"mods/{Constants.DEFAULT_MOD_NAME}")

        Paths.createFolder(Paths.join(engineFolder, "mods"))
        Paths.createFolder(modFolder)

        mod = cls(modFolder)
        
        Paths.saveJson(mod.getPath("pack.json"), mod.pack)
        Paths.copyFile(Paths.getAssetPath("defaultIcon.png"), mod.getIconPath())

        Paths.createFolder(mod.getPath("data"))
        Paths.createFolder(mod.getPath("images"))
        Paths.createFolder(mod.getPath("songs"))

        return mod
    def listSongs(self):
        chartsPath = Paths.listFolder(self.getPath("data/songs"))
        songsPath = Paths.listFolder(self.getPath("songs"))
        possiblesSongs = list(dict.fromkeys(chartsPath + songsPath))
        songs = []
        for songName in possiblesSongs:
            if not Paths.isDir(self.getPath(f"data/{songName}")):
                continue
            if not Paths.exists(self.getPath(f"songs/{songName}/Inst.ogg")):
                continue
            songs.append(songName)
        return songs
