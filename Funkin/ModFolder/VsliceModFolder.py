from .ModFolder import ModFolder
import Paths, Constants
from Constants import Engine

class VsliceMod(ModFolder):
    @staticmethod
    def generateMeta():
        return {
    	    "title": Constants.DEFAULT_MOD_NAME,
    	    "description": "",
    	    "contributors": [],
    	    "dependencies": {},
    	    "optionalDependencies": {},
    	    "api_version": "0.7.3",
    	    "mod_version": "1.0.0",
		    "license": "Apache-2.0"
	    }
    def __init__(self, path = ""):
        super().__init__(path)
        self.metadata = VsliceMod.generateMeta()
    def getIconPath(self):
        return self.getPath("_polymod_icon.png")
    def setIcon(self, iconPath):
        Paths.copyFile(iconPath, self.getIconPath())
    def getEngine(self):
        return Engine.VSLICE
    @classmethod
    def generate(cls, engineFolder:str):
        modFolder = Paths.join(engineFolder, f"mods/{Constants.DEFAULT_MOD_NAME}")

        Paths.createFolder(Paths.join(engineFolder, "mods"))
        Paths.createFolder(modFolder)

        mod = cls(modFolder)
        
        Paths.saveJson(mod.getPath("_polymod_meta.json"), mod.metadata)
        Paths.copyFile(Paths.getAssetPath("defaultIcon.png"), mod.getIconPath())

        Paths.createFolder(mod.getPath("data"))
        Paths.createFolder(mod.getPath("images"))
        Paths.createFolder(mod.getPath("songs"))
        Paths.createFolder(mod.getPath("shared"))
        Paths.createFolder(mod.getPath("shared/images"))
        

        return mod
    
    def setModName(self, newName:str):
        super().setModName(newName)
        self.metadata["title"] = newName
        Paths.saveJson(self.getPath("_polymod_meta.json"), self.metadata)
    def getModName(self):
        return self.metadata["name"]
    def update(self):
        self.metadata = Paths.getJsonData(self.getPath("_polymod_meta.json"))
    def listSongs(self):
        chartsPath = Paths.listFolder(self.getPath("data/songs"))
        songsPath = Paths.listFolder(self.getPath("songs"))
        possiblesSongs = list(dict.fromkeys(chartsPath + songsPath))
        songs = []
        for songName in possiblesSongs:
            if not Paths.exists(self.getPath(f"data/songs/{songName}/{songName}-chart.json")):
                continue
            if not Paths.exists(self.getPath(f"songs/{songName}/Inst.ogg")):
                continue
            songs.append(songName)
        return songs
    @classmethod
    def load(cls, path):
        mod = cls(path)
        mod.update()
        return mod