import unittest


def decode_string(s):
    """Expand k[encoded] groups in s."""
    stack = []
    current = ""
    count = 0
    for ch in s:
        if ch.isdigit():
            count = int(ch)
        elif ch == "[":
            stack.append((current, count))
            current, count = "", 0
        elif ch == "]":
            previous, repeat = stack.pop()
            current = previous + current * repeat
        else:
            current += ch
    return current


class DecodeStringTests(unittest.TestCase):
    def test_adjacent_groups(self):
        self.assertEqual(decode_string("3[a]2[bc]"), "aaabcbc")

    def test_nested_groups(self):
        self.assertEqual(decode_string("3[a2[c]]"), "accaccacc")

    def test_trailing_letters(self):
        self.assertEqual(decode_string("2[abc]3[cd]ef"), "abcabccdcdcdef")

    def test_plain_text(self):
        self.assertEqual(decode_string("abc"), "abc")

    def test_two_digit_count(self):
        self.assertEqual(decode_string("12[x]"), "xx")

    def test_large_repeat_count(self):
        self.assertEqual(decode_string("10[a]"), "a" * 10)


if __name__ == "__main__":
    unittest.main()
