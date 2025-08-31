from .VSliceHandler import VSliceHandler
from .CodenameHandler import CodenameHandler
from .PsychHandler import PsychHandler
from .SongHandler import SongHandler

from Funkin.Song import Song
from Funkin.ModFolder import ModFolder
from Constants import Engine


def importSong(modFolder:ModFolder, songName = "test"):
    song:Song
    handler:SongHandler = getHandler(modFolder.getEngine())

    song = handler.importSong(modFolder, songName)
    return song
    

def exportSong(modFolder:ModFolder, song:Song, diff:str = "hard"):
    song:Song = song
    handler:SongHandler = getHandler(modFolder.getEngine())

    success = handler.exportSong(modFolder, song, diff)
    if not success:
        print(f"Couldn't export {song.internName}")

def exportFNFC(song:Song, diff:str = "hard", path:str = "temp"):
    VSliceHandler.exportFNFC(song, diff, path)

def getHandler(engine) -> SongHandler:
    match engine:
        case Engine.PSYCH:
            return PsychHandler
        case Engine.CODENAME:
            return CodenameHandler
        case Engine.VSLICE:
            return VSliceHandler
    return SongHandler