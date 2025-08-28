from PySide6.QtWidgets import QMainWindow
from ModFolder import ModFolder
import UI, Dialogs
#V-Slice
#Mod Folder Generator
#Album Generator
#Playable Character Generator
#Character Porter
#Song Porter

#Psych
#Mod Folder Generator
#Convert Psych Stages in stage scripts or port it in V-Slice Stages
#Character Porter
#Song Porter

#Codename
#Mod Folder Generator
#Character Porter
#Song Porter

class FunkinWindow(QMainWindow):
    def __init__(self):
        super().__init__(None)
        self.mod:ModFolder = None
        self.ui = UI.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.file_newMod.triggered.connect(self.createMod)
    def updateGlobal(self):
        pass
    def createMod(self):
        dialog = Dialogs.ModFolderCreator(self)
        result = dialog.exec()
        if result == 1:
            self.mod = dialog.mod
            print(self.mod)
        