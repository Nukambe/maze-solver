import time
import random
from cell import Cell
from typing import List, Tuple
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
        seed = None
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
        if seed:
            random.seed(seed)

    def _create_cells(self):
        for col in range(self.num_cols):
            self._cells.append([])
            for row in range(self.num_rows):
                self._cells[-1].append(Cell(0, 0, 0, 0, self._window))
                self._draw_cell(col, row)
        self._break_entrance_and_exit()
        self._break_walls()
        self._reset_cells_visited()

    def _draw_cell(self, col: int, row: int):
        x1 = self.x1 + (col * self.cell_size_x)
        y1 = self.y1 + (row * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        cell = self._cells[col][row]
        cell._x1 = x1
        cell._y1 = y1
        cell._x2 = x2
        cell._y2 = y2

        if self._window:
            cell.draw()
            self._animate()

    def _animate(self, seconds=0.05):
        self._window.redraw()
        time.sleep(seconds)

    def _break_entrance_and_exit(self):
        self._cells[0][0].walls["top"] = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].walls["bottom"] = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls(self):
        self._break_walls_r(0, 0)

    def _break_walls_r(self, col: int, row: int):
        cell = self._cells[col][row]
        cell.visited = True

        to_visit = self._get_visit_directions(col, row)

        while True:
            neighbors: List[Tuple[str, int, int]] = []
            for direction in to_visit:
                col_direction, row_direction = to_visit[direction]
                to_col = col + col_direction
                to_row = row + row_direction
                neighbor = self._cells[to_col][to_row]
                if not neighbor.visited:
                    neighbors.append((direction, to_col, to_row))

            if len(neighbors) < 1:
                cell.draw()
                return

            random_direction, random_col, random_row = random.choice(neighbors)
            cell.walls[random_direction] = False
            cell.draw()

            random_neighbor = self._cells[random_col][random_row]
            opposite_wall = Cell.OPPOSITE_WALLS[random_direction]
            random_neighbor.walls[opposite_wall] = False
            random_neighbor.draw()

            self._break_walls_r(random_col, random_row)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, col: int, row: int):
        self._animate(0.1)
        cell = self._cells[col][row]
        cell.visited = True
        if col == self.num_cols - 1 and row == self.num_rows - 1:
            return True

        to_visit = self._get_visit_directions(col, row)
        for direction in to_visit:
            if not cell.walls[direction]:
                neighbor_col = col + to_visit[direction][0]
                neighbor_row = row + to_visit[direction][1]
                neighbor = self._cells[neighbor_col][neighbor_row]
                if not neighbor.visited:
                    cell.draw_move(neighbor)
                    solved = self._solve_r(neighbor_col, neighbor_row)
                    if solved:
                        return True
                    cell.draw_move(neighbor, undo=True)
                    self._animate(0.1)
        return False

    def _get_visit_directions(self, col: int, row: int):
        to_visit = {
            "left": (-1, 0),
            "right": (1, 0),
            "top": (0, -1),
            "bottom": (0, 1)
            }

        if col == 0:
            del to_visit["left"]
        if col == self.num_cols - 1:
            del to_visit["right"]
        if row == 0:
            del to_visit["top"]
        if row == self.num_rows - 1:
            del to_visit["bottom"]

        return to_visit
