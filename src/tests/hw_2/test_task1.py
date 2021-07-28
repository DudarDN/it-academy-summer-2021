import task1
import unittest
import ddt


@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(
        (4, 5, 8, "Общая цена составит 32 рублей 40 копеек."),
        (2.8, 0, 1.5, "Общая цена составит 4.0 рублей 20.0 копеек."),
    )
    @ddt.unpack
    def test_positive(self, rubles, penny, number, expected):
        result = task1.total_price(rubles, penny, number)
        self.assertEqual(result, expected)

    @ddt.data(
        ("8 рублей", "10 копеек", "5 штук", TypeError),
        ("1", "50", "4", TypeError),

    )
    @ddt.unpack
    def test_2(self, rubles, penny, number, expected):
        with self.assertRaises(expected):
            task1.total_price(rubles, penny, number)


if __name__ == '__main__':
    unittest.main()
