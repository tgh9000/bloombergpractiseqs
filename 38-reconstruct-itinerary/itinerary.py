import unittest
from collections import defaultdict


def find_itinerary(tickets):
    """Return the lexically smallest itinerary from JFK that uses every ticket."""
    graph = defaultdict(list)
    for source, destination in tickets:
        graph[source].append(destination)
    for source in graph:
        graph[source].sort()

    route = ["JFK"]
    current = "JFK"
    while graph[current]:
        current = graph[current].pop(0)
        route.append(current)
    return route


class FindItineraryTests(unittest.TestCase):
    def test_single_path(self):
        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        self.assertEqual(find_itinerary(tickets), ["JFK", "MUC", "LHR", "SFO", "SJC"])

    def test_choose_smallest_airport(self):
        tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
        self.assertEqual(find_itinerary(tickets), ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"])

    def test_prefers_smallest_destination(self):
        tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
        self.assertEqual(find_itinerary(tickets), ["JFK", "KUL"])

    def test_smallest_airport_is_a_dead_end(self):
        tickets = [["JFK", "AAA"], ["JFK", "BBB"], ["BBB", "JFK"]]
        self.assertEqual(find_itinerary(tickets), ["JFK", "BBB", "JFK", "AAA"])

    def test_starts_at_jfk(self):
        self.assertEqual(find_itinerary([["JFK", "AAA"]])[0], "JFK")

    def test_uses_every_ticket(self):
        tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
        self.assertEqual(len(find_itinerary(tickets)), len(tickets) + 1)


if __name__ == "__main__":
    unittest.main()
