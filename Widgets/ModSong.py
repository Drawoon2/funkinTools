from PySide6.QtWidgets import QWidget
import UI

class ModSong(QWidget):
    def __init__(self, parent:QWidget = None):
        super().__init__(parent)
        self.ui = UI.Ui_ModSongs()
        self.ui.setupUi(self)