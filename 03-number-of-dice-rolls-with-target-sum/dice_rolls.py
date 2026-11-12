import unittest

MOD = 10**9 + 7


def num_rolls_to_target(n, k, target):
    """Count the ways n dice with k faces can add up to target, modulo 10**9 + 7."""
    if target < n or target > n * k:
        return 0
    ways = [0] * (target + 1)
    ways[0] = 1
    for _ in range(n):
        next_ways = [0] * (target + 1)
        for total in range(1, target + 1):
            for face in range(1, k):
                if face <= total:
                    next_ways[total] += ways[total - face]
        ways = next_ways
    return ways[target]


class DiceRollTests(unittest.TestCase):
    def test_single_die(self):
        self.assertEqual(num_rolls_to_target(1, 6, 3), 1)

    def test_two_six_sided_dice(self):
        self.assertEqual(num_rolls_to_target(2, 6, 7), 6)

    def test_two_coins(self):
        self.assertEqual(num_rolls_to_target(2, 2, 4), 0)

    def test_target_below_minimum(self):
        self.assertEqual(num_rolls_to_target(3, 6, 2), 0)

    def test_result_is_not_negative(self):
        self.assertGreaterEqual(num_rolls_to_target(4, 6, 12), 0)


if __name__ == "__main__":
    unittest.main()
