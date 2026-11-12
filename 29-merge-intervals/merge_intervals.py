import unittest


def merge(intervals):
    """Merge overlapping intervals."""
    intervals.sort()
    merged = []
    for start, end in intervals:
        if merged and start < merged[-1][1]:
            merged[-1][1] = end
        else:
            merged.append([start, end])
    return merged


class MergeTests(unittest.TestCase):
    def test_overlapping_pair(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        self.assertEqual(merge(intervals), [[1, 6], [8, 10], [15, 18]])

    def test_unsorted_input(self):
        self.assertEqual(merge([[8, 10], [1, 3], [2, 6]]), [[1, 6], [8, 10]])

    def test_touching_intervals(self):
        self.assertEqual(merge([[1, 4], [4, 5]]), [[1, 4], [4, 5]])

    def test_contained_interval(self):
        self.assertEqual(merge([[1, 10], [2, 3]]), [[1, 10]])

    def test_single_interval(self):
        self.assertEqual(merge([[1, 2]]), [[1, 2]])


if __name__ == "__main__":
    unittest.main()
