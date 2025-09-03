from PySide6.QtWidgets import QMainWindow, QWidget, QMdiArea, QFileDialog
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt, QDir
from Constants import Engine
from Funkin.ModFolder import ModFolder, PsychMod, CodenameMod, VsliceMod
import UI, Dialogs, Widgets, Manager
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
        self.ui = UI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.childWindows = {}
        Manager.initManager(self)

        self.workspace = QMdiArea(self)
        self.setCentralWidget(self.workspace)


        self.ui.file_newMod.triggered.connect(self.createMod)
        self.ui.file_openMod.triggered.connect(self.openMod)
        self.generateToolbarButton("Global", self.openGlobalModWindow)
        self.generateToolbarButton("Songs/Charts", self.openSongWindow)
        self.generateToolbarButton("Characters")
        self.generateToolbarButton("Stages")

        Manager.instance.onModFolderUpdate.connect(self.updateStatusBar)
    
    
    def generateToolbarButton(self, name, connection = None):
        action:QAction = self.ui.tool_bar.addAction(name)
        if connection is not None:
            action.triggered.connect(connection)
        return action
    def openGlobalModWindow(self):
        window = Widgets.ModGlobal(self)
        self.addWidgetToWorkspace(window, "mod_global")
    def openSongWindow(self):
        window = Widgets.ModSong(self)
        self.addWidgetToWorkspace(window, "mod_song")

    def addWidgetToWorkspace(self, widget:QWidget, refName:str = "test"):
        if self.childWindows.get(refName) is not None:
            self.workspace.removeSubWindow(self.childWindows.get(refName))
        child = self.workspace.addSubWindow(widget)
        child.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        child.destroyed.connect(lambda: self.childWindows.pop(refName))
        child.show()
        self.childWindows[refName] = child
    def createMod(self):
        dialog = Dialogs.ModFolderCreator(self)
        result = dialog.exec()
        if result == 1:
            Manager.instance.setModFolder(dialog.mod)
            print(Manager.instance.modFolder)
            
        else:
            print("Couldn't create the mod Folder")
    def openMod(self):
        modFolderPath = QFileDialog.getExistingDirectory(self, "Plese select the Mod Folder", QDir.currentPath())
        engine = ModFolder.guessEngine(modFolderPath)
        modFolder = None
        match engine:
            case Engine.PSYCH:
                modFolder = PsychMod.load(modFolderPath)
            case Engine.CODENAME:
                modFolder = CodenameMod.load(modFolderPath)
            case Engine.VSLICE:
                modFolder = VsliceMod.load(modFolderPath)
        Manager.instance.setModFolder(modFolder)
    def updateStatusBar(self):
        mod = Manager.instance.modFolder
        self.statusBar().showMessage(f"Mod path: {mod.FolderPath} / Using Engine: {mod.getEngineName()}")
        