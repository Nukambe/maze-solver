from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main():
    width = 1020
    height = 768
    win = Window(width, height)
    cols = 30
    rows = 30
    col_size = (width - 20) / cols
    row_size = (height - 20) / rows

    maze = Maze(10, 10, rows, cols, col_size, row_size, win)
    maze.solve()

    win.wait_for_close()

if __name__ == "__main__":
    main()
