import unittest


def remove_duplicates(s, k):
    """Repeatedly remove runs of k equal adjacent letters."""
    stack = []
    for ch in s:
        if stack and stack[-1][0] == ch:
            stack[-1][1] = (stack[-1][1] + 1) % k
        else:
            stack.append([ch, 1])
    return "".join(ch * count for ch, count in stack)


class RemoveDuplicatesTests(unittest.TestCase):
    def test_nothing_to_remove(self):
        self.assertEqual(remove_duplicates("abcd", 2), "abcd")

    def test_everything_removed(self):
        self.assertEqual(remove_duplicates("aaa", 3), "")

    def test_letters_on_both_sides(self):
        self.assertEqual(remove_duplicates("abbbaa", 3), "aaa")

    def test_cascading_removals(self):
        self.assertEqual(remove_duplicates("deeedbbcccbdaa", 3), "aa")

    def test_result_is_not_longer(self):
        s = "pbbcggttciiippooaais"
        self.assertLessEqual(len(remove_duplicates(s, 2)), len(s))


if __name__ == "__main__":
    unittest.main()
