__author__ = 'tanvirshahjada'
import unittest

from unnecessary_math import multiply1


class TestUM(unittest.TestCase):

    def setUp(self):
        pass
    def test_numbers_3_4(self):
        self.assertEqual(multiply1(4,3), 12)

    def test_strings_a_3(self):
        self.assertEqual(multiply1('a',4), 'aaaa')

if __name__ == '__main__':
    unittest.main()


