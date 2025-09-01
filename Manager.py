from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QWidget
from Funkin.ModFolder import ModFolder


class Manager(QObject):
    onModFolderUpdate = Signal()
    def __init__(self, parent:QWidget):
        super().__init__(parent)
        self.modFolder:ModFolder = None
    def setModFolder(self, modFolder:ModFolder):
        self.modFolder = modFolder
        self.onModFolderUpdate.emit()

instance:Manager = None
def initManager(mainWindow:QWidget):
    global instance
    instance = Manager(mainWindow)
    return instance
