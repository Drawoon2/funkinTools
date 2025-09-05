from Funkin.Song import Song
from Funkin import SongHandlers
from Funkin.ModFolder import VsliceMod, PsychMod, CodenameMod
import Paths

#Codename test
codenameMod = CodenameMod("E:/ModsFNF/friday-night-dustin/mods/dustin")
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

#song = importSong(vsliceMod, "baffled")
song = SongHandlers.importSong(vsliceMod, "sky")
chart = song.getChart("hard")
print(chart.getAllEventsName())
print(chart.getAllNoteTypes())
print(song.getDifficults())
#chart.renameNoteTypes({"Madness_NOTE_assets": "Hurt Note"})
#chart.removeNoteTypes("Madness_NOTE_assets")
print(chart.getAllNoteTypes())
SongHandlers.exportSong(psychModgen, song, song.getDifficults())

#SongHandlers.exportFNFC(song, song.getDifficults())