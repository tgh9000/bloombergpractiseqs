import unittest
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key):
        if key not in self.data:
            return -1
        return self.data[key]

    def put(self, key, value):
        if key in self.data:
            self.data[key] = value
            return
        if len(self.data) >= self.capacity:
            self.data.popitem(last=False)
        self.data[key] = value


class LRUCacheTests(unittest.TestCase):
    def test_put_then_get(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        self.assertEqual(cache.get(1), 1)

    def test_missing_key(self):
        cache = LRUCache(2)
        self.assertEqual(cache.get(3), -1)

    def test_evicts_oldest_when_full(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(3), 3)

    def test_get_does_not_change_eviction_order(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)
        cache.put(3, 3)
        self.assertEqual(cache.get(1), -1)

    def test_update_counts_as_use(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 10)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 10)


if __name__ == "__main__":
    unittest.main()
