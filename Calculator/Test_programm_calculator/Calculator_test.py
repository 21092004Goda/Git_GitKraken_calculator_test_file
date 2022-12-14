from unittest import TestCase, main

def calculator(function):
    symbol = '+-/*'
    if not any(sign in function for sign in symbol):
        raise ValueError(f'Некорректно выражение, нет допустимых знаков ({symbol})')
    for sign in symbol:
        if sign in function:
            try:
                left, right = function.split(sign)
                left, right = int(left), int(right)
                return {
                    '+': lambda a, b: a + b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b,
                    '-': lambda a, b: a - b,
                }[sign](left, right)
            except (ValueError, TypeError):
                raise ValueError('Выражение должно содержать целые числа и один знак')
            except(ZeroDivisionError):
                raise ZeroDivisionError('На ноль не делят')


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)  # assertEqual()для проверки ожидаемого результата

    def test_minus(self):
        self.assertEqual(calculator('3-2'), 1)

    def test_multi(self):
        self.assertEqual(calculator('3*2'), 6.0)

    def test_divide(self):
        self.assertEqual(calculator('5/2'), 2.5)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as exclusion:   # assertRaises()для проверки того, что возникает конкретное исключение
            calculator('abdfwfdscewsdc')
        self.assertEqual('Некорректно выражение, нет допустимых знаков (+-/*)', exclusion.exception.args[0])
    def test_no_int(self):
        with self.assertRaises(ValueError) as exclusion:
            calculator('2.2 + 3.6')
        self.assertEqual('Выражение должно содержать целые числа и один знак', exclusion.exception.args[0])

    def test_no_int(self):
        with self.assertRaises(ValueError) as exclusion:
            calculator('a + b')
        self.assertEqual('Выражение должно содержать целые числа и один знак', exclusion.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as exclusion:
            calculator('2 + 2 + 2')
        self.assertEqual('Выражение должно содержать целые числа и один знак', exclusion.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as exclusion:
            calculator('2 + 3 * 32 / 5')
        self.assertEqual('Выражение должно содержать целые числа и один знак', exclusion.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ZeroDivisionError) as exclusion:
            calculator('2 / 0')
        self.assertEqual('На ноль не делят', exclusion.exception.args[0])
