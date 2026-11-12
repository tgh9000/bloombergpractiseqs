import unittest


def unique_paths(m, n):
    """Return the number of down/right paths across an m x n grid."""
    row = [1] * n
    for _ in range(m):
        for j in range(1, n):
            row[j] += row[j - 1]
    return row[-1]


class UniquePathsTests(unittest.TestCase):
    def test_single_cell(self):
        self.assertEqual(unique_paths(1, 1), 1)

    def test_three_by_two(self):
        self.assertEqual(unique_paths(3, 2), 4)

    def test_three_by_seven(self):
        self.assertEqual(unique_paths(3, 7), 28)


if __name__ == "__main__":
    unittest.main()
