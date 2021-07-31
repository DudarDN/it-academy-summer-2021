import hw_4_task_5
import unittest
import ddt


class Test(unittest.TestCase):

    def test_positive(self):
        result = hw_4_task_5.all_languages()
        self.assertEqual(result, (1, ['Belarusian'], 5, ['Belarusian', 'Russian', 'Polish', 'English', 'German']))


if __name__ == '__main__':
    unittest.main()
