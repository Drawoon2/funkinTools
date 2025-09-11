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
char2 = Character.importFromCodename(codenameMod, "coconut")
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Scene(None, 1080, 720, 30)
    window.defaultCamera.zoom = 0.6

    bg = Sprite(-150, -350).loadGraphic(codenameMod.getPath("images/stages/paradise/sunset.png"))
    bg.setScrollFactor(0.5, 0.5)
    bg.setScale(1.6, 1.6)
    bg.zoomFactor = 0.3
    window.add(bg)

    sun = Sprite(-120, -20).loadGraphic(codenameMod.getPath("images/stages/paradise/sun.png"))
    sun.setScrollFactor(0.4, 0.4)
    sun.setScale(1.2, 1.2)
    sun.zoomFactor = 0.2
    window.add(sun)

    volcano = Sprite(-500, -20).loadGraphic(codenameMod.getPath("images/stages/paradise/volcano.png"))
    volcano.setScrollFactor(0.6, 0.6)
    volcano.setScale(1.3, 1.3)
    volcano.zoomFactor = 0.4
    window.add(volcano)

    tree1 = Sprite(-1020, -150).loadGraphic(codenameMod.getPath("images/stages/paradise/treeGroup1.png"))
    tree1.setScrollFactor(0.8, 0.8)
    tree1.setScale(1.3, 1.3)
    tree1.zoomFactor = 0.8
    window.add(tree1)

    tree2 = Sprite(-200, -150).loadGraphic(codenameMod.getPath("images/stages/paradise/treeGroup2.png"))
    tree2.setScrollFactor(0.8, 0.8)
    tree2.setScale(1.3, 1.3)
    tree2.zoomFactor = 0.8
    window.add(tree2)

    tree3 = Sprite(1050, -150).loadGraphic(codenameMod.getPath("images/stages/paradise/treeGroup3.png"))
    tree3.setScrollFactor(0.8, 0.8)
    tree3.setScale(1.3, 1.3)
    tree3.zoomFactor = 0.8
    window.add(tree3)

    sand = Sprite(-450, -250).loadGraphic(codenameMod.getPath("images/stages/paradise/sand1.png"))
    sand.setScrollFactor(0.8, 0.8)
    sand.setScale(1.3, 1.3)
    sand.zoomFactor = 0.9
    window.add(sand)

    wrathiron = Sprite(730, 240).loadGraphic(codenameMod.getPath("images/stages/paradise/wrathandiron.png"))
    wrathiron.setScrollFactor(0.8, 0.8)
    wrathiron.setScale(0.55, 0.55)
    wrathiron.zoomFactor = 0.9
    window.add(wrathiron)

    trees2 = Sprite(-550, -150).loadGraphic(codenameMod.getPath("images/stages/paradise/tree2.png"))
    trees2.setScrollFactor(0.9, 0.9)
    trees2.setScale(1.2, 1.2)
    trees2.zoomFactor = 0.9
    window.add(trees2)

    sandFG = Sprite(-450, -250).loadGraphic(codenameMod.getPath("images/stages/paradise/sand2.png"))
    sandFG.setScale(1.3, 1.3)
    window.add(sandFG)


    dad = CharacterSprite(char2)
    window.add(dad)
    dad.x = -30
    dad.y = 150

    bf = CharacterSprite(char)
    window.add(bf)
    bf.x = 990
    bf.y = 190
    window.target = bf
    window.show()

    sys.exit(app.exec())