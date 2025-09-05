from Funkin.Song import Song
from Funkin.ModFolder import ModFolder
from Constants import Engine

class SongHandler:
    def __init__(self, engine:int = 0):
        self.engine = engine
        self.song:Song = None
        self.renameDefaultEvents = True
    def getEngine(self):
        return self.engine

    #Import giving a mod and song name
    def importSong(self, modFolder:ModFolder, songName:str) -> Song:
        return Song()
    #Import giving the files
    def localImportSong(self, files:dict[str, str]) -> Song:
        return Song()
    #Export to the giving mod
    def exportSong(self, modFolder:ModFolder, song:Song, diff:str = "hard") -> bool:
        return True
    def exportSong(self, modFolder:ModFolder, song:Song, diffs:list = []) -> bool:
        return True