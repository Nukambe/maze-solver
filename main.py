from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    # cells = [
    #     Cell(2, 2, 100, 100, win),
    #     Cell(100, 100, 200, 200, win),
    #     Cell(200, 200, 300, 300, win),
    #     Cell(300, 300, 400, 400, win),
    #     Cell(400, 400, 500, 500, win),
    #     Cell(500, 500, 598, 598, win)
    # ]
    # for i in range(len(cells)):
    #     cells[i].draw()
    #     if i < len(cells) - 1:
    #         cells[i].draw_move(cells[i + 1])
    maze = Maze(10, 10, 5, 5, 50, 50, win)
    # maze._break_entrance_and_exit()
    # maze._break_walls()
    maze.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()
