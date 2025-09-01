from Funkin.Song import Song
from Funkin import SongHandlers
from Funkin.ModFolder import VsliceMod, PsychMod, CodenameMod
import Paths

#Codename test
codenameMod = CodenameMod("E:/ModsFNF/friday-night-dustin/mods/dustin")

#Psych test
psychMod = PsychMod("E:/ModsFNF/duedebtsbfmixv102/mods")
#psychMod = PsychMod("D:\FNF shit\ModsFNFen creacion\PsychEngine para Charts\PsychEngine\mods\Memory-Merge-Inst")

#Vslice test
vsliceMod = VsliceMod("E:/ModsFNF/FNF OG (FNF-V-Slice)/FNF V-Slice 0.6.4/mods/Vs Nonsense V1.5")

#Codename gen
codenameModgen = PsychMod("D:/Python Things/funkinTools/testEngines/Codename/mods/test")
#Psych gen
psychModgen = PsychMod("D:/Python Things/funkinTools/testEngines/PsychEngine/mods/Template")
#Vslice gen
vsliceModgen = VsliceMod("D:/Python Things/funkinTools/testEngines/FNF V-Slice 0.7.2/mods/Template")

#song = importSong(vsliceMod, "baffled")
song = SongHandlers.importSong(vsliceMod, "baffled")

#SongHandlers.exportSong(vsliceModgen, song, "hard")
print(song.getDifficults())
SongHandlers.exportFNFC(song, "hard")