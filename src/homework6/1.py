@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(
        ([1, 2, 3], 2),
        ((1, 2, 3), 2),
        ({1, 2, 3}, 2),
    )
    @ddt.unpack
    def test_1(self, input_data, expected):
        result = main_1.avg(input_data)
        self.assertEqual(result, expected)

    @ddt.data(
        ('123', TypeError),
        (1, TypeError),
        ([], ZeroDivisionError),
        ([1, 2, '3'], TypeError),
    )
    @ddt.unpack
    def test_2(self, input_data, expected):
        with self.assertRaises(expected):
            main_1.avg(input_data)


if __name__ == '__main__':
    unittest.main()
