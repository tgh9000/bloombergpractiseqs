import unittest


def find_best_value(arr, target):
    """Return the cap whose capped array sum is closest to target."""
    values = sorted(arr.copy())
    remaining = target
    n = len(values)
    for i, x in enumerate(values): 
        k = n - i
        if remaining <= x * k:
            cap = remaining // k
            if remaining - cap * k <= (cap + 1) * k - remaining:
                return cap
            return cap + 1
        remaining -= x
    return values[-1]


class FindBestValueTests(unittest.TestCase):
    def test_cap_between_values(self):
        self.assertEqual(find_best_value([4, 9, 3], 10), 3)

    def test_target_equals_total(self):
        self.assertEqual(find_best_value([2, 3, 5], 10), 5)

    def test_large_values(self):
        self.assertEqual(find_best_value([60864, 25176, 27249, 21296, 20204], 56803), 11361)

    def test_target_above_total(self):
        self.assertEqual(find_best_value([1, 2, 3], 100), 3)

    def test_target_above_total(self):
        input = [1,2,3]
        find_best_value(input, 100)
        self.assertEqual(input, [1,2,3])


    def test_tie_rounds_down_from_even(self):
        self.assertEqual(find_best_value([2, 2], 3), 1)

    def test_rounds_down_when_closer(self):
        self.assertEqual(find_best_value([5, 5, 5], 7), 2)

    def test_cap_can_be_zero(self):
        self.assertEqual(find_best_value([5, 5, 5], 1), 0)

    def test_single_element_capped(self):
        self.assertEqual(find_best_value([5], 3), 3)

    def test_single_element_uncapped(self):
        self.assertEqual(find_best_value([5], 10), 5)

    def test_every_element_capped(self):
        self.assertEqual(find_best_value([10, 10, 10], 5), 2)

    def test_cap_between_elements_exact(self):
        self.assertEqual(find_best_value([1, 10], 8), 7)

    def test_cap_equals_middle_element(self):
        self.assertEqual(find_best_value([1, 3, 5], 7), 3)

    def test_exact_hit_after_several_fixed(self):
        self.assertEqual(find_best_value([1, 2, 3, 4], 7), 2)

    def test_input_not_modified(self):
        arr = [4, 9, 3]
        find_best_value(arr, 10)
        self.assertEqual(arr, [4, 9, 3])

    def test_large_input_is_fast(self):
        import random, time
        rng = random.Random(0)
        arr = [rng.randint(1, 10**5) for _ in range(10**4)]
        start = time.perf_counter()
        find_best_value(arr, 10**5)
        self.assertLess(time.perf_counter() - start, 1.0)

    def test_matches_brute_force(self):
        import random
        rng = random.Random(42)

        def brute(arr, target):
            return min(range(max(arr) + 1),
                       key=lambda v: (abs(sum(min(x, v) for x in arr) - target), v))

        for _ in range(500):
            arr = [rng.randint(1, 30) for _ in range(rng.randint(1, 8))]
            target = rng.randint(1, 200)
            self.assertEqual(find_best_value(arr, target), brute(arr, target), (arr, target))

if __name__ == "__main__":
    unittest.main()
