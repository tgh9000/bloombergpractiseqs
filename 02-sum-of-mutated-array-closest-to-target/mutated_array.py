import unittest


def find_best_value(arr, target):
    """Return the cap whose capped array sum is closest to target."""
    arr.sort()
    values = arr
    remaining = target
    n = len(values)
    for i, x in enumerate(values):
        cap = remaining / (n - i)
        if cap < x:
            return round(cap)
        remaining -= x
    return values[-1]


class FindBestValueTests(unittest.TestCase):
    def test_cap_between_values(self):
        self.assertEqual(find_best_value([4, 9, 3], 10), 4)

    def test_target_equals_total(self):
        self.assertEqual(find_best_value([2, 3, 5], 10), 5)

    def test_large_values(self):
        self.assertEqual(find_best_value([60864, 25176, 27249, 21296, 20204], 56803), 11361)

    def test_target_above_total(self):
        self.assertEqual(find_best_value([1, 2, 3], 100), 3)

    def test_tie_between_two_caps(self):
        self.assertEqual(find_best_value([2, 2], 3), 1)

    def test_returns_integer(self):
        self.assertIsInstance(find_best_value([5, 5, 5], 7), int)


if __name__ == "__main__":
    unittest.main()
