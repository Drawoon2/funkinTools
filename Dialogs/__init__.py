from .ModFolderCreator import ModFolderCreator
from .ImportSongMod import ImportSongMod

from PySide6.QtWidgets import QWidget, QFileDialog
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