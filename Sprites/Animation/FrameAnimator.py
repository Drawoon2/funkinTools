from PySide6.QtGui import QPainter
from .Animator import Animator
from PIL import Image, ImageFile
import xml.etree.ElementTree as ET
class FrameAnimator(Animator):
    def __init__(self):
        super().__init__()
        self.frames:list[FrameData] = []
        self.animations:dict[str, AnimData] = {}
        self.curAnim:AnimData = None
        self.frameIndex:int = 0
        self.timer:float = 0
        self.finished = False
    def update(self, elapsed:float):
        if self.curAnim is None:
            self.timer = 0
            return 
        self.timer += elapsed
        if self.timer > 1/self.curAnim.frameRate:
            self.timer = 0
            if len(self.curAnim.frames) -1 > self.frameIndex:
                self.frameIndex += 1
            elif self.curAnim.looped:
                self.frameIndex = 0
            else:
                self.finished = True

    def draw(self, scene:QPainter, x:float = 0, y:float = 0):
        if self.curAnim is None:
            return
        index = self.frameIndex
        if self.curAnim.reversed:
            index = len(self.curAnim.frames) -1 -self.frameIndex

        frame = self.curAnim.frames[index]
        if self.flipX ^ self.curAnim.flipX:
            frame = frame.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        
        if self.flipY ^ self.curAnim.flipY:
            frame = frame.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

        mode = Image.Resampling.NEAREST
        if self.antialiasing:
            mode = Image.Resampling.BILINEAR
        frame = frame.resize((int(self.scaleX * frame.width), int(self.scaleY * frame.height)), mode)
        scene.drawPixmap(x, y, frame.toqpixmap())
        

    def play(self, name:str, forced:bool = False, reversed:bool = False, startFrame:int = 0):
        self.timer = 0
        anim = self.animations.get(name)
        if self.curAnim is not None:
            if anim == self.curAnim and not forced and not self.finished and reversed == self.curAnim.reversed:
                return
        if anim is None:
            print(f"Animation {name} not found")
            return
        self.finished = False
        self.curAnim = anim
        self.curAnim.reversed = reversed
        self.frameIndex = startFrame
        
    
    def loadSparrow(self, xml, image):
        image = Image.open(image)
        root = ET.parse(xml).getroot()

        for frame in root:
            if frame.tag != "SubTexture":
                continue
            frameInfo = frame.attrib
            x = int(frameInfo.get("x"))
            y = int(frameInfo.get("y"))
            height = int(frameInfo.get("height"))
            width = int(frameInfo.get("width"))
            frameW = width
            frameH = height
            offsetX = 0
            offsetY = 0
            flipX = frameInfo.get("flipX") == "true"
            flipY = frameInfo.get("flipY") == "true"
            if frameInfo.get("frameWidth") is not None:
                frameW = int(frameInfo.get("frameWidth"))
                frameH = int(frameInfo.get("frameHeight"))
            if frameInfo.get("frameX") is not None:
                offsetX = int(frameInfo.get("frameX"))
                offsetY = int(frameInfo.get("frameY"))
                            

            crop = image.crop((x, y, x + width, y + height))
            if frameInfo.get("rotated") == "true":
                crop = crop.transpose(Image.Transpose.ROTATE_90)        
                            
            frame = Image.new("RGBA", (frameW, frameH))

            frame.paste(crop, (-offsetX, -offsetY))
            if flipX:   
                frame = frame.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

            if flipY:   
                frame = frame.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

            frameData = FrameData(frameInfo.get("name"), frame)
            self.frames.append(frameData)

        image.close()

    def addByPrefix(self, name, prefix, frameRate, looped, flipX, flipY):
        frames = []
        for frame in self.frames:
            if frame.name.startswith(prefix):
                frames.append(frame.image)

        anim = AnimData(frames)
        anim.looped = looped
        anim.frameRate = frameRate
        anim.flipX = flipX
        anim.flipY = flipY
        anim.name = name
        self.animations[name] = anim

    def addByIndices(self, name, prefix, indices:list[int], frameRate, looped, flipX, flipY):
        temp = []
        frames = []
        for frame in self.frames:
            if frame.name.startswith(prefix):
                temp.append(frame.image)
        for idx in indices:
            frames.append(temp[idx])
        anim = AnimData(frames)
        anim.looped = looped
        anim.frameRate = frameRate
        anim.flipX = flipX
        anim.flipY = flipY
        anim.name = name
        self.animations[name] = anim
        

class FrameData:
    def __init__(self, name:str = "", image:Image.Image = None):
        self.name:str = name
        self.image:Image.Image = image

class AnimData:
    def __init__(self, frames:list[Image.Image] = []):
        self.name = ""
        self.frames:list[Image.Image] = frames
        self.flipX = False
        self.flipY = False
        self.looped = False
        self.frameRate = False
        self.reversed = False
    def __repr__(self):
        return f"Name={self.name}, frames={self.frames}"