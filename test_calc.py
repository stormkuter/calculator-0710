from unittest import TestCase
from calc import Calc


class TestCalc(TestCase):

    def test_calc_sum_sum(self):
        calc = Calc()
        for a, b, c, ans in [(1, 1, 1, 3),
                             (1, 2, 3, 6),
                             (2, 2, 2, 6)]:
            with self.subTest(f"{a}+{b}+{c}={ans}"):
                ret = calc.getSumSum(a, b, c)
                self.assertEqual(ret, ans)
