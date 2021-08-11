from . import task6
import ddt
import unittest


@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(
        (458, "Это не палиндром!"),
        (28882, "Это палиндром!"),
        (7, "Это палиндром!"),
        (24.42, "Это не палиндром!"),
    )
    @ddt.unpack
    def test_positive_1(self, number, expected):
        """Проверка корректной работы функции с различными типами данных"""
        result = task6.palindrome(number)
        self.assertEqual(result, expected)

    def test_positive_2(self):
        """Тест корректной работы функции со значением по умолчанию"""
        result = task6.palindrome()
        self.assertEqual(result, "Это палиндром!")

    @ddt.data(
        ("123321", TypeError),
        ({1, 2, 3, 3, 2, 1}, TypeError),
        ("abcddcba", TypeError),
        ([1], TypeError),
    )
    @ddt.unpack
    def test_negative(self, input_data, expected):
        """Тест некоректной работы функции с различными типами данными"""
        with self.assertRaises(expected):
            task6.palindrome(input_data)

    def test_negative_2(self):
        """Проверка некорректной работы функции.

        При передаче бОльшего кол-ва аргументов, а также при передаче
        именованных аргументов функция вернет ошибку.

       """
        with self.assertRaises(TypeError):
            task6.palindrome(num=1221)
        with self.assertRaises(TypeError):
            task6.palindrome(12221, 75)


if __name__ == '__main__':
    unittest.main()
