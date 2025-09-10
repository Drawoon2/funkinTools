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
        self.animator:Animator = None
        self.offsets:dict[str, list] = {}
        self.offset:list = [0, 0]
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
            

        self.animator.antialiasing = self.data.antialiasing
        self.animator.scaleX = self.data.scale
        self.animator.scaleY = self.data.scale
        self.playAnim("idle")



    def draw(self, scene:QPainter):
        self.animator.draw(scene, self.x - self.offset[0], self.y - self.offset[1])
        return super().draw(scene)
    
    def update(self, elapsed:float):
        self.animator.update(elapsed)
        return super().update(elapsed)
    def playAnim(self, anim:str, forced:bool = False):
        self.animator.play(anim, forced)
        self.offset = self.offsets.get(anim, (0, 0))
        
    def onPressKey(self, key):
        match key:
            case Qt.Key.Key_D:
                self.playAnim("singLEFT", True)
            case Qt.Key.Key_F:
                self.playAnim("singDOWN", True)
            case Qt.Key.Key_J:
                self.playAnim("singUP", True)
            case Qt.Key.Key_K:
                self.playAnim("singRIGHT", True)
        
    

    