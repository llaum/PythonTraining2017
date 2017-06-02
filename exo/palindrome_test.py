import unittest
from palindrome import digits, is_palindrome


class Tests(unittest.TestCase):

    def test_digits_1(self):
        self.assertListEqual([1, 4, 1], digits(141))

    def test_digits_2(self):
        self.assertListEqual([1, 2, 3, 4, 4, 4], digits(444321))

    def test_is_palindrome_negative(self):
        """ should retrun false """
        self.assertFalse(is_palindrome(1234))
        self.assertFalse(is_palindrome(-1234))

    def test_is_palindrome_positive(self):
        """ should retrun true """
        self.assertTrue(is_palindrome(0))
        self.assertTrue(is_palindrome(1))
        self.assertTrue(is_palindrome(2))
        self.assertTrue(is_palindrome(33))
        self.assertTrue(is_palindrome(1234321))


unittest.main()
