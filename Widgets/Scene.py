from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPainter, QKeyEvent
from Sprites import Sprite
class Scene(QWidget):
    def __init__(self, parent:QWidget = None, width:int = 1080, heigth:int = 720, frameRate:int = 60):
        super().__init__(parent)
        self.sprites:list[Sprite] = []
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.onUpdate)
        self.timer.start(int(1000/frameRate))
        self.setFixedSize(width, heigth)

        self.target:Sprite = None

    def paintEvent(self, event):
        with QPainter(self) as newPaint:
            for sprite in self.sprites:
                sprite.draw(newPaint)

    def keyPressEvent(self, e:QKeyEvent):
        if self.target is not None:
            self.target.onPressKey(e.key())


    def onUpdate(self):
        for sprite in self.sprites:
                sprite.update(self.timer.interval()/1000)
        self.update()

    def add(self, sprite:Sprite):
        if self.target is None:
             self.target = sprite
        self.sprites.append(sprite)

    
