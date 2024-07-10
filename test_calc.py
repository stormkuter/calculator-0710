from unittest import TestCase

from calc import Calc

class TestCalc(TestCase):
    def test_getGop(self):
        calc = Calc()
        self.assertEqual(calc.gop(3, 4), 12)
