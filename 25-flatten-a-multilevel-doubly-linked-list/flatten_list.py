import unittest


class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def build_level(values):
    """Build one level of a doubly linked list and return its nodes."""
    nodes = [Node(v) for v in values]
    for left, right in zip(nodes, nodes[1:]):
        left.next = right
        right.prev = left
    return nodes


def forward_values(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def flatten(head):
    """Flatten a multilevel doubly linked list in place."""
    node = head
    while node:
        if node.child:
            child = node.child
            tail = child
            while tail.next:
                tail = tail.next
            tail.next = node.next
            node.next = child
            child.prev = node
        node = node.next
    return head


class FlattenTests(unittest.TestCase):
    def test_three_levels(self):
        top = build_level([1, 2, 3, 4, 5, 6])
        middle = build_level([7, 8, 9, 10])
        bottom = build_level([11, 12])
        top[2].child = middle[0]
        middle[1].child = bottom[0]
        head = flatten(top[0])
        self.assertEqual(forward_values(head), [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6])

    def test_backward_walk_matches_forward_walk(self):
        top = build_level([1, 2, 3, 4, 5, 6])
        middle = build_level([7, 8, 9, 10])
        bottom = build_level([11, 12])
        top[2].child = middle[0]
        middle[1].child = bottom[0]
        head = flatten(top[0])
        tail = head
        while tail.next:
            tail = tail.next
        backward = []
        while tail:
            backward.append(tail.val)
            tail = tail.prev
        self.assertEqual(backward, list(reversed(forward_values(head))))

    def test_child_links_are_kept(self):
        top = build_level([1, 2])
        child = build_level([3])
        top[0].child = child[0]
        flatten(top[0])
        self.assertIs(top[0].child, child[0])

    def test_single_child(self):
        top = build_level([1, 2])
        child = build_level([3])
        top[0].child = child[0]
        self.assertEqual(forward_values(flatten(top[0])), [1, 3, 2])

    def test_no_children(self):
        top = build_level([1, 2, 3])
        self.assertEqual(forward_values(flatten(top[0])), [1, 2, 3])

    def test_head_has_no_prev(self):
        top = build_level([1, 2])
        self.assertIsNone(flatten(top[0]).prev)

    def test_empty(self):
        self.assertIsNone(flatten(None))


if __name__ == "__main__":
    unittest.main()
