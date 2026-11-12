import unittest
from collections import Counter


def frequency_sort(s):
    """Return s with characters grouped and ordered by decreasing frequency."""
    counts = Counter(s.lower())
    ordered = sorted(counts.items(), key=lambda item: (item[1], item[0]), reverse=True)
    return "".join(ch * count for ch, count in ordered)


class FrequencySortTests(unittest.TestCase):
    def test_most_frequent_first(self):
        self.assertEqual(frequency_sort("tree"), "eetr")

    def test_equal_frequencies_keep_groups(self):
        self.assertEqual(frequency_sort("cccaaa"), "cccaaa")

    def test_mixed_case_length(self):
        self.assertEqual(len(frequency_sort("Aabb")), 4)

    def test_longer_word(self):
        self.assertEqual(frequency_sort("loveleetcode"), "eeeeoollvtdc")

    def test_ties_follow_first_appearance(self):
        self.assertEqual(frequency_sort("abc"), "abc")

    def test_empty_string(self):
        self.assertEqual(frequency_sort(""), "")


if __name__ == "__main__":
    unittest.main()
