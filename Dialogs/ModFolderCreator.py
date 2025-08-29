from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtCore import QDir
import UI, Constants
from Funkin.ModFolder import PsychMod, CodenameMod, VsliceMod, ModFolder


class ModFolderCreator(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.mod:ModFolder = None
        self.ui = UI.Ui_Dialog_ModFolderCreator()
        self.ui.setupUi(self)
        self.ui.create_button.pressed.connect(self.create)
        self.ui.enginefolder_button.pressed.connect(self.searchEngineFolder)
    
    def searchEngineFolder(self):
        path = QFileDialog.getExistingDirectory(self, "Select the Engine Folder", QDir.currentPath())
        self.ui.engineFolderPath_label.setText(path)
        
    def create(self):
        engineFolder = self.ui.engineFolderPath_label.text()
        match self.ui.comboBox.currentIndex():
            case Constants.CODENAME:
                self.mod = CodenameMod.generate(engineFolder)
            case Constants.PSYCH:
                self.mod = PsychMod.generate(engineFolder)
            case Constants.VSLICE:
                self.mod = VsliceMod.generate(engineFolder)
        name = self.ui.name_line_edit.text()
        self.mod.setModName(name)


        self.done(1)