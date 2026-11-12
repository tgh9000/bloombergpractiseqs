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


def level_order(root):
    """Return the tree's values grouped by level, left to right."""
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            if node is None:
                continue
            level.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        result.append(level)
    return result


class LevelOrderTests(unittest.TestCase):
    def test_root_is_first_level(self):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(level_order(root)[0], [3])

    def test_second_level(self):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(level_order(root)[1], [9, 20])

    def test_empty_tree_has_no_values(self):
        self.assertEqual(sum(len(level) for level in level_order(None)), 0)

    def test_empty_tree(self):
        self.assertEqual(level_order(None), [])

    def test_single_node(self):
        self.assertEqual(level_order(TreeNode(1)), [[1], []])


if __name__ == "__main__":
    unittest.main()
