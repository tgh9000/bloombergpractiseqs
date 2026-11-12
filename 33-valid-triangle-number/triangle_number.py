import unittest


def triangle_number(nums):
    """Count triplets that can be the side lengths of a triangle."""
    nums = sorted(nums)
    count = 0
    for k in range(len(nums) - 1, 1, -1):
        lo, hi = 0, k - 1
        while lo < hi:
            if nums[lo] + nums[hi] >= nums[k]:
                count += hi - lo
                hi -= 1
            else:
                lo += 1
    return count


class TriangleNumberTests(unittest.TestCase):
    def test_mixed_lengths(self):
        self.assertEqual(triangle_number([4, 2, 3, 4]), 4)

    def test_all_equal_sides(self):
        self.assertEqual(triangle_number([3, 3, 3, 3]), 4)

    def test_some_triplets_too_flat(self):
        self.assertEqual(triangle_number([2, 2, 3, 4]), 3)

    def test_consecutive_lengths(self):
        self.assertEqual(triangle_number([1, 2, 3]), 1)

    def test_empty(self):
        self.assertEqual(triangle_number([]), 0)

    def test_too_few_sides(self):
        self.assertEqual(triangle_number([1, 1]), 0)


if __name__ == "__main__":
    unittest.main()
