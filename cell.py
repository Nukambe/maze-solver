from window import Window
from line import Line
from point import Point

class Cell:
    def __init__(self, x1, y1, x2, y2, window: Window = None):
        self.walls = {
            "left": True,
            "right": True,
            "top": True,
            "bottom": True
        }
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._window = window

    def draw(self):
        for wall, exists in self.walls.items():
            if exists:
                point1 = Point(0, 0)
                point2 = Point(0, 0)
                match wall:
                    case "left":
                        point1.x = self._x1
                        point1.y = self._y1
                        point2.x = self._x1
                        point2.y = self._y2
                    case "right":
                        point1.x = self._x2
                        point1.y = self._y1
                        point2.x = self._x2
                        point2.y = self._y2
                    case "top":
                        point1.x = self._x1
                        point1.y = self._y1
                        point2.x = self._x2
                        point2.y = self._y1
                    case "bottom":
                        point1.x = self._x1
                        point1.y = self._y2
                        point2.x = self._x2
                        point2.y = self._y2
                line = Line(point1, point2)
                self._window.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        here = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        there = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        line = Line(here, there)
        self._window.draw_line(line, "gray" if undo else "red")
