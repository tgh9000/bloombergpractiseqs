import random
import unittest
from itertools import permutations


class ArrayShuffler:
    def __init__(self, nums, rng=None):
        self.original = nums
        self.current = nums
        self.rng = rng if rng is not None else random.Random()

    def reset(self):
        """Return the array in its original order."""
        self.current = self.original
        return self.current

    def shuffle(self):
        """Return a random permutation of the array."""
        items = self.current
        n = len(items)
        for i in range(n):
            j = self.rng.randint(0, n - 1)
            items[i], items[j] = items[j], items[i]
        return items


class ArrayShufflerTests(unittest.TestCase):
    def test_shuffle_is_permutation(self):
        shuffler = ArrayShuffler([1, 2, 3, 4], rng=random.Random(1))
        self.assertEqual(sorted(shuffler.shuffle()), [1, 2, 3, 4])

    def test_reset_restores_elements(self):
        shuffler = ArrayShuffler([1, 2, 3], rng=random.Random(2))
        shuffler.shuffle()
        self.assertEqual(sorted(shuffler.reset()), [1, 2, 3])

    def test_reset_returns_original_order(self):
        shuffler = ArrayShuffler([1, 2, 3, 4, 5], rng=random.Random(4))
        shuffler.shuffle()
        self.assertEqual(shuffler.reset(), [1, 2, 3, 4, 5])

    def test_reset_returns_callers_list(self):
        nums = [1, 2, 3]
        shuffler = ArrayShuffler(nums)
        self.assertIs(shuffler.reset(), nums)

    def test_every_permutation_can_appear(self):
        shuffler = ArrayShuffler([1, 2, 3], rng=random.Random(3))
        seen = {tuple(shuffler.shuffle()) for _ in range(500)}
        self.assertEqual(seen, set(permutations([1, 2, 3])))

    def test_empty(self):
        self.assertEqual(ArrayShuffler([]).shuffle(), [])


if __name__ == "__main__":
    unittest.main()
