import unittest

import recursion


class TestRecursion(unittest.TestCase):
    def test_is_palindrome1(self):
        self.assertTrue(recursion.is_palindrome1('tenet'))

    def test_to_power(self):
        self.assertEqual(recursion.to_power(2, 4), 16)
        with self.assertRaises(ValueError):
            recursion.to_power(2, 0)

    def test_mult(self):
        with self.assertRaises(ValueError):
            recursion.mult(1, -1)
        self.assertEqual(recursion.mult(2, 5), 10)
        self.assertEqual(recursion.mult(1, 0), 0)

    def test_reverse(self):
        self.assertEqual(recursion.reverse('hello'), 'olleh')

    def test_sum_of_digits(self):
        self.assertEqual(recursion.sum_of_digits('36'), 9)


if __name__ == '__main__':
    unittest.main
