import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def from_list(values):
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def to_list(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values


def _reverse(node):
    previous = None
    while node:
        following = node.next
        node.next = previous
        previous = node
        node = following
    return previous


def add_two_numbers(l1, l2):
    """Add two numbers stored most-significant-digit first."""
    a, b = _reverse(l1), _reverse(l2)
    carry = 0
    head = None
    while a or b:
        total = carry + (a.val if a else 0) + (b.val if b else 0)
        carry = total // 10
        head = ListNode(total % 10, head)
        a = a.next if a else None
        b = b.next if b else None
    return head


class AddTwoNumbersIITests(unittest.TestCase):
    def test_different_lengths(self):
        result = add_two_numbers(from_list([7, 2, 4, 3]), from_list([5, 6, 4]))
        self.assertEqual(to_list(result), [7, 8, 0, 7])

    def test_same_length(self):
        result = add_two_numbers(from_list([2, 4, 3]), from_list([5, 6, 4]))
        self.assertEqual(to_list(result), [8, 0, 7])

    def test_zeros(self):
        self.assertEqual(to_list(add_two_numbers(from_list([0]), from_list([0]))), [0])

    def test_final_carry_adds_digit(self):
        self.assertEqual(to_list(add_two_numbers(from_list([5]), from_list([5]))), [1, 0])

    def test_carry_through_all_digits(self):
        result = add_two_numbers(from_list([9, 9]), from_list([1]))
        self.assertEqual(to_list(result), [0, 0])


if __name__ == "__main__":
    unittest.main()
