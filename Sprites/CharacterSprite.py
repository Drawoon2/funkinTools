from .Sprite import Sprite
from Funkin import Character
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt
from Sprites.Animation import FrameAnimator, Animator
from Constants import RenderType
class CharacterSprite(Sprite):
    def __init__(self, data:Character):
        super().__init__()
        self.data:Character = data
        self.danced:bool = False
        self.offsets:dict[str, list] = {}
        if self.data.renderType != RenderType.ATLAS:
            self.animator = FrameAnimator()
            match self.data.renderType:
                case RenderType.SPARROW | RenderType.MULTISPARROW:
                    for key, asset in self.data.assets.items():
                        self.animator.loadSparrow(asset["xml"], asset["image"])

        for name, animData in self.data.animations.items():
            if animData.indice is not None:
                self.animator.addByIndices(name, animData.prefix, animData.indice, animData.frameRate, animData.loop, animData.flipX, animData.flipY)
            else:
                self.animator.addByPrefix(name, animData.prefix, animData.frameRate, animData.loop, animData.flipX, animData.flipY)
            self.offsets[name] = animData.offset
            

        self.dance()


    
    def update(self, elapsed:float):
        if self.animator.finished:
            self.dance()
        return super().update(elapsed)
    def playAnim(self, anim:str, forced:bool = False):
        self.animator.play(anim, forced)
        offset = self.offsets.get(anim, (0, 0))
        self.offsetX = -offset[0] + self.data.position[0]
        self.offsetY = -offset[1] + self.data.position[1]
        
    def dance(self, forced:bool = False):
        if self.animator.hasAnimation("idle"):
            self.playAnim("idle")
        elif self.animator.hasAnimation("danceLeft") and self.animator.hasAnimation("danceRight"):
            self.danced = not self.danced
            if self.danced:
                self.playAnim("danceLeft")
            else:
                self.playAnim("danceRight")
                
    def onPressKey(self, key):
        match key:
            case Qt.Key.Key_Z:
                self.playAnim("singLEFT", True)
            case Qt.Key.Key_X:
                self.playAnim("singDOWN", True)
            case Qt.Key.Key_C:
                self.playAnim("singUP", True)
            case Qt.Key.Key_V:
                self.playAnim("singRIGHT", True)
        
    

    