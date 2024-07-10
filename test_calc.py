from unittest import TestCase

from calc import Calc


class TestCalc(TestCase):
    def test_zegop(self):
        calc = Calc()
        self.assertEqual(8, calc.zegop(2, 3))
        self.assertEqual(9, calc.zegop(3, 2))
