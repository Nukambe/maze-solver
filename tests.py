import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def setUp(self):
        self.num_cols = 12
        self.num_rows = 10
        self.maze = Maze(0, 0, self.num_rows, self.num_cols, 10, 10)
        return super().setUp()


    def test_maze_create_cells(self):
        self.assertEqual(
            len(self.maze._cells),
            self.num_cols,
        )
        self.assertEqual(
            len(self.maze._cells[0]),
            self.num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        # self.maze._break_entrance_and_exit()
        self.assertFalse(self.maze._cells[0][0].walls["top"])
        self.assertFalse(self.maze._cells[-1][-1].walls["bottom"])

    def test_maze_reset_visited(self):
        for col in self.maze._cells:
            for cell in col:
                self.assertFalse(cell.visited, f"Visited is still true for cell: {cell}")

if __name__ == "__main__":
    unittest.main()
