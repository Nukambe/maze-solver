from tkinter import Canvas
from point import Point

class Line:
    def __init__(self, point1: Point, point2: Point):
        self._point1 = point1
        self._point2 = point2

    def draw(self, canvas: Canvas, fill: str):
        canvas.create_line(
            self._point1.x,
            self._point1.y,
            self._point2.x,
            self._point2.y,
            fill=fill,
            width=2
            )
