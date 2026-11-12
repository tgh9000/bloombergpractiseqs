import unittest


def exist(board, word):
    """Return whether word can be traced through adjacent cells of board."""
    rows, cols = len(board), len(board[0])

    def search(r, c, i):
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c].lower() != word[i].lower():
            return False
        return (
            search(r + 1, c, i + 1)
            or search(r - 1, c, i + 1)
            or search(r, c + 1, i + 1)
            or search(r, c - 1, i + 1)
        )

    return any(search(r, c, 0) for r in range(rows) for c in range(cols))


def make_board():
    return [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]


class ExistTests(unittest.TestCase):
    def test_word_with_turns(self):
        self.assertTrue(exist(make_board(), "ABCCED"))

    def test_word_going_down(self):
        self.assertTrue(exist(make_board(), "SEE"))

    def test_single_cell(self):
        self.assertTrue(exist([["a"]], "a"))

    def test_word_doubling_back(self):
        self.assertTrue(exist(make_board(), "ABCB"))

    def test_cannot_reuse_cell(self):
        self.assertFalse(exist([["a", "a"]], "aaa"))

    def test_word_not_on_board(self):
        self.assertFalse(exist(make_board(), "XYZ"))


if __name__ == "__main__":
    unittest.main()
