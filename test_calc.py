from unittest import TestCase

from calc import Calc


class TestCalc(TestCase):
    def test_sum(self):
        sut = Calc()
        self.assertEqual(5, sut.getSum(2, 3))
