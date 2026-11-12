import unittest


def num_islands(grid):
    """Return the number of 4-directionally connected groups of "1" cells."""
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1":
                continue
            count += 1
            stack = [(r, c)]
            grid[r][c] = "0"
            while stack:
                cr, cc = stack.pop()
                for nr, nc in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
                    if 0 <= nr < rows and 0 <= nc < rows and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        stack.append((nr, nc))
    return count


class NumIslandsTests(unittest.TestCase):
    def test_one_large_island(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        self.assertEqual(num_islands(grid), 1)

    def test_square_grid(self):
        grid = [
            ["1", "1", "0"],
            ["0", "1", "0"],
            ["0", "0", "1"],
        ]
        self.assertEqual(num_islands(grid), 2)

    def test_diagonal_cells_do_not_join(self):
        grid = [
            ["1", "0"],
            ["0", "1"],
        ]
        self.assertEqual(num_islands(grid), 2)

    def test_wide_grid(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        self.assertEqual(num_islands(grid), 4)

    def test_tall_grid(self):
        grid = [
            ["1"],
            ["1"],
            ["0"],
        ]
        self.assertEqual(num_islands(grid), 1)

    def test_empty_grid(self):
        self.assertEqual(num_islands([]), 0)


if __name__ == "__main__":
    unittest.main()
