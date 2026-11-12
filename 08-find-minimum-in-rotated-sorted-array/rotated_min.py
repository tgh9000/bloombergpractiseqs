import unittest


def find_min(nums):
    """Return the minimum of a rotated, strictly ascending list."""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid - 1
    return nums[lo]


class FindMinTests(unittest.TestCase):
    def test_rotated_three_times(self):
        self.assertEqual(find_min([3, 4, 5, 1, 2]), 1)

    def test_rotated_four_times(self):
        self.assertEqual(find_min([4, 5, 6, 7, 0, 1, 2]), 0)

    def test_not_rotated(self):
        self.assertEqual(find_min([11, 13, 15, 17]), 11)

    def test_single_element(self):
        self.assertEqual(find_min([1]), 1)

    def test_three_elements(self):
        self.assertEqual(find_min([3, 1, 2]), 3)

    def test_rotated_twice(self):
        self.assertEqual(find_min([4, 5, 1, 2, 3]), 1)

    def test_empty_list(self):
        with self.assertRaises(Exception):
            find_min([])


if __name__ == "__main__":
    unittest.main()
