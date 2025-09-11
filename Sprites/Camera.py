from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtCore import Qt, QPoint
from PIL import Image
class Camera:
    def __init__(self, width = 1080, height = 720):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.scrollX = 0
        self.scrollY = 0
        self.__scrollTargetX = 0
        self.__scrollTargetY = 0
        self.__lastTargetX = None
        self.__lastTargetY = None
        self.zoom = 1
        self.target = None
        self.render:QPixmap = None
        self.canvas:Image.Image = None
        self.followLerp = 1
        pass
    def follow(self, target, followLerp):
        self.target = target
        self.followLerp = followLerp
    def update(self, elapsed):
        self.updateScroll(elapsed)

    def updateScroll(self, elapsed):
        if self.target is None:
            return
        if self.__lastTargetX is None or self.__lastTargetY is None:
            self.__lastTargetX = self.target.x
            self.__lastTargetY = self.target.y

        self.__scrollTargetX += self.target.x - self.__lastTargetX
        self.__scrollTargetY += self.target.y - self.__lastTargetY

        self.__lastTargetX = self.target.x
        self.__lastTargetY = self.target.y
        if self.followLerp >= 1:
            self.scrollX = self.__scrollTargetX
            self.scrollY = self.__scrollTargetY
        elif self.followLerp > 0:
            adjustedLerp = 1.0 - pow(1.0 - self.followLerp, elapsed * 60)
            self.scrollX += (self.__scrollTargetX - self.scrollX) * adjustedLerp
            self.scrollY += (self.__scrollTargetY - self.scrollY) * adjustedLerp

    def preDraw(self):
        self.canvas = Image.new("RGBA", (self.width, self.height))
        #self.canvas.scale(self.zoom, self.zoom)

    def draw(self):
        self.render = self.canvas.toqpixmap()
    
    