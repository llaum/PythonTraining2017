import unittest

def digits(x):
    """ retourne la liste des chiffres composant x

    >>> digits(4586378)
    [4, 5, 8, 6, 3, 7, 8]
    """

    pass


def is_palindrome(x):
    """ l'entier  x est -il un palindrome ?

    >>> is_palindrome(-14)
    False
    >>> is_palindrome(1234)
    False
    >>> is_palindrome(2468642)
    True
    """
    pass


class Tests(unittest.TestCase):
    """ tests des fonctions digit et is_palindrome """

    def test_digits_0(self):
        self.assertListEqual([], digits(0))

     def test_palindrome01(self):
         self.assertTrue(is_palindrome(11211))

    def test_digits01(self):
        self.assertListEqual(digits(4586378), [4, 5, 8, 6, 3, 7, 8])

    def test_digits02(self):
        self.assertListEqual(digits(123), [1, 2, 3])

    def test_palindrome1(self):
        self.assertTrue(is_palindrome(111))

    def test_palindrome2(self):
        self.assertFalse(is_palindrome(110))

    def test_palindrome3(self):
        self.assertFalse(is_palindrome(121))

    def test_palindrome4(self):
        self.assertFalse(is_palindrome(1221))

    def test_palindrome5(self):
        self.assertTrue(is_palindrome(1221))


# la ligne suivante indique que les tests ne doivent
# pas être effectués  si l'on fait un import
if __name__ == '__main__':
     unittest.main()

