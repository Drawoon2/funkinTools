from PySide6.QtWidgets import QWidget, QFileDialog, QLineEdit
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QDir
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
        mod.setApiVersion(self.ui.api_input.text())
        mod.setVersion(self.ui.version_input.text())
        mod.setDiscordRPC(self.ui.discord_input.text())
    def existsMod(self):
        return Manager.instance.modFolder is not None
    def getModValues(self):
        mod = Manager.instance.modFolder
        if not self.existsMod():
            self.ui.name_input.setDisabled(True)
            self.ui.desc_input.setDisabled(True)
            self.ui.api_input.setDisabled(True)
            self.ui.discord_input.setDisabled(True)
            self.ui.version_input.setDisabled(True)
            self.ui.selecticon_button.setDisabled(True)
            self.ui.save_button.setDisabled(True)
            self.ui.clear_button.setDisabled(True)
            return
        self.ui.clear_button.setDisabled(False)
        self.ui.save_button.setDisabled(False)
        self.ui.name_input.setDisabled(False)
        self.ui.name_input.setText(mod.getModName())
        self.usableInput(self.ui.desc_input, mod.getDescription())
        self.usableInput(self.ui.api_input, mod.getApiVersion())
        self.usableInput(self.ui.discord_input, mod.getDiscordRPC())
        self.usableInput(self.ui.version_input, mod.getVersion())

        iconPath = mod.getIconPath()
        self.ui.selecticon_button.setDisabled((iconPath is None))
        self.setIcon(iconPath)
    def usableInput(self, inputObj:QLineEdit, value:str = None):
        inputObj.setDisabled((value is None))
        if value is not None:
            inputObj.setText(value)

    def setIcon(self, path:str = None):
        if Paths.exists(path):
            icon = QPixmap(path)
            self.iconPath = path
        else:
            icon = QPixmap(Paths.getAssetPath("defaultIcon.png"))
            self.iconPath = Paths.getAssetPath("defaultIcon.png")
        icon = icon.scaled(150, 150)
        self.ui.icon_preview.setPixmap(icon)
            
            