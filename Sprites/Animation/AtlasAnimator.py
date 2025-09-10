from PySide6.QtGui import QPainter

class Animator:
    def __init__(self):
        pass
    def update(self, elapsed:float):
        pass

    def draw(self, scene:QPainter, x:float = 0, y:float = 0):
        pass

    def play(self, name, forced, reverced, startFrame):
        pass