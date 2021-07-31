import task6
import unittest
import ddt


@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(
        (458, "Это не палиндром!"),
        (28882, "Это палиндром!"),
        (7, "Это палиндром!"),
        (24.42, "Это не палиндром!"),
    )
    @ddt.unpack
    def test_positive(self, number, expected):
        result = task6.palindrome(number)
        self.assertEqual(result, expected)

    @ddt.data(
        ("123321", TypeError),
        ({1, 2, 3, 3, 2, 1}, TypeError),
        ("abcddcba", TypeError),
        ([1], TypeError),
    )
    @ddt.unpack
    def test_negative(self, input_data, expected):
        with self.assertRaises(expected):
            task6.palindrome(input_data)


if __name__ == '__main__':
    unittest.main()
