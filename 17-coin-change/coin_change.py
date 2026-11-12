import unittest


def coin_change(coins, amount):
    """Return the fewest coins that add up to amount, or -1 if impossible."""
    count = 0
    coins.sort(reverse=True)
    for coin in coins:
        take = amount // coin
        count += take
        amount -= take * coin
    return count if amount == 0 else -1


class CoinChangeTests(unittest.TestCase):
    def test_standard_coins(self):
        self.assertEqual(coin_change([1, 2, 5], 11), 3)

    def test_impossible_amount(self):
        self.assertEqual(coin_change([2], 3), -1)

    def test_largest_coin_is_a_trap(self):
        self.assertEqual(coin_change([2, 5], 6), 3)

    def test_zero_amount(self):
        self.assertEqual(coin_change([1], 0), 0)

    def test_non_standard_coins(self):
        self.assertEqual(coin_change([1, 3, 4], 6), 3)


if __name__ == "__main__":
    unittest.main()
