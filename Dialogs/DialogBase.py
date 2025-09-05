#This is just to be copien LOL :)
from PySide6.QtWidgets import QDialog, QWidget
from Funkin.ModFolder import ModFolder
import UI, Manager

class WidgetName(QDialog):
    def __init__(self, parent:QWidget = None):
        super().__init__(parent)
        self.ui = UI.Ui_Dialog_ModFolderCreator()
        self.ui.setupUi(self)