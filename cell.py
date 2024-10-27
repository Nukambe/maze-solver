from window import Window
from line import Line
from point import Point

class Cell:
    def __init__(self, x1, y1, x2, y2, window: Window):
        self.walls = {
            "left": True,
            "right": True,
            "top": True,
            "bottom": True
        }
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__window = window

    def draw(self):
        for wall, exists in self.walls.items():
            if exists:
                point1 = Point(0, 0)
                point2 = Point(0, 0)
                match wall:
                    case "left":
                        point1.x = self.__x1
                        point1.y = self.__y1
                        point2.x = self.__x1
                        point2.y = self.__y2
                    case "right":
                        point1.x = self.__x2
                        point1.y = self.__y1
                        point2.x = self.__x2
                        point2.y = self.__y2
                    case "top":
                        point1.x = self.__x1
                        point1.y = self.__y1
                        point2.x = self.__x2
                        point2.y = self.__y1
                    case "bottom":
                        point1.x = self.__x1
                        point1.y = self.__y2
                        point2.x = self.__x2
                        point2.y = self.__y2
                line = Line(point1, point2)
                self.__window.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        here = Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)
        there = Point((to_cell.__x1 + to_cell.__x2) / 2, (to_cell.__y1 + to_cell.__y2) / 2)
        line = Line(here, there)
        self.__window.draw_line(line, "gray" if undo else "red")
