import task4
import unittest
import ddt


@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(
        ("1 1 1", "Количество пар чисел: 3"),
        ("1 1 1 2 2", "Количество пар чисел: 4"),
        ("111", "Количество пар чисел: 0"),
        ("1 1 1 d d ! !", "Количество пар чисел: 5"),
        ("", "Количество пар чисел: 0")
    )
    @ddt.unpack
    def test_positive(self, number, expected):
        result = task4.pairs_of_numbers(number)
        self.assertEqual(result, expected)

    @ddt.data(
        (["1 2 3 3 2 1"], AttributeError),
        ((1, 1, 1), AttributeError),
        ({1, 1, 1}, AttributeError),
        (111, AttributeError),
    )
    @ddt.unpack
    def test_negative(self, input_data, expected):
        with self.assertRaises(expected):
            task4.pairs_of_numbers(input_data)


if __name__ == '__main__':
    unittest.main()
