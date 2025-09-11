from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer, QPoint, Qt
from PySide6.QtGui import QPainter, QKeyEvent
from Sprites import Sprite, Camera, Object
import time
class Scene(QWidget):
    def __init__(self, parent:QWidget = None, width:int = 1080, height:int = 720, frameRate:int = 60):
        super().__init__(parent)
        self.objects:list[Object] = []
        self.cameras:list[Camera] = []
        self.target:Object = None
        self.timer = QTimer(self)
        self.lastUpdate = time.time()
        self.timer.timeout.connect(self.onUpdate)
        self.timer.start(int(1000/frameRate))
        self.setFixedSize(width, height)

        
        self.defaultCamera = Camera(width, height)
        self.addCamera(self.defaultCamera)

        self.cameraTarget:Object = Object()
        self.add(self.cameraTarget)

        self.defaultCamera.follow(self.cameraTarget, 0.04)
        self.targetZoom = 1


    def paintEvent(self, event):
        for cam in self.cameras:
            cam.preDraw()
        for sprite in self.objects:
            sprite.draw()
        with QPainter(self) as scene:
            for cam in self.cameras:
                cam.draw()
                scene.drawPixmap(QPoint(cam.x, cam.y), cam.render)
        #breakpoint()

    def keyPressEvent(self, e:QKeyEvent):
        if self.target is not None:
            self.target.onPressKey(e.key())
        match e.key():
            case Qt.Key.Key_Q:
               self.targetZoom += 0.01
               pass
            case Qt.Key.Key_E:
                self.targetZoom -= 0.01
                pass
            case Qt.Key.Key_W:
                self.cameraTarget.y -= 10
                pass
            case Qt.Key.Key_A:
                self.cameraTarget.x -= 10
                pass
            case Qt.Key.Key_S:
                self.cameraTarget.y += 10
                pass
            case Qt.Key.Key_D:
               self.cameraTarget.x += 10
               pass


    def onUpdate(self):
        elapsed = time.time() - self.lastUpdate
        for cam in self.cameras:
            cam.update(elapsed)
        for sprite in self.objects:
                sprite.update(elapsed)

        easeLerp = 1 - (elapsed * 3.125)
        self.defaultCamera.zoom = self.lerp(self.targetZoom, self.defaultCamera.zoom, easeLerp)
        self.update()
        self.lastUpdate = time.time()
    def lerp(self, min, max, ratio):
        return min + ratio * (max - min)
    def addCamera(self, cam:Camera):
        self.cameras.append(cam)
    def add(self, sprite:Object):
        if self.target is None:
            self.target = sprite
        sprite.camera = self.defaultCamera
        self.objects.append(sprite)

    
