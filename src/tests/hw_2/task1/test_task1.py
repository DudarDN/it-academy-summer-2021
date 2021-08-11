from . import task1
import ddt
import unittest


@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(
        (4, 5, 8, "Общая цена составит 32 рублей 40 копеек."),
        (2.8, 0, 1.5, "Общая цена составит 4.0 рублей 20.0 копеек."),
    )
    @ddt.unpack
    def test_positive_1(self, rubles, penny, number, expected):
        """Проверка корректной работы функции с различными типами данных"""
        result = task1.total_price(rubles, penny, number)
        self.assertEqual(result, expected)

    def test_positive_2(self):
        """Проверка корректной работы функции.

        Тестирование способности функции работать со значениями по умолчанию,
        с различными типами и количеством аргументов.

        """
        result = task1.total_price(rubles=1, penny=20)
        self.assertEqual(result, "Общая цена составит 9 рублей 60 копеек.")
        result = task1.total_price(1, 20, 4)
        self.assertEqual(result, "Общая цена составит 4 рублей 80 копеек.")
        result = task1.total_price()
        self.assertEqual(result, "Общая цена составит 36 рублей 0 копеек.")

    @ddt.data(
        ("8 рублей", "10 копеек", "5 штук", TypeError),
        ("1", "50", "4", TypeError),
        ([1], [20], [3], TypeError),
        ({2}, {40}, {5}, TypeError),
    )
    @ddt.unpack
    def test_negative_1(self, rubles, penny, number, expected):
        """Тест некоректной работы функции с различными типами данными"""
        with self.assertRaises(expected):
            task1.total_price(rubles, penny, number)

    def test_negative_2(self):
        """Проверка некорректной работы функции.

        При передаче бОльшего кол-ва аргументов, а также при передаче
        аргументов любого иного типа кроме int и float функция вернет ошибку.

       """
        with self.assertRaises(TypeError):
            task1.total_price(8, 7, 7, 5)
        with self.assertRaises(TypeError):
            task1.total_price(8, 7, 7, number=5)
        with self.assertRaises(TypeError):
            task1.total_price([1, 50, 4])


if __name__ == '__main__':
    unittest.main()
