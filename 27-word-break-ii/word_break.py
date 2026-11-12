import unittest


def word_break(s, word_dict):
    """Return every way to split s into dictionary words, joined by spaces."""
    words = set(word_dict)
    longest = max(len(word) for word in words)
    memo = {}

    def sentences_from(start):
        if start == len(s):
            return [""]
        if start in memo:
            return memo[start]
        results = []
        for end in range(start + 1, min(len(s), start + longest - 1) + 1):
            piece = s[start:end]
            if piece in words:
                for rest in sentences_from(end):
                    results.append(piece + " " + rest if rest else piece)
        memo[start] = results
        return results

    return sentences_from(0)


class WordBreakTests(unittest.TestCase):
    def test_no_valid_sentence(self):
        words = ["cats", "dog", "sand", "and", "cat"]
        self.assertEqual(word_break("catsandog", words), [])

    def test_contains_expected_sentence(self):
        words = ["apple", "pen", "applepen", "pine", "pineapple"]
        self.assertIn("pine apple pen apple", word_break("pineapplepenapple", words))

    def test_number_of_sentences(self):
        words = ["apple", "pen", "applepen", "pine", "pineapple"]
        self.assertEqual(len(word_break("pineapplepenapple", words)), 2)

    def test_two_sentences(self):
        words = ["cat", "cats", "and", "sand", "dog"]
        self.assertEqual(sorted(word_break("catsanddog", words)), ["cat sand dog", "cats and dog"])

    def test_returns_list(self):
        self.assertIsInstance(word_break("ab", ["a", "b", "xyz"]), list)


if __name__ == "__main__":
    unittest.main()
