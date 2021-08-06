import ddt
import unittest
from . import task5


@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(
        (10, 8),
        (30, 32),
        (1, 1),
        (0, 1),
        (23.34, 16),
        (-20, 1),
    )
    @ddt.unpack
    def test_positive(self, input_data, expected):
        result = task5.power_of_two(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        ("5", TypeError),
        ([5], TypeError),
        ({5}, TypeError),
    )
    @ddt.unpack
    def test_negative_1(self, input_data, expected):
        with self.assertRaises(expected):
            task5.power_of_two(input_data)

    def test_negative_2(self):
        with self.assertRaises(TypeError):
            task5.power_of_two()


if __name__ == '__main__':
    unittest.main()
