import ddt
from . import task1
import unittest


@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(
        (4, 5, 8, "Общая цена составит 32 рублей 40 копеек."),
        (2.8, 0, 1.5, "Общая цена составит 4.0 рублей 20.0 копеек."),
    )
    @ddt.unpack
    def test_positive_1(self, rubles, penny, number, expected):
        result = task1.total_price(rubles, penny, number)
        self.assertEqual(result, expected)

    def test_positive_2(self):
        result = task1.total_price(rubles=1, penny=20)
        self.assertEqual(result, "Общая цена составит 9 рублей 60 копеек.")
        result = task1.total_price(1, 20, 4)
        self.assertEqual(result, "Общая цена составит 4 рублей 80 копеек.")
        result = task1.total_price()
        self.assertEqual(result, "Общая цена составит 36 рублей 0 копеек.")

    @ddt.data(
        ("8 рублей", "10 копеек", "5 штук", TypeError),
        ("1", "50", "4", TypeError),

    )
    @ddt.unpack
    def test_negative_1(self, rubles, penny, number, expected):
        with self.assertRaises(expected):
            task1.total_price(rubles, penny, number)

    def test_negative_2(self):
        with self.assertRaises(TypeError):
            task1.total_price(8, 7, 7, 5)
        with self.assertRaises(TypeError):
            task1.total_price(8, 7, 7, number=5)


if __name__ == '__main__':
    unittest.main()
