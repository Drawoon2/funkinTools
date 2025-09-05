from PySide6.QtWidgets import QDialog, QWidget
from Funkin.ModFolder import ModFolder
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
            self.updateFromMod()

        self.ui.select_button.pressed.connect(self.selectMod)
        self.ui.import_button.pressed.connect(self.importSong)
    def selectMod(self):
        modFolder = Dialogs.openModDialog(self)
        self.mod = modFolder
        self.updateFromMod()
    def updateFromMod(self):
        if self.mod is None:
            print("ImportSongMod: mod not gived")
            return
        self.ui.showpath_label.setText(self.mod.FolderPath)
        self.ui.showengine_label.setText(self.mod.getEngineName())

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



