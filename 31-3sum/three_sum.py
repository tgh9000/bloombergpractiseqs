import unittest


def three_sum(nums):
    """Return all distinct triplets that sum to zero."""
    nums = sorted(nums)
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            total = nums[i] + nums[lo] + nums[hi]
            if total < 0:
                lo += 1
            elif total > 0:
                hi -= 1
            else:
                result.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
    return result


def normalise(triplets):
    return sorted(sorted(t) for t in triplets)


class ThreeSumTests(unittest.TestCase):
    def test_two_triplets(self):
        result = three_sum([-1, 0, 1, 2, -1, -4])
        self.assertEqual(normalise(result), [[-1, -1, 2], [-1, 0, 1]])

    def test_no_triplet(self):
        self.assertEqual(three_sum([0, 1, 1]), [])

    def test_all_zeros(self):
        self.assertEqual(three_sum([0, 0, 0]), [[0, 0, 0]])

    def test_repeated_values(self):
        self.assertIn([-2, 0, 2], three_sum([-2, 0, 0, 2, 2]))

    def test_repeated_values_count(self):
        self.assertEqual(len(three_sum([-2, 0, 0, 2, 2])), 2)

    def test_repeated_negative_values(self):
        self.assertEqual(normalise(three_sum([-1, -1, -1, 2, 2])), [[-1, -1, 2]])


if __name__ == "__main__":
    unittest.main()
