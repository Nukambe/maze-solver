from window import Window
from line import Line
from point import Point
from cell import Cell

def main():
    win = Window(800, 600)
    cells = [
        Cell(2, 2, 100, 100, win),
        Cell(100, 100, 200, 200, win),
        Cell(200, 200, 300, 300, win),
        Cell(300, 300, 400, 400, win),
        Cell(400, 400, 500, 500, win),
        Cell(500, 500, 598, 598, win)
    ]
    for cell in cells:
        print(cell.walls)
        cell.draw()
    win.wait_for_close()

if __name__ == "__main__":
    main()
