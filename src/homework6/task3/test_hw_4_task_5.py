import hw_4_task_5
import unittest


class Test(unittest.TestCase):

    def test_positive_default_values(self):
        """Тестирование работы функции со значениями по умолчанию"""
        result = hw_4_task_5.all_languages()
        self.assertEqual(result[0], 1)
        self.assertCountEqual(result[1], ["Belarusian"])
        self.assertEqual(result[2], 5)
        self.assertCountEqual(result[3],
                              ["Belarusian", "Russian", "Polish", "English",
                               "German"])
        result = hw_4_task_5.all_languages(student_1=["Belarusian", "Russian",
                                                      "Polish", "English"])
        self.assertEqual(result[0], 4)
        self.assertCountEqual(result[1], ["Belarusian", "Russian",
                                          "Polish", "English"])
        self.assertEqual(result[2], 4)
        self.assertCountEqual(result[3], ["Belarusian", "Russian",
                                          "Polish", "English"])

    def test_positive_data_types(self):
        """Тестирование работы функции с различными типами данных"""
        result = hw_4_task_5.all_languages(student_1=["Belarusian", "Russian",
                                                      "Polish", "English"],
                                           student_2=("German",),
                                           student_3={"France"})
        self.assertEqual(result[0], 0)
        self.assertCountEqual(result[1], [])
        self.assertEqual(result[2], 6)
        self.assertCountEqual(result[3], ["Belarusian", "Russian", "Polish",
                                          "English", "German", "France"])

    def test_positive_empty_collections(self):
        result = hw_4_task_5.all_languages(student_1=[], student_2={},
                                           student3=())
        self.assertEqual(result, (0, [], 0, []))

    def test_negative_string(self):
        """Передача аргумента в виде строки приведет к неверному результату"""
        result = hw_4_task_5.all_languages(student_1=["Belarusian", "Russian",
                                                      "Polish", "English"],
                                           student_2=("German",),
                                           student_3="France")
        self.assertNotEqual(result[2], 6)

    def test_negative_other_data_types(self):
        """Передача неккорректных типов данных вернет ошибку"""
        with self.assertRaises(TypeError):
            hw_4_task_5.all_languages(student_1=23, student_2=23.34)
            hw_4_task_5.all_languages(student_1=[23],
                                      student_2=(23.34, 23),
                                      student_3={23.34, 23}
                                      )
            hw_4_task_5.all_languages(student_1={"student_1": ["Russian",
                                                               "English",
                                                               "Belarusian"]})

    def test_negative_positional_arguments(self):
        """Передача позиционных аргументов вернет ошибку"""
        with self.assertRaises(TypeError):
            hw_4_task_5.all_languages(["Belarusian", "Russian"],
                                      ["Polish", "English", "German"])
            hw_4_task_5.all_languages({"student_1": ["Russian", "English",
                                                     "Belarusian"]})


if __name__ == '__main__':
    unittest.main()
