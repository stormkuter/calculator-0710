from unittest import TestCase
from calc import Calc


class TestCalc(TestCase):

    def setUp(self):
        super().setUp()
        self.sut = Calc()

    def test_minus_a_larger_than_b(self):
        self.assertEqual(3, self.sut.getMinus(7, 4))

    def test_minus_a_equal_to_b(self):
        self.assertEqual(0, self.sut.getMinus(3, 3))

    def test_minusa_a_smaller_than_b(self):
        self.assertEqual(-5, self.sut.getMinus(5, 10))

