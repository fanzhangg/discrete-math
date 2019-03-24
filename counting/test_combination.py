from unittest import TestCase
from combination import combination


class TestCombination(TestCase):
    def test_combination(self):
        self.assertEqual(0, combination(6, 10))
        self.assertEqual(1716, combination(13, 7))

