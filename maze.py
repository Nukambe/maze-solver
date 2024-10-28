import time
from cell import Cell
from typing import List
from window import Window

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window = None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._window: Window = window
        self._cells: List[List[Cell]] = []
        self._create_cells()

    def _create_cells(self):
        for col in range(self.num_cols):
            self._cells.append([])
            for row in range(self.num_rows):
                self._cells[-1].append(None)
                self._draw_cell(col, row)

    def _draw_cell(self, col, row):
        x1 = self.x1 + (col * self.cell_size_x)
        y1 = self.y1 + (row * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        cell = Cell(x1, y1, x2, y2, self._window)
        self._cells[col][row] = cell
        if self._window:
            cell.draw()
            self._animate()

    def _animate(self):
        self._window.redraw()
        time.sleep(0.05)
