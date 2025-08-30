from .VSliceHandler import VSliceHandler
from .CodenameHandler import CodenameHandler
from .PsychHandler import PsychHandler
from .SongHandler import SongHandler

from Funkin.Song import Song
from Funkin.ModFolder import ModFolder
from Constants import Engine


def importSong(modFolder:ModFolder, songName = "test"):
    song:Song
    handler:SongHandler
    match modFolder.getEngine():
        case Engine.VSLICE:
            handler = VSliceHandler
        case Engine.CODENAME:
            handler = CodenameHandler

    song = handler.importSong(modFolder, songName)
    return song
    

def exportSong(modFolder:ModFolder, song, diff:str = "hard"):
    song:Song = song
    handler:SongHandler
    match modFolder.getEngine():
        case Engine.PSYCH:
            handler = PsychHandler

    success = handler.exportSong(modFolder, song, diff)
    if not success:
        print(f"Couldn't export {song.internName}")