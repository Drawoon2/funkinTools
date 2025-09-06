from .ModFolderCreator import ModFolderCreator
from .ImportSongMod import ImportSongMod

from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import QDir
from Funkin.ModFolder import PsychMod, CodenameMod, VsliceMod, ModFolder
from Constants import Engine
import UI

def openModDialog(parent:QWidget) -> ModFolder:
    modFolderPath = QFileDialog.getExistingDirectory(parent, "Plese select the Mod Folder", QDir.currentPath())
    engine = ModFolder.guessEngine(modFolderPath)
    modFolder = None
    match engine:
        case Engine.PSYCH:
            modFolder = PsychMod.load(modFolderPath)
        case Engine.CODENAME:
            modFolder = CodenameMod.load(modFolderPath)
        case Engine.VSLICE:
            modFolder = VsliceMod.load(modFolderPath)
    return modFolder

def errorDialog(parent:QWidget, title:str, info:str):
    QMessageBox.critical(parent, title, info)

def warningDialog(parent:QWidget, title:str, info:str):
    QMessageBox.warning(parent, title, info)

def informativeDialog(parent:QWidget, title:str, info:str):
    QMessageBox.information(parent, title, info)