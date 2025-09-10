import sys
from PySide6.QtWidgets import QApplication
from Widgets import Scene
from Funkin.Character import Character
from Sprites import Sprite, CharacterSprite
from Funkin.ModFolder import VsliceMod, PsychMod, CodenameMod
import Paths

#Codename test
#codenameMod = CodenameMod("E:/ModsFNF/friday-night-dustin/mods/dustin")
codenameMod = CodenameMod("E:\ModsFNF\MCM Demo\mods\MCM")
#codenameMod = CodenameMod("E:\ModsFNF\monsterofmonsterscodename\MonsterOfMonstersCODENAME/assets")
#Psych test
psychMod = PsychMod("E:/ModsFNF/duedebtsbfmixv102/mods")
#psychMod = PsychMod("D:\FNF shit\ModsFNFen creacion\PsychEngine para Charts\PsychEngine\mods\Memory-Merge-Inst")

#Vslice test
#vsliceMod = VsliceMod("E:/ModsFNF/FNF OG (FNF-V-Slice)/FNF V-Slice 0.6.4/mods/Vs Nonsense V1.5")
vsliceMod = VsliceMod("E:\Descargas\SKY REBORN [THE PICO UPDATE]")
#Codename gen
codenameModgen = PsychMod("D:/Python Things/funkinTools/testEngines/Codename/mods/test")
#Psych gen
psychModgen = PsychMod("D:/Python Things/funkinTools/testEngines/PsychEngine/mods/Template")
#Vslice gen
vsliceModgen = VsliceMod("D:/Python Things/funkinTools/testEngines/FNF V-Slice 0.7.2/mods/Template")

char = Character.importFromCodename(codenameMod, "berryfriend")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Scene()
    charSpr = CharacterSprite(char)
    window.add(charSpr)
    charSpr.x = 400
    charSpr.y = 200
    window.show()

    sys.exit(app.exec())