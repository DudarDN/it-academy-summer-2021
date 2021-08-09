import hw_4_task_5
import unittest


class Test(unittest.TestCase):

    def test_positive(self):
        """Проверка корректной работы функции с различными входными данными

        Тестирование способности функции работать со значениями по умалчанию,
        с аргументами - различными типами данных,
        с пустыми коллекциями.

        """
        result = hw_4_task_5.all_languages()
        self.assertEqual(result[0], 1)
        self.assertCountEqual(result[1], ["Belarusian"])
        self.assertEqual(result[2], 5)
        self.assertCountEqual(result[3],
                              ["Belarusian", "Russian", "Polish", "English",
                               "German"])
        result = hw_4_task_5.all_languages(student_1=["Belarusian", "Russian",
                                                      "Polish", "English"],
                                           student_2=("German",),
                                           student_3={"France"})
        self.assertEqual(result[0], 0)
        self.assertCountEqual(result[1], [])
        self.assertEqual(result[2], 6)
        self.assertCountEqual(result[3], ["Belarusian", "Russian", "Polish",
                                          "English", "German", "France"])
        result = hw_4_task_5.all_languages(student_1=["Belarusian", "Russian",
                                                      "Polish", "English"])
        self.assertEqual(result[0], 4)
        self.assertCountEqual(result[1], ["Belarusian", "Russian",
                                          "Polish", "English"])
        self.assertEqual(result[2], 4)
        self.assertCountEqual(result[3], ["Belarusian", "Russian",
                                          "Polish", "English"])
        result = hw_4_task_5.all_languages(student_1=[], student_2={},
                                           student3=())
        self.assertEqual(result, (0, [], 0, []))

    def test_negative(self):
        """Проверка некоректной работы функции с различными входными данными

        Передача аргумента в виде строки приведет к ошибочному результату.
        Передача чисел и славаря, коллекций с числами,
        а также использование позиционных аргументов вернет ошибку.

        """
        result = hw_4_task_5.all_languages(student_1=["Belarusian", "Russian",
                                                      "Polish", "English"],
                                           student_2=("German",),
                                           student_3="France")
        self.assertNotEqual(result[2], 6)
        with self.assertRaises(TypeError):
            hw_4_task_5.all_languages(student_1=23, student_2=23.34)
            hw_4_task_5.all_languages(student_1=[23],
                                      student_2=(23.34, 23),
                                      student_3={23.34, 23}
                                      )
            hw_4_task_5.all_languages(student_1={"student_1": ["Russian",
                                                               "English",
                                                               "Belarusian"]})
            hw_4_task_5.all_languages(["Belarusian", "Russian"],
                                      ["Polish", "English", "German"])
            hw_4_task_5.all_languages({"student_1": ["Russian", "English",
                                                     "Belarusian"]})


if __name__ == '__main__':
    unittest.main()
