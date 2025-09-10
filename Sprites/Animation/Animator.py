from PySide6.QtGui import QPainter

class Animator:
    def __init__(self):
        self.flipX:bool = False
        self.flipY:bool = False
        self.scaleX:float = 1
        self.scaleY:float = 1
        self.antialiasing:bool = True
    def update(self, elapsed:float):
        pass

    def draw(self, scene:QPainter, x:float = 0, y:float = 0):
        pass

    def play(self, name, forced, reverced, startFrame):
        pass