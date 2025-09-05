from .VSliceHandler import VSliceHandler
from .CodenameHandler import CodenameHandler
from .PsychHandler import PsychHandler
from .SongHandler import SongHandler

from Funkin.Song import Song
from Funkin.ModFolder import ModFolder
from Constants import Engine


def importSong(modFolder:ModFolder, songName = "test", renameDefault:bool = True):
    song:Song
    handler:SongHandler = getHandler(modFolder.getEngine())
    handler.renameDefaultEvents = renameDefault
    song = handler.importSong(modFolder, songName)
    return song
    

def exportSong(modFolder:ModFolder, song:Song, diffs:list[str] = ["hard"]):
    song:Song = song
    handler:SongHandler = getHandler(modFolder.getEngine())

    success = handler.exportSong(modFolder, song, diffs)
    if not success:
        print(f"Couldn't export {song.internName}")

def exportFNFC(song:Song, diffs:list[str] = ["hard"], path:str = None):
    VSliceHandler().exportFNFC(song, diffs, path)

def getHandler(engine) -> SongHandler:
    match engine:
        case Engine.PSYCH:
            return PsychHandler()
        case Engine.CODENAME:
            return CodenameHandler()
        case Engine.VSLICE:
            return VSliceHandler()
    return SongHandler()