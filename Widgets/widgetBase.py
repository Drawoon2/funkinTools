#This is just to be copien LOL :)
from PySide6.QtWidgets import QWidget
from Funkin import ModFolder
import UI, Manager

class WidgetName(QWidget):
    def __init__(self, parent:QWidget = None):
        super().__init__(parent)
        self.ui = UI.Ui_ModGlobal()
        self.ui.setupUi(self)