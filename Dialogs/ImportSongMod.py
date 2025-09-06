from PySide6.QtWidgets import QDialog, QWidget
from Funkin.ModFolder import ModFolder, PsychMod, VsliceMod, CodenameMod
from Constants import Engine
from Funkin import Song, SongHandlers
import UI, Manager, Dialogs

class ImportSongMod(QDialog):
    def __init__(self, fromManager:bool = False, parent:QWidget = None):
        super().__init__(parent)
        self.ui = UI.Ui_songImportMod()
        self.ui.setupUi(self)
        self.mod:ModFolder = None
        self.song:Song = None
        self.renameDefault:bool = True
        if fromManager and Manager.instance.modFolder is not None:
            self.mod = Manager.instance.modFolder
            self.ui.engine_combobox.setCurrentIndex(self.mod.getEngine())
            self.updateFromMod()

        self.ui.select_button.pressed.connect(self.selectMod)
        self.ui.import_button.pressed.connect(self.importSong)
        self.ui.engine_combobox.currentIndexChanged.connect(self.selectEngine)
    def selectEngine(self, engine):
        if self.mod is None:
            return
        path = self.mod.FolderPath
        match engine:
            case Engine.PSYCH:
                self.mod = PsychMod.load(path)
            case Engine.CODENAME:
                self.mod = CodenameMod.load(path)
            case Engine.VSLICE:
                self.mod = VsliceMod.load(path)
        self.updateFromMod()
    def selectMod(self):
        self.mod = Dialogs.openModDialog(self)
        self.ui.engine_combobox.setCurrentIndex(self.mod.getEngine())
        self.updateFromMod()
    def updateFromMod(self):
        if self.mod is None:
            print("ImportSongMod: mod not gived")
            return
        self.ui.showpath_label.setText(self.mod.FolderPath)
        

        songs = self.mod.listSongs()

        self.ui.song_combobox.clear()
        self.ui.song_combobox.addItems(songs)

    def importSong(self):
        if self.mod is None:
            print("ImportSongMod: mod not gived")
            return
        songName = self.ui.song_combobox.currentText()

        self.song = SongHandlers.importSong(self.mod, songName, self.renameDefault)
        self.done(1)



