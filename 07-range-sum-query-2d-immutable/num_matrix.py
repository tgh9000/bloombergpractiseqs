import unittest


class NumMatrix:
    def __init__(self, matrix):
        self._matrix = matrix
        self._prefix = None

    def _build_prefix(self):
        matrix = self._matrix
        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0
        self._prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                self._prefix[r + 1][c + 1] = (
                    matrix[r][c]
                    + self._prefix[r][c + 1]
                    + self._prefix[r + 1][c]
                    - self._prefix[r][c]
                )

    def sum_region(self, row1, col1, row2, col2):
        """Return the sum of the inclusive rectangle (row1, col1) to (row2, col2)."""
        if self._prefix is None:
            self._build_prefix()
        p = self._prefix
        return p[row2 + 1][col2 + 1] - p[row1][col2 + 1] - p[row2 + 1][col1] + p[row1][col1 + 1]


GRID = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5],
]


class NumMatrixTests(unittest.TestCase):
    def setUp(self):
        self.matrix = NumMatrix(GRID)

    def test_whole_grid(self):
        self.assertEqual(self.matrix.sum_region(0, 0, 4, 4), 58)

    def test_single_cell(self):
        self.assertEqual(self.matrix.sum_region(0, 3, 0, 3), 4)

    def test_part_of_first_row(self):
        self.assertEqual(self.matrix.sum_region(0, 1, 0, 3), 5)

    def test_rectangle_touching_right_edge(self):
        self.assertEqual(self.matrix.sum_region(1, 2, 2, 4), 12)

    def test_inner_rectangle(self):
        self.assertEqual(self.matrix.sum_region(2, 1, 4, 3), 14)


if __name__ == "__main__":
    unittest.main()
