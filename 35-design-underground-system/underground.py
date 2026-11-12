import unittest


class UndergroundSystem:
    def __init__(self):
        self.active = {}
        self.totals = {}

    def check_in(self, id, station_name, t):
        self.active[id] = (station_name, t)

    def check_out(self, id, station_name, t):
        start_station, start_time = self.active[id]
        key = tuple(sorted((start_station, station_name)))
        total, count = self.totals.get(key, (0, 0))
        self.totals[key] = (total + t - start_time, count + 1)

    def get_average_time(self, start_station, end_station):
        key = tuple(sorted((start_station, end_station)))
        total, count = self.totals[key]
        return total // count


class UndergroundSystemTests(unittest.TestCase):
    def test_several_passengers(self):
        system = UndergroundSystem()
        system.check_in(45, "Leyton", 3)
        system.check_in(32, "Paradise", 8)
        system.check_in(27, "Leyton", 10)
        system.check_out(45, "Waterloo", 15)
        system.check_out(27, "Waterloo", 20)
        system.check_out(32, "Cambridge", 22)
        self.assertEqual(system.get_average_time("Paradise", "Cambridge"), 14.0)
        self.assertEqual(system.get_average_time("Leyton", "Waterloo"), 11.0)
        system.check_in(10, "Leyton", 24)
        system.check_out(10, "Waterloo", 38)
        self.assertEqual(system.get_average_time("Leyton", "Waterloo"), 12.0)

    def test_single_journey(self):
        system = UndergroundSystem()
        system.check_in(1, "A", 0)
        system.check_out(1, "B", 7)
        self.assertEqual(system.get_average_time("A", "B"), 7.0)

    def test_fractional_average(self):
        system = UndergroundSystem()
        for passenger, start, end in [(10, 3, 8), (5, 10, 16), (2, 21, 30)]:
            system.check_in(passenger, "Leyton", start)
            system.check_out(passenger, "Paradise", end)
        self.assertAlmostEqual(system.get_average_time("Leyton", "Paradise"), 20 / 3)

    def test_round_trip_average(self):
        system = UndergroundSystem()
        system.check_in(1, "A", 0)
        system.check_out(1, "B", 10)
        system.check_in(1, "B", 20)
        system.check_out(1, "A", 40)
        self.assertEqual(system.get_average_time("A", "B"), 15.0)


if __name__ == "__main__":
    unittest.main()
