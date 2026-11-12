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


def is_valid_bst(root):
    """Return whether the tree rooted at root is a valid binary search tree."""
    if root is None:
        return True
    if root.left and root.left.val >= root.val:
        return False
    if root.right and root.right.val <= root.val:
        return False
    return is_valid_bst(root.left) and is_valid_bst(root.right)


class IsValidBSTTests(unittest.TestCase):
    def test_small_valid_tree(self):
        self.assertTrue(is_valid_bst(build_tree([2, 1, 3])))

    def test_right_child_too_small(self):
        self.assertFalse(is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6])))

    def test_grandchild_larger_than_root(self):
        self.assertFalse(is_valid_bst(build_tree([3, 1, 5, 0, 4])))

    def test_duplicate_child(self):
        self.assertFalse(is_valid_bst(build_tree([1, 1])))

    def test_empty_tree(self):
        self.assertTrue(is_valid_bst(None))

    def test_children_ordered_at_every_node(self):
        self.assertTrue(is_valid_bst(build_tree([5, 4, 6, None, None, 3, 7])))


if __name__ == "__main__":
    unittest.main()
