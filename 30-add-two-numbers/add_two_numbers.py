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


def add_two_numbers(l1, l2):
    """Add two numbers stored least-significant-digit first."""
    dummy = ListNode()
    tail = dummy
    carry = 0
    while l1 and l2:
        total = l1.val + l2.val + carry
        carry = total // 10
        tail.next = ListNode(total % 10)
        tail = tail.next
        l1, l2 = l1.next, l2.next
    tail.next = l1 or l2
    if carry:
        tail.next = ListNode(carry)
    return dummy.next


class AddTwoNumbersTests(unittest.TestCase):
    def test_same_length(self):
        result = add_two_numbers(from_list([2, 4, 3]), from_list([5, 6, 4]))
        self.assertEqual(to_list(result), [7, 0, 8])

    def test_zeros(self):
        self.assertEqual(to_list(add_two_numbers(from_list([0]), from_list([0]))), [0])

    def test_different_lengths(self):
        result = add_two_numbers(from_list([1]), from_list([1, 2, 3]))
        self.assertEqual(to_list(result), [2, 2, 3])

    def test_final_carry(self):
        self.assertEqual(to_list(add_two_numbers(from_list([5]), from_list([5]))), [0, 1])

    def test_carry_into_longer_list(self):
        self.assertEqual(to_list(add_two_numbers(from_list([9, 9]), from_list([1]))), [0, 1])

    def test_long_carry_chain(self):
        result = add_two_numbers(from_list([9, 9, 9, 9, 9, 9, 9]), from_list([9, 9, 9, 9]))
        self.assertEqual(to_list(result), [8, 9, 9, 9, 0, 0, 0, 1])


if __name__ == "__main__":
    unittest.main()
