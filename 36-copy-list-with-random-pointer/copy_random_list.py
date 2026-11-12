import unittest


class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def build_list(pairs):
    """Build a list from [value, random_index] pairs (random_index may be None)."""
    nodes = [Node(value) for value, _ in pairs]
    for i, (_, random_index) in enumerate(pairs):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        if random_index is not None:
            nodes[i].random = nodes[random_index]
    return nodes[0] if nodes else None


def copy_random_list(head):
    """Return a deep copy of a list whose nodes have next and random pointers."""
    if head is None:
        return None
    clones = {}
    node = head
    while node:
        clones[node] = Node(node.val)
        node = node.next
    node = head
    while node:
        clone = clones[node]
        clone.next = clones.get(node.next)
        clone.random = node.random
        node = node.next
    return clones[head]


PAIRS = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]


class CopyRandomListTests(unittest.TestCase):
    def test_values_are_copied(self):
        copy = copy_random_list(build_list(PAIRS))
        values = []
        while copy:
            values.append(copy.val)
            copy = copy.next
        self.assertEqual(values, [7, 13, 11, 10, 1])

    def test_random_values_match(self):
        original = build_list(PAIRS)
        copy = copy_random_list(original)
        while original:
            if original.random is None:
                self.assertIsNone(copy.random)
            else:
                self.assertEqual(copy.random.val, original.random.val)
            original, copy = original.next, copy.next

    def test_copy_does_not_point_into_original(self):
        original = build_list(PAIRS)
        originals = set()
        node = original
        while node:
            originals.add(id(node))
            node = node.next
        copy = copy_random_list(original)
        while copy:
            self.assertNotIn(id(copy.next), originals)
            self.assertNotIn(id(copy.random), originals)
            copy = copy.next

    def test_random_points_to_original_node(self):
        original = build_list(PAIRS)
        copy = copy_random_list(original)
        self.assertIs(copy.next.random, original)

    def test_head_is_a_new_node(self):
        original = build_list(PAIRS)
        self.assertIsNot(copy_random_list(original), original)

    def test_empty_list(self):
        self.assertIsNone(copy_random_list(None))


if __name__ == "__main__":
    unittest.main()
