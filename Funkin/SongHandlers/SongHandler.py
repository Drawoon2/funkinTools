from Funkin.Song import Song
from Funkin.ModFolder import ModFolder
from Constants import Engine

class SongHandler:
    def __init__(self, engine:int = 0):
        self.engine = engine
        self.song:Song = None
    def getEngine(self):
        return self.engine
    #Import giving a mod and song name
    @staticmethod
    def importSong(modFolder:ModFolder, songName:str) -> Song:
        return Song()
    #Import giving the files
    @staticmethod
    def localImportSong(files:dict[str, str]) -> Song:
        return Song()
    #Export to the giving mod
    @staticmethod
    def exportSong(modFolder:ModFolder, song:Song, diff:str = "hard") -> bool:
        return True