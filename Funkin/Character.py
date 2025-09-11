from Constants import RenderType, AnimationType
from Funkin.ModFolder import ModFolder, CodenameMod
import Paths
import xml.etree.ElementTree as ET
class Character:
    def __init__(self, internalName:str = "test"):
        self.internalName:str = internalName
        self.name:str = internalName.title()
        self.animations:dict[str, Animation] = {}
        self.antialiasing:bool = True
        self.icon:str = ""
        self.healthbar_color:str = "FF0000"
        self.renderType:int = RenderType.SPARROW
        self.assets:dict[str, dict] = {}
        self.flipX:str = False
        self.scale:float = 1
        self.singTime:float = 6
        self.position:list = [0, 0]
        self.camPosition:list = [0, 0]
        self.isPlayable:bool = True
        self.startAnimation:str = "idle"
    def addAnimation(self, name:str = "idle", prefix:str = "idle"):
        animation = Animation(name, prefix)
        self.animations[name] = animation
        return animation
    def getAnim(self, name:str = "idle"):
        return self.animations.get(name)
    @classmethod
    def importFromCodename(cls, mod:CodenameMod, char:str):
        characterPath = mod.getPath(f"data/characters/{char}.xml")
        character = cls(char)
        data = ET.parse(characterPath)
        root = data.getroot()
        characterData = root.attrib
        
        character.healthbar_color = characterData.get("color", "#00FF00").removeprefix("#")
        character.flipX = characterData.get("flipX", "false") == "true"
        character.scale = float(characterData.get("scale", "1"))
        character.singTime = float(characterData.get("holdTime", "6"))
        character.antialiasing = characterData.get("antialiasing", "true") == "true"
        character.position[0] = int(characterData.get("x", "0"))
        character.position[1] = int(characterData.get("y", "0"))
        character.camPosition[0] = int(characterData.get("camx", "0"))
        character.camPosition[1] = int(characterData.get("camy", "0"))

        spritePath = mod.getPath(f"images/characters/{characterData.get("sprite", char)}")
        if Paths.isDir(spritePath):
            if Paths.exists(Paths.join(spritePath, "1.xml")):
                character.renderType = RenderType.MULTISPARROW
                count = 1
                while Paths.exists(Paths.join(spritePath, f"{count}.xml")):
                    character.addAssetSparrow(Paths.join(spritePath, f"{count}"))
                    count += 1

            elif Paths.exists(Paths.join(spritePath, "Animation.json")):
                character.saveAssetAtlas(spritePath)
        elif Paths.exists(f"{spritePath}.xml"):
            character.saveAssetSparrow(spritePath)
        elif Paths.exists(f"{spritePath}.txt"):
            character.saveAssetPacker(spritePath)
        elif Paths.exists(f"{spritePath}.json"):
            character.saveAssetAsesprite(spritePath)
        else:
            print("there is nothing")


        for animation in root:
            if animation.tag != "anim":
                print("What the hell?")
                continue
            animData = animation.attrib
            anim = character.addAnimation(animData.get("name", "idle"), animData.get("anim", "idle"))
            anim.frameRate = int(animData.get("fps", "24"))
            anim.loop = animData.get("loop", "false") == "true"
            anim.offset[0] = int(animData.get("x", "0"))
            anim.offset[1] = int(animData.get("y", "0"))

            if animData.get("type", "loop") == "beat":
                anim.type = AnimationType.BEAT

            anim.forced = animData.get("forced", "false") == "true"

            if animData.get("indices") is not None:
                valueInd:str = animData.get("indices").split(",")
                indiceList = []
                for part in valueInd:
                    part = part.strip()
                    if ".." in part:
                        idx = part.index("..")
                        start = int(part[:idx].strip())
                        end = int(part[(idx + 2):].strip())
                        rangeList = list(range(start, end + 1))
                        if start > end:
                            rangeList.reverse()
                        
                        indiceList += rangeList
                    else:
                        indiceList.append(int(part))

        return character
            

    def saveAssetAtlas(self, folder):
        self.renderType = RenderType.ATLAS
        asset = {"image": Paths.join(folder, "spritemap1.png"), 
                 "spritemap": Paths.join(folder, "spritemap1.json"), 
                 "animation": Paths.join(folder, "Animation.json")
                }
        self.assets[folder] = asset
    def saveAssetSparrow(self, path):
        self.renderType = RenderType.SPARROW
        asset = {"image": f"{path}.png", "xml": f"{path}.xml"}
        self.assets[Paths.getFileName(path)] = asset
    def saveAssetPacker(self, path):
        self.renderType = RenderType.PACKER
        asset = {"image": f"{path}.png", "txt": f"{path}.txt"}
        self.assets[Paths.getFileName(path)] = asset
    def saveAssetAsesprite(self, path):
        self.renderType = RenderType.ASESPRITE
        asset = {"image": f"{path}.png", "json": f"{path}.json"}
        self.assets[Paths.getFileName(path)] = asset
    def addAssetSparrow(self, path):
        self.renderType = RenderType.MULTISPARROW
        asset = {"image": f"{path}.png", "xml": f"{path}.xml"}
        self.assets[Paths.getFileName(path)] = asset


    

class Animation:
    def __init__(self, name:str = "idle", prefix:str = "idle"):
        self.frameRate:int = 24
        self.name:str = name
        self.prefix:str = prefix
        self.indice:list[int] = None
        self.offset:list = [0, 0]
        self.loop:bool = False
        #Codename Specific
        self.type:int = AnimationType.LOOP
        self.forced:bool = False
        #Vslice Specific
        self.flipY:bool = False
        self.flipX:bool = False
