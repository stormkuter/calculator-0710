from unittest import TestCase

from calc import Calc


class TestCalc(TestCase):
    def setUp(self):
        super().setUp()
        self.sut = Calc()

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