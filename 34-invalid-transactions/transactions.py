import unittest


def invalid_transactions(transactions):
    """Return the transactions that are possibly invalid."""
    parsed = []
    for raw in transactions:
        name, time, amount, city = raw.split(",")
        parsed.append((name, int(time), int(amount), city, raw))

    invalid = []
    for i, (name, time, amount, city, raw) in enumerate(parsed):
        if amount >= 1000:
            invalid.append(raw)
            continue
        for j, (other_name, other_time, _, other_city, _) in enumerate(parsed):
            if (
                i != j
                and name == other_name
                and city != other_city
                and abs(time - other_time) < 60
            ):
                invalid.append(raw)
                break
    return invalid


class InvalidTransactionsTests(unittest.TestCase):
    def test_same_name_different_city(self):
        transactions = ["alice,20,800,mtv", "alice,50,100,beijing"]
        self.assertEqual(sorted(invalid_transactions(transactions)), sorted(transactions))

    def test_large_amount(self):
        transactions = ["alice,20,800,mtv", "alice,50,1200,mtv"]
        self.assertEqual(invalid_transactions(transactions), ["alice,50,1200,mtv"])

    def test_different_names(self):
        transactions = ["alice,20,800,mtv", "bob,50,1200,mtv"]
        self.assertEqual(invalid_transactions(transactions), ["bob,50,1200,mtv"])

    def test_exactly_sixty_minutes_apart(self):
        transactions = ["dave,0,10,nyc", "dave,60,10,sf"]
        self.assertEqual(sorted(invalid_transactions(transactions)), sorted(transactions))

    def test_amount_at_limit_is_invalid(self):
        self.assertEqual(invalid_transactions(["carol,10,1000,nyc"]), ["carol,10,1000,nyc"])


if __name__ == "__main__":
    unittest.main()
