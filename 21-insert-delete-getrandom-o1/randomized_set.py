import random
import unittest


class RandomizedSet:
    def __init__(self, rng=None):
        self._values = []
        self._positions = {}
        self._rng = rng if rng is not None else random.Random()

    def insert(self, val):
        if val in self._positions:
            return False
        self._positions[val] = len(self._values)
        self._values.append(val)
        return True

    def remove(self, val):
        if val not in self._positions:
            return False
        index = self._positions.pop(val)
        last = self._values[-1]
        self._values[index] = last
        self._positions[last] = index
        self._values.pop()
        return True

    def get_random(self):
        return self._rng.choice(list(self._positions))


class RandomizedSetTests(unittest.TestCase):
    def test_insert_and_duplicate(self):
        rs = RandomizedSet(rng=random.Random(0))
        self.assertTrue(rs.insert(1))
        self.assertFalse(rs.insert(1))

    def test_remove_missing_value(self):
        rs = RandomizedSet(rng=random.Random(0))
        self.assertFalse(rs.remove(7))

    def test_get_random_after_removing_first_value(self):
        rs = RandomizedSet(rng=random.Random(0))
        rs.insert(1)
        rs.insert(2)
        rs.remove(1)
        self.assertEqual(rs.get_random(), 2)

    def test_removed_last_value_is_never_returned(self):
        rs = RandomizedSet(rng=random.Random(0))
        rs.insert(1)
        rs.insert(2)
        rs.remove(2)
        for _ in range(20):
            self.assertEqual(rs.get_random(), 1)

    def test_reinserting_removed_value(self):
        rs = RandomizedSet(rng=random.Random(0))
        rs.insert(1)
        self.assertTrue(rs.remove(1))
        self.assertFalse(rs.insert(1))


if __name__ == "__main__":
    unittest.main()
