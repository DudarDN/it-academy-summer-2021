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
        ("", "Количество пар чисел: 0"),
    )
    @ddt.unpack
    def test_positive_1(self, number, expected):
        result = task4.pairs_of_numbers(number)
        self.assertEqual(result, expected)

    def test_positive_2(self):
        result = task4.pairs_of_numbers()
        self.assertEqual(result, "Количество пар чисел: 4")

    @ddt.data(
        (["1 2 3 3 2 1"], AttributeError),
        ((1, 1, 1), AttributeError),
        ({1, 1, 1}, AttributeError),
        (111, AttributeError),
    )
    @ddt.unpack
    def test_negative_1(self, input_data, expected):
        with self.assertRaises(expected):
            task4.pairs_of_numbers(input_data)

    def test_negative_2(self):
        with self.assertRaises(TypeError):
            task4.pairs_of_numbers(num="1, 2, 1, 2, 3, 4")
        with self.assertRaises(TypeError):
            task4.pairs_of_numbers("7 8 8", "2 3 3 4")


if __name__ == '__main__':
    unittest.main()
