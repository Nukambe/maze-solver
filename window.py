from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:
    def __init__(self, width, height):
        self._root = Tk()
        self._root.geometry(f"{width}x{height}")
        self._root.title("Maze Solver")
        self._canvas = Canvas()
        self._canvas.pack(fill=BOTH, expand=True)
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()

    def close(self):
        self._running = False

    def draw_line(self, line: Line, fill: str):
        line.draw(self._canvas, fill)
