import task4
import unittest
import ddt


@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(
        (8, 22),
        (100, 3604),
        (0, 0),
        (-60, 0),
    )
    @ddt.unpack
    def test_positive(self, input_data, expected):
        result = task4.func_s(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        (23.34, TypeError),
        ("8", TypeError),
        ([100], TypeError),
    )
    @ddt.unpack
    def test_negative(self, input_data, expected):
        with self.assertRaises(expected):
            task4.func_s(input_data)


if __name__ == '__main__':
    unittest.main()
