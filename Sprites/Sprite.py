from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt, QPoint
from PIL import Image
from Sprites.Animation import FrameAnimator, Animator
from .Object import Object
import math
class Sprite(Object):
    def __init__(self, x:float = 0, y:float = 0):
        super().__init__(x, y)
        self.offsetX = 0
        self.offsetY = 0
        self.scaleX = 1
        self.scaleY = 1
        self.zoomFactor = 1 # This is to see codename stages
        self.graphic:Image.Image = None
        self.antialiasing = False
        self.animator:Animator = None
        self.optimization:bool = True

    def update(self, elapsed):
        if self.animator is not None:
            self.animator.update(elapsed)
    def draw(self):
        camera = self.camera
        if self.animator is not None:
            self.graphic = self.animator.getFrame()
        if self.graphic is None:
            return
        graphic = self.graphic
        
        mode = Image.Resampling.NEAREST
        if self.antialiasing:
            mode = Image.Resampling.BILINEAR
        
        camW = camera.width
        camH = camera.height
        
        posX = math.ceil((self.x + self.offsetX - camera.scrollX * self.scrollFactorX) * camera.zoom)
        posY = math.ceil((self.y + self.offsetY - camera.scrollY * self.scrollFactorY) * camera.zoom)
        if posX > camW or posY > camH:
            return 
        
        diff = 1
        if self.zoomFactor != 1:
            requestedZoom = max(1 + (camera.zoom -1) * self.zoomFactor, 0)
            diff = requestedZoom / camera.zoom
        frame = graphic.resize((int(self.scaleX * graphic.width * diff * camera.zoom), int(self.scaleY * graphic.height * diff * camera.zoom)), mode)

        if posX + frame.width < 1 or posY + frame.height < 1:
            return 
        
        if self.optimization:
            relativePosX = 0
            relativePosY = 0
            if posX >= 0:
                width = min(camW -posX, frame.width,)
            else:
                width = min(posX + frame.width, camW)
                relativePosX = -posX
                posX = 0

            if posY >= 0:
                height = min(camH - posY, frame.height)  
            else:
                height = min(posY + frame.height, camH)
                relativePosY = -posY
                posY = 0

            width = max(width, 1)
            height = max(height, 1)
            camera.canvas.alpha_composite(frame, (posX, posY), (relativePosX, relativePosY, relativePosX+ width, relativePosY + height))
        else:
            camera.canvas.alpha_composite(frame, (posX, posY))

    def loadGraphic(self, path):
        with Image.open(path) as img:
            image = img.copy()
            image = image.convert("RGBA")
            self.graphic:Image.Image = image
        
        return self
    def setScrollFactor(self, x:float = 1, y:float = 1):
        self.scrollFactorX = x
        self.scrollFactorY = y
    def setScale(self, x:float = 1, y:float = 1):
        self.scaleX = x
        self.scaleY = y
    def destroy(self):
        pass

    def onPressKey(self, key:int):
        pass