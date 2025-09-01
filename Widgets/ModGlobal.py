from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QDir
from Funkin import ModFolder
from Constants import SearchFormat
import UI, Manager, Paths

class ModGlobal(QWidget):
    def __init__(self, parent:QWidget = None):
        super().__init__(parent)
        self.ui = UI.Ui_ModGlobal()
        self.ui.setupUi(self)
        self.iconPath:str = ""
        self.setIcon()

        Manager.instance.onModFolderUpdate.connect(self.getModValues)
        self.getModValues()
        
        self.ui.clear_button.pressed.connect(self.getModValues)
        self.ui.save_button.pressed.connect(self.updateMod)
        self.ui.selecticon_button.pressed.connect(self.searchIcon)

    def searchIcon(self):
        iconPath, filter = QFileDialog.getOpenFileName(self, "Select Icon", QDir.currentPath(), SearchFormat.IMAGE_FORMAT)
        if not Paths.exists(iconPath):
            return
        self.setIcon(iconPath)
    def updateMod(self):
        mod = Manager.instance.modFolder
        if not self.existsMod():
            return
        mod.setModName(self.ui.name_input.text())
        mod.setDescription(self.ui.desc_input.text())
        mod.setIcon(self.iconPath)
    def existsMod(self):
        return Manager.instance.modFolder is not None
    def getModValues(self):
        mod = Manager.instance.modFolder
        if not self.existsMod():
            return
        self.ui.name_input.setText(mod.getModName())

        desc = mod.getDescription()
        self.ui.desc_input.setDisabled((desc is None))
        if desc is not None:
            self.ui.desc_input.setText(desc)

        iconPath = mod.getIconPath()
        self.ui.selecticon_button.setDisabled((iconPath is None))
        self.setIcon(self.iconPath)
                
    def setIcon(self, path:str = None):
        if Paths.exists(path):
            icon = QPixmap(path)
            self.iconPath = path
        else:
            icon = QPixmap(Paths.getAssetPath("defaultIcon.png"))
            self.iconPath = Paths.getAssetPath("defaultIcon.png")
        icon.scaled(150, 150)
        self.ui.icon_preview.setPixmap(icon)
            
            