from . import task4
import ddt
import unittest


@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(
        ([1, 2, 3, 4], [1, 3, 4, 5], 2),
        ([1, 2, 3, 4], (1, 3, 4, 5), 2),
        ([1, 2, 3, 4], {1, 3, 4, 5}, 2),
        ([1, 2, 3, 4], ["a", "b", "c", "d"], 8),
        ([1, 2, 3, 4], "1345", 8),
    )
    @ddt.unpack
    def test_positive_1(self, list1, list2, expected):
        """Проверка корректной работы функции с различными типами данных"""
        result = task4.only_one_list_unique(list1, list2)
        self.assertEqual(result, expected)

    def test_positive_2(self):
        """Проверка корректной работы функции.

        Тестирование способности функции работать со значениями по умолчанию,
        с различными типами и количеством аргументов.

        """
        result = task4.only_one_list_unique()
        self.assertEqual(result, 5)
        result = task4.only_one_list_unique([6, 6, 5])
        self.assertEqual(result, 6)
        result = task4.only_one_list_unique(list_num_2=[6, 6, 5])
        self.assertEqual(result, 5)

    @ddt.data(
        ([1, 2, 3, 4], 1345, TypeError),
        ([1, 2, 3, 4], [1, 3, [4], 5], TypeError)
    )
    @ddt.unpack
    def test_negative_1(self, list1, list2, expected):
        """Тест некоректной работы функции с различными типами данными"""
        with self.assertRaises(expected):
            task4.only_one_list_unique(list1, list2)

    def test_negative_2(self):
        """Проверка некорректной работы функции.

        При передаче бОльшего кол-ва аргументов, а также при передаче
        аргумента с некорректным именем функция вернет ошибку.

        """
        with self.assertRaises(TypeError):
            task4.only_one_list_unique(list=[1, 2, 3, 4])
        with self.assertRaises(TypeError):
            task4.only_one_list_unique([7, 8, 8], [2, 3, 3, 4], [1, 2, 3, 7])


if __name__ == '__main__':
    unittest.main()
