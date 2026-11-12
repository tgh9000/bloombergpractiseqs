import unittest


def min_remove_to_make_valid(s):
    """Remove the fewest parentheses so that s becomes valid."""
    chars = list(s)
    open_count = 0
    for i, ch in enumerate(chars):
        if ch == "(":
            open_count += 1
        elif ch == ")":
            if open_count == 0:
                chars[i] = ""
            else:
                open_count -= 1

    i = 0
    while open_count > 0 and i < len(chars):
        if chars[i] == "(":
            chars[i] = ""
            open_count -= 1
        i += 1
    return "".join(chars)


def is_valid(s):
    depth = 0
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


class MinRemoveTests(unittest.TestCase):
    def test_unmatched_open_before_text(self):
        s = "(a)(b"
        result = min_remove_to_make_valid(s)
        self.assertTrue(is_valid(result))
        self.assertEqual(len(result), len(s) - 1)

    def test_trailing_open_paren(self):
        self.assertEqual(min_remove_to_make_valid("x(y)("), "xy)(")

    def test_extra_closing_at_end(self):
        self.assertEqual(min_remove_to_make_valid("lee(t(c)o)de)"), "lee(t(c)o)de")

    def test_extra_closing_in_middle(self):
        self.assertEqual(min_remove_to_make_valid("a)b(c)d"), "ab(c)d")

    def test_nothing_can_be_kept(self):
        self.assertEqual(min_remove_to_make_valid("))(("), "")

    def test_result_only_uses_input_characters(self):
        s = "(ab)c)"
        self.assertTrue(set(min_remove_to_make_valid(s)) <= set(s))


if __name__ == "__main__":
    unittest.main()
