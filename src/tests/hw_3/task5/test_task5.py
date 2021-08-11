from . import task5
import ddt
import unittest


@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(
        (None, [5, 3, 7]),
        ([1, 2, 3, 4, 5, 6, 1, 2, 3], [4, 5, 6]),
        ((1, 2, 3, 4, 5, 6, 1, 2, 3), [4, 5, 6]),
        ("123456123", ['4', '5', '6']),
        ([], []),
        ([1, "2", 3, "4", (5, 6), 1, 2, 3, "4", 5], ["2", (5, 6), 2, 5]),
    )
    @ddt.unpack
    def test_positive_1(self, input_data, expected):
        """Проверка корректной работы функции с различными типами данных"""
        result = task5.unique_elements(input_data)
        self.assertEqual(result, expected)

    def test_positive_2(self):
        """Тест корректной работы функции со значением по умолчанию"""
        result = task5.unique_elements()
        self.assertEqual(result, [5, 3, 7])

    @ddt.data(
        (123456123, TypeError),
        ({1: 2, 3: 4, 5: 6}, AttributeError),
        ({1, 2, 3, 4, 1, 2}, AttributeError),
    )
    @ddt.unpack
    def test_negative_1(self, input_data, expected):
        """Тест некоректной работы функции с различными типами данными"""
        with self.assertRaises(expected):
            task5.unique_elements(input_data)

    def test_negative_2(self):
        """Проверка некорректной работы функции.

        При передаче бОльшего кол-ва аргументов, а также при передаче
        именованных аргументов функция вернет ошибку.

       """
        with self.assertRaises(TypeError):
            task5.unique_elements(list=[1, 2, 3, 4])
        with self.assertRaises(TypeError):
            task5.unique_elements([7, 8, 8], [2, 3, 3, 4])


if __name__ == '__main__':
    unittest.main()
