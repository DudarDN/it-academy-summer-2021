import ddt
from . import task3
import unittest


@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(
        ([0, 1, 2, 3, 4, 7, 8, 10], "0-4, 7-8, 10"),
        ((4, 7, 10), "4, 7, 10"),
        ("2389", "2-3, 8-9"),
        (["0", "1", "2", "3", "4", "7", "8", "10"], "0-4, 7-8, 10"),
        (["0", "1", 2, "3", 4, "7", "8", 10], "0-4, 7-8, 10")
    )
    @ddt.unpack
    def test_positive_1(self, input_data, expected):
        result = task3.get_ranges(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        ({0, 1, 2, 3, 4, 7, 8, 10}, TypeError),
        ("2,3,8,9", ValueError),
        (12457810, TypeError),
        ([], IndexError)
    )
    @ddt.unpack
    def test_negative_1(self, input_data, expected):
        with self.assertRaises(expected):
            task3.get_ranges(input_data)

    def test_negative_2(self):
        with self.assertRaises(TypeError):
            task3.get_ranges()


if __name__ == '__main__':
    unittest.main()
