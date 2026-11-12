import unittest


def subsets(nums):
    """Return every subset of nums."""
    result = []
    current = []

    def backtrack(start):
        result.append(current)
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1)
            current.pop()

    backtrack(0)
    return result


class SubsetsTests(unittest.TestCase):
    def test_number_of_subsets(self):
        self.assertEqual(len(subsets([1, 2, 3])), 8)

    def test_empty_input(self):
        self.assertEqual(subsets([]), [[]])

    def test_contains_empty_subset(self):
        self.assertIn([], subsets([1, 2]))

    def test_single_element(self):
        self.assertEqual(len(subsets([5])), 2)

    def test_single_element_subsets(self):
        self.assertEqual(subsets([1]), [[], []])

    def test_all_subsets_of_three(self):
        expected = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        self.assertEqual(sorted(sorted(s) for s in subsets([1, 2, 3])), expected)


if __name__ == "__main__":
    unittest.main()
