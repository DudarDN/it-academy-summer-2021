import task6
import unittest
import ddt


@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(
        ("hello, hello,  my friends!!!", 3),
        ("Python 3 is a (better?) programming  .. language?", 7),
        ("1991 year, year when Belarus became independent", 6),
        ("", 0),
        ("! !!! (?) ", 0)
    )
    @ddt.unpack
    def test_positive_1(self, input_text, expected):
        result = task6.unique_words(input_text)
        self.assertEqual(result, expected)

    def test_positive_2(self):
        result = task6.unique_words()
        self.assertEqual(result, 10)

    @ddt.data(
        (["Hello #### ****"], AttributeError),
        (1991, AttributeError),
        ({"hello, hello,  my friends!!!"}, AttributeError),
    )
    @ddt.unpack
    def test_negative_1(self, input_text, expected):
        with self.assertRaises(expected):
            task6.unique_words(input_text)

    def test_negative_2(self):
        result = task6.unique_words("Hello #### ****")
        self.assertNotEqual(result, 1)
        result = task6.unique_words("&&& ///")
        self.assertNotEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
