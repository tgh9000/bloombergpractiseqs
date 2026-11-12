import unittest


def find_peak_element(nums):
    """Return the index of a peak element."""
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return i
    return 0


class FindPeakElementTests(unittest.TestCase):
    def test_single_peak(self):
        self.assertEqual(find_peak_element([1, 2, 3, 1]), 2)

    def test_multiple_peaks(self):
        self.assertIn(find_peak_element([1, 2, 1, 3, 5, 6, 4]), (1, 5))

    def test_single_element(self):
        self.assertEqual(find_peak_element([1]), 0)

    def test_two_elements_peak_at_end(self):
        self.assertEqual(find_peak_element([1, 2]), 1)

    def test_strictly_decreasing(self):
        self.assertEqual(find_peak_element([3, 2, 1]), 0)

    def test_strictly_increasing(self):
        self.assertEqual(find_peak_element([1, 2, 3]), 0)


if __name__ == "__main__":
    unittest.main()
