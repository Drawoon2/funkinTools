import Constants, Paths



class ModFolder:
    def __init__(self, path:str = ""):
        self.FolderPath:str = path
        self.name:str = Constants.DEFAULT_MOD_NAME
    def getEngine(self):
        if Paths.exists(self.getPath("pack.json")):
            return Constants.PSYCH
        elif Paths.exists(self.getPath("_polymod_meta.json")):
            return Constants.VSLICE
        
        return Constants.CODENAME
    
    def getEngineName(self):
        match self.getEngine():
            case Constants.PSYCH:
                return "PSYCH"
            case Constants.CODENAME:
                return "CODENAME"
            case Constants.VSLICE:
                return "VSLICE"
    def getEngineFolder(self):
        pass

    def setModName(self, newName:str):
        newPath = Paths.join(Paths.getDirName(self.FolderPath), newName)
        Paths.rename(self.FolderPath, newPath)
        self.FolderPath = newPath

    def getPath(self, path) -> str:
        return Paths.join(self.FolderPath, path)
    def __repr__(self):
        return f"Path={self.FolderPath} / Name={self.name} / Engine={self.getEngineName()}"
    
class PsychMod(ModFolder):
    def __init__(self, path = ""):
        super().__init__(path)

    def getEngine(self):
        return Constants.PSYCH
    
    def setModName(self, newName:str):
        super().setModName(newName)
        data = Paths.getJsonData(self.getPath("pack.json"))
        data["name"] = newName
        Paths.saveJson(self.getPath("pack.json"), data)
    
    @classmethod
    def generate(cls, engineFolder:str):
        modFolder = Paths.join(engineFolder, f"mods/{Constants.DEFAULT_MOD_NAME}")

        Paths.createFolder(Paths.join(engineFolder, "mods"))
        Paths.createFolder(modFolder)

        mod = cls(modFolder)
        
        Paths.saveJson(mod.getPath("pack.json"), Constants.PSYCH_PACK_BASE)
        Paths.copyFile(Paths.getAssetPath("pack.png"), mod.getPath("pack.png"))

        Paths.createFolder(mod.getPath("data"))
        Paths.createFolder(mod.getPath("images"))
        Paths.createFolder(mod.getPath("songs"))

        return mod

    
class CodenameMod(ModFolder):
    def __init__(self, path = ""):
        super().__init__(path)

    def getEngine(self):
        return Constants.CODENAME
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
    
class VsliceMod(ModFolder):
    def __init__(self, path = ""):
        super().__init__(path)

    def getEngine(self):
        return Constants.VSLICE
    @classmethod
    def generate(cls, engineFolder:str):
        modFolder = Paths.join(engineFolder, f"mods/{Constants.DEFAULT_MOD_NAME}")

        Paths.createFolder(Paths.join(engineFolder, "mods"))
        Paths.createFolder(modFolder)

        mod = cls(modFolder)
        
        Paths.saveJson(mod.getPath("_polymod_meta.json"), Constants.VSLICE_POLYMOD_META)

        Paths.createFolder(mod.getPath("data"))
        Paths.createFolder(mod.getPath("images"))
        Paths.createFolder(mod.getPath("songs"))
        Paths.createFolder(mod.getPath("shared"))
        Paths.createFolder(mod.getPath("shared/images"))
        

        return mod
    
    def setModName(self, newName:str):
        super().setModName(newName)
        data = Paths.getJsonData(self.getPath("_polymod_meta.json"))
        data["title"] = newName
        Paths.saveJson(self.getPath("_polymod_meta.json"), data)
        
        
        


       