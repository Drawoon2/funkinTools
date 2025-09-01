import Paths
from Constants import Engine


class ModFolder:
    def __init__(self, path:str = ""):
        self.FolderPath:str = path
        self.apiVersion:str = None
    def getEngine(self):
        if Paths.exists(self.getPath("pack.json")):
            return Engine.PSYCH
        elif Paths.exists(self.getPath("_polymod_meta.json")):
            return Engine.VSLICE
        
        return Engine.CODENAME
    
    def getEngineName(self):
        return Engine.getName(self.getEngine())

    def getEngineFolder(self):
        pass

    def setModName(self, newName:str):
        newPath = Paths.join(Paths.getDirName(self.FolderPath), newName)
        Paths.rename(self.FolderPath, newPath)
        self.FolderPath = newPath
    def getModName(self) -> str:
        return Paths.getFileName(self.FolderPath)
    def getPath(self, path) -> str:
        return Paths.join(self.FolderPath, path)
    def listSongs(self) -> list[str]:
        return []
    def setDescription(self, new):
        pass
    def getDescription(self) -> str:
        return None
    def setIcon(self, iconPath:str):
        pass
    def getIconPath(self) -> str:
        return None
    def update(self):
        pass
    
    def __repr__(self):
        return f"Path={self.FolderPath} / Name={self.getModName()} / Engine={self.getEngineName()}"
    @classmethod
    def load(cls, path):
        return cls(path)
    