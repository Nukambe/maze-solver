from window import Window
from line import Line
from point import Point

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(0, 100), Point(50, 100)), "black")
    win.draw_line(Line(Point(100, 50), Point(100, 200)), "red")
    win.draw_line(Line(Point(0, 0), Point(500, 300)), "blue")
    win.wait_for_close()

if __name__ == "__main__":
    main()
