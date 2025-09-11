from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt, QPoint
from .Camera import Camera
class Object:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.scrollFactorX = 1
        self.scrollFactorY = 1
        self.camera:Camera = None
    def update(self, elapsed):
        pass
    def draw(self):
        pass

    def destroy(self):
        pass

    def onPressKey(self, key:int):
        pass