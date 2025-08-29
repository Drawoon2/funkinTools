from Funkin import Song, ModFolder
import Paths

#Codename test

#Psych test

#Vslice test
vsliceMod = ModFolder.VsliceMod("E:/ModsFNF/FNF OG (FNF-V-Slice)/FNF V-Slice 0.6.4/mods/Vs Nonsense V1.5")

#Codename gen
codenameModgen = ModFolder.PsychMod("D:/Python Things/funkinTools/testEngines/Codename/mods/test")
#Psych gen
psychModgen = ModFolder.PsychMod("D:/Python Things/funkinTools/testEngines/PsychEngine/mods/Template")
#Vslice gen
vsliceModgen = ModFolder.VsliceMod("D:/Python Things/funkinTools/testEngines/FNF V-Slice 0.7.2/mods/test")

song = Song.fromVSlice(vsliceMod, "baffled")

song.exportToPsych(psychModgen)