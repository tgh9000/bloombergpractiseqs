import unittest
from collections import deque


def ladder_length(begin_word, end_word, word_list):
    """Return the number of words in the shortest ladder, or 0 if none exists."""
    if end_word not in word_list:
        word_list.append(end_word)
    words = set(word_list)
    queue = deque([(begin_word, 1)])
    visited = {begin_word}
    while queue:
        word, length = queue.popleft()
        if word == end_word:
            return length
        for i in range(len(word)):
            for ch in "abcdefghijklmnopqrstuvwxy":
                candidate = word[:i] + ch + word[i + 1:]
                if candidate in words and candidate not in visited:
                    visited.add(candidate)
                    queue.append((candidate, length + 1))
    return 0


class LadderLengthTests(unittest.TestCase):
    def test_classic_ladder(self):
        words = ["hot", "dot", "dog", "lot", "log", "cog"]
        self.assertEqual(ladder_length("hit", "cog", words), 5)

    def test_end_word_missing_from_list(self):
        words = ["hot", "dot", "dog", "lot", "log"]
        self.assertEqual(ladder_length("hit", "cog", words), 5)

    def test_change_to_last_letter_of_alphabet(self):
        self.assertEqual(ladder_length("lab", "laz", ["laz"]), 2)

    def test_unreachable(self):
        self.assertEqual(ladder_length("abc", "xyz", ["xyz"]), 0)

    def test_returns_int(self):
        self.assertIsInstance(ladder_length("a", "c", ["a", "b", "c"]), int)


if __name__ == "__main__":
    unittest.main()
