from unittest import TestCase
from counting.permutation import permutation


class TestPermutation(TestCase):
    def test_permutation(self):
        self.assertEqual(6, permutation(3, 3))
        self.assertEqual(970200, permutation(100, 3))
        self.assertEqual(0, permutation(3, 5))
