import unittest


def update_board(board, click):
    """Apply a click to the board and return the updated board."""
    r, c = click
    if board[r][c] == "M":
        board[r][c] = "X"
        return board

    rows, cols = len(board), len(board[0])

    def adjacent_mines(row, col):
        total = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows - 1 and 0 <= nc < cols and board[nr][nc] == "M":
                    total += 1
        return total

    def reveal(row, col):
        if not (0 <= row < rows and 0 <= col < cols) or board[row][col] != "E":
            return
        mines = adjacent_mines(row, col)
        if mines:
            board[row][col] = str(mines)
            return
        board[row][col] = "B"
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            reveal(row + dr, col + dc)

    reveal(r, c)
    return board


def fresh_board():
    return [
        ["E", "E", "E", "E", "E"],
        ["E", "E", "M", "E", "E"],
        ["E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E"],
    ]


class UpdateBoardTests(unittest.TestCase):
    def test_click_empty_area(self):
        expected = [
            ["B", "1", "E", "1", "B"],
            ["B", "1", "M", "1", "B"],
            ["B", "1", "1", "1", "B"],
            ["B", "B", "B", "B", "B"],
        ]
        self.assertEqual(update_board(fresh_board(), [3, 0]), expected)

    def test_click_mine(self):
        board = update_board(fresh_board(), [1, 2])
        self.assertEqual(board[1][2], "X")

    def test_click_square_next_to_mine(self):
        board = update_board(fresh_board(), [0, 1])
        self.assertEqual(board[0][1], "1")
        self.assertEqual(board[0][0], "E")

    def test_mine_in_bottom_row_is_counted(self):
        board = [
            ["E", "E"],
            ["E", "M"],
        ]
        self.assertEqual(update_board(board, [0, 0]), [["1", "E"], ["E", "M"]])

    def test_blank_area_does_not_spread_diagonally(self):
        board = [
            ["E", "E", "E", "M"],
            ["E", "E", "E", "E"],
            ["E", "E", "E", "E"],
            ["M", "E", "E", "E"],
            ["E", "E", "E", "E"],
        ]
        update_board(board, [0, 0])
        self.assertEqual(board[2][2], "E")

    def test_board_keeps_its_shape(self):
        board = update_board(fresh_board(), [3, 4])
        self.assertEqual((len(board), len(board[0])), (4, 5))


if __name__ == "__main__":
    unittest.main()
