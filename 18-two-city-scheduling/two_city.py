import unittest


def two_city_sched_cost(costs):
    """Return the minimum cost of sending half the people to each city."""
    n = len(costs) // 2
    costs.sort(key=lambda pair: pair[0])
    return sum(a for a, _ in costs[:n]) + sum(b for _, b in costs[n:])


class TwoCitySchedCostTests(unittest.TestCase):
    def test_four_people(self):
        costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
        self.assertEqual(two_city_sched_cost(costs), 110)

    def test_six_people(self):
        costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
        self.assertEqual(two_city_sched_cost(costs), 1859)

    def test_two_people(self):
        self.assertEqual(two_city_sched_cost([[10, 1], [20, 100]]), 110)

    def test_cost_is_positive(self):
        self.assertGreater(two_city_sched_cost([[1, 2], [3, 4]]), 0)


if __name__ == "__main__":
    unittest.main()
