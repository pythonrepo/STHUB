__author__ = 'tanvirshahjada'

import unittest

def is_prime(number):
    """Return True if *number* is prime."""
    for (element) in range(2,number):
        if number % element == 0:
            return False

    return True

def print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)

class PrimeTestCase(unittest.TestCase):
    """Tests for 'primes.py"""

    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))

    def test_is_six_prime(self):
        self.assertTrue(is_prime(6))

if __name__ == '__main__':
  #  unittest.main()
    unittest.main(testRunner=XMLTestRunner(output='test-reports'))


