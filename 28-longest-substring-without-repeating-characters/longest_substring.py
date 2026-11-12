import unittest


def length_of_longest_substring(s):
    """Return the length of the longest substring without repeated characters."""
    last_seen = {}
    start = 0
    best = 0
    for i, ch in enumerate(s):
        if ch in last_seen:
            start = last_seen[ch] + 1
        last_seen[ch] = i
        best = max(best, i - start + 1)
    return best


class LongestSubstringTests(unittest.TestCase):
    def test_repeating_pattern(self):
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)

    def test_all_same(self):
        self.assertEqual(length_of_longest_substring("bbbbb"), 1)

    def test_answer_in_middle(self):
        self.assertEqual(length_of_longest_substring("pwwkew"), 3)

    def test_mirror_string(self):
        self.assertEqual(length_of_longest_substring("abba"), 3)

    def test_repeat_far_back(self):
        self.assertEqual(length_of_longest_substring("tmmzuxt"), 5)

    def test_empty(self):
        self.assertEqual(length_of_longest_substring(""), 0)


if __name__ == "__main__":
    unittest.main()
