from PySide6.QtGui import QPixmap
from .ModFolder import ModFolder
import Paths, Constants
from Constants import Engine

class CodenameMod(ModFolder):
    def __init__(self, path = ""):
        super().__init__(path)

    def getEngine(self):
        return Engine.CODENAME
    @classmethod
    def generate(cls, engineFolder:str):
        modFolder = Paths.join(engineFolder, f"mods/{Constants.DEFAULT_MOD_NAME}")

        Paths.createFolder(Paths.join(engineFolder, "mods"))
        Paths.createFolder(modFolder)

        mod = cls(modFolder)

        Paths.createFolder(mod.getPath("data"))
        Paths.createFolder(mod.getPath("images"))
        Paths.createFolder(mod.getPath("songs"))

        return mod
    def listSongs(self):
        possiblesSongs = Paths.listFolder(self.getPath("songs"))
        songs = []
        for songName in possiblesSongs:
            if not Paths.exists(self.getPath(f"songs/{songName}/charts")):
                continue
            songs.append(songName)
        return songs
    @classmethod
    def load(cls, path):
        return cls(path)