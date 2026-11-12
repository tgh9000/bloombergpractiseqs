import unittest

def is_valid_access_code(code):
    """Return whether code is a valid six digit student access code."""
    try:
        if isinstance(code, str) is False:
            return False
        if len(code) != 6:
            return False
        for digit in code:
            if not is_ascii_digit(digit):
                return False
        return True
    except (TypeError, ValueError):
        return False


class ValidatorTests(unittest.TestCase):
    def test_six_digit_code_is_valid(self):
        self.assertTrue(is_valid_access_code("123456"))
    def test_integer_is_invalid(self):
        self.assertFalse(is_valid_access_code(123456))
    def test_space_is_invalid(self):
        self.assertFalse(is_valid_access_code(" 123456"))
    def test_plus_sign_is_invalid(self):
        self.assertFalse(is_valid_access_code("+23456"))
    def test_seven_digits_is_invalid(self):
        self.assertFalse(is_valid_access_code("1234567"))    
        

    def test_leading_zero_code_is_valid(self):
        self.assertTrue(is_valid_access_code("001234"))

    def test_non_digit_code_is_invalid(self):
        self.assertFalse(is_valid_access_code("12a456"))

    def test_non_ascii_digits_are_invalid(self):
        self.assertFalse(is_valid_access_code("１２３４５６"))

    def test_unrelated_arithmetic(self):
        self.assertEqual(2 + 2, 4)

def is_ascii_digit(digit):
    try:
        return digit.isdigit() and ord(digit) < 128
    except (TypeError, ValueError):
        return False

if __name__ == "__main__":
    unittest.main()