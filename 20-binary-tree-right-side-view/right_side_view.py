import unittest
from collections import deque


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


def right_side_view(root):
    """Return the values visible from the right side, top to bottom."""
    view = []

    def visit(node, depth):
        if node is None:
            return
        if depth == len(view):
            view.append(node.val)
        if node.right:
            visit(node.right, depth + 1)
        else:
            visit(node.left, depth + 1)

    visit(root, 0)
    return view


class RightSideViewTests(unittest.TestCase):
    def test_mixed_tree(self):
        root = build_tree([1, 2, 3, None, 5, None, 4])
        self.assertEqual(right_side_view(root), [1, 3, 4])

    def test_right_chain(self):
        root = build_tree([1, None, 3])
        self.assertEqual(right_side_view(root), [1, 3])

    def test_leaf_hidden_behind_right_node(self):
        root = build_tree([1, 2, 3, None, 5])
        self.assertEqual(right_side_view(root), [1, 3, 5])

    def test_empty_tree(self):
        self.assertEqual(right_side_view(None), [])

    def test_deeper_left_subtree(self):
        root = build_tree([1, 2, 3, 4])
        self.assertEqual(right_side_view(root), [1, 3])


if __name__ == "__main__":
    unittest.main()
