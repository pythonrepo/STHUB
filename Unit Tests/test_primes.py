__author__ = 'tanvirshahjada'

import unittest

from Primes import is_prime


class PrimeTestCase(unittest.TestCase):
    """Tests for 'primes.py"""

    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))

    def test_is_six_prime(self):
        self.assertTrue(is_prime(6))

if __name__ == '__main__':
    unittest.main()

