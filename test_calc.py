from unittest import TestCase
from calc import Calc

class TestCalc(TestCase):
  
    def test_getGop(self):
        calc = Calc()
        self.assertEqual(calc.gop(3, 4), 12)
        
    def test_getZegop(self):
        calc = Calc()
        self.assertEqual(8, calc.zegop(2, 3))
        self.assertEqual(9, calc.zegop(3, 2))

    def setUp(self):
        super().setUp()
        self.sut = Calc()

    def test_minus_a_larger_than_b(self):
        self.assertEqual(3, self.sut.getMinus(7, 4))

    def test_minus_a_equal_to_b(self):
        self.assertEqual(0, self.sut.getMinus(3, 3))

    def test_minusa_a_smaller_than_b(self):
        self.assertEqual(-5, self.sut.getMinus(5, 10))

    def test_getDivide_should_raise_exception_when_second_arg_is_zero(self):
        a = 1
        b = 0

        with self.assertRaises(ValueError) as ve:
            self.sut.getDivide(a, b)
        self.assertEqual("Divider must not be zero", str(ve.exception))

    def test_getDivide_should_return_correct_value(self):
        a = 4
        b = 2
        expected_result = 2
        self.assertEqual(expected_result, self.sut.getDivide(a, b))

        a = -4
        b = 2
        expected_result = -2
        self.assertEqual(expected_result, self.sut.getDivide(a, b))

    def test_sum(self):
        sut = Calc()
        self.assertEqual(5, sut.getSum(2, 3))
        
    def test_calc_sum_sum(self):
        calc = Calc()
        for a, b, c, ans in [(1, 1, 1, 3),
                             (1, 2, 3, 6),
                             (2, 2, 2, 6)]:
            with self.subTest(f"{a}+{b}+{c}={ans}"):
                ret = calc.getSumSum(a, b, c)
                self.assertEqual(ret, ans)
