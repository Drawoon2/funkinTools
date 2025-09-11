from PySide6.QtGui import QPainter
from PIL import Image
class Animator:
    def __init__(self):
        self.finished = False
    def update(self, elapsed:float):
        pass

    def getFrame(self) -> Image.Image:
        pass

    def play(self, name, forced, reverced, startFrame):
        pass
    def hasAnimation(self, name:str) -> bool:
        return False