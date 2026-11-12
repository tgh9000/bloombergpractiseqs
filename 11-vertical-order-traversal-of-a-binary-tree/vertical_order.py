import unittest
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Build a tree from a level-order list where None marks a missing child."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def vertical_traversal(root):
    """Return node values grouped by column from left to right."""
    positions = []

    def visit(node, row, col):
        if node is None:
            return
        positions.append((col, row, node.val))
        visit(node.left, row + 1, col - 1)
        visit(node.right, row + 1, col + 1)

    visit(root, 0, 0)
    columns = defaultdict(list)
    for col, row, val in sorted(positions, key=lambda item: item[0]):
        columns[col].append(val)
    return [columns[col] for col in sorted(columns)]


class VerticalTraversalTests(unittest.TestCase):
    def test_uneven_tree(self):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(vertical_traversal(root), [[9], [3, 15], [20], [7]])

    def test_complete_tree(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(vertical_traversal(root), [[4], [2], [1, 5, 6], [3], [7]])

    def test_same_position_keeps_left_subtree_first(self):
        root = build_tree([1, 2, 3, 4, 6, 5, 7])
        self.assertEqual(vertical_traversal(root), [[4], [2], [1, 6, 5], [3], [7]])

    def test_deep_left_node_in_right_column(self):
        root = build_tree([1, 2, 3, None, 5, None, None, None, 6])
        self.assertEqual(vertical_traversal(root), [[2], [1, 5], [3, 6]])

    def test_empty_tree(self):
        self.assertEqual(vertical_traversal(None), [])


if __name__ == "__main__":
    unittest.main()
