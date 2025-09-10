from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt, QPoint

class Sprite:
    def __init__(self):
        self.x = 0
        self.y = 0
        pass
    def update(self, elapsed):
        pass
    def draw(self, scene:QPainter):
        pass

    def destroy(self):
        pass

    def onPressKey(self, key:int):
        pass