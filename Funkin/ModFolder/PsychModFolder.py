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

    @classmethod
    def load(cls, path):
        mod = cls(path)
        mod.update()
        return mod
    def getEngine(self):
        return Engine.PSYCH
    def setIcon(self, iconPath):
        Paths.copyFile(iconPath, self.getIconPath())
    def getIconPath(self):
        return self.getPath("pack.png")
    def setModName(self, newName:str):
        super().setModName(newName)
        self.pack["name"] = newName
        self.updatePack()

    def getModName(self):
        return self.pack["name"]
    def setDescription(self, new):
        self.pack["description"] = new
        self.updatePack()
    def getDescription(self):
        return self.pack["description"]
    def setDiscordRPC(self, token):
        self.pack["discordRPC"] = token
        self.updatePack()
    def getDiscordRPC(self):
        return self.pack.get("discordRPC")
    
    def setApiVersion(self, version):
        super().setApiVersion(version)
        self.pack["apiVersion"] = version
        self.updatePack()
    def getApiVersion(self):
        return super().getApiVersion()
    
    def update(self):
        if Paths.exists(self.getPath("pack.json")):
            self.pack = Paths.getJsonData(self.getPath("pack.json"))
        self.apiVersion = self.pack.get("apiVersion", "1.0")
    def updatePack(self):
        Paths.saveJson(self.getPath("pack.json"), self.pack)
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
