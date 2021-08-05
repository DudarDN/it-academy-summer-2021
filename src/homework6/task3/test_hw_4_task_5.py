import hw_4_task_5
import unittest


class Test(unittest.TestCase):

    def test_positive_1(self):
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
        result = hw_4_task_5.all_languages(student_1=["Belarusian", "Russian",
                                                      "Polish", "English"],
                                           student_2=("German",),
                                           student_3="France")
        self.assertNotEqual(result[2], 6)
        with self.assertRaises(TypeError):
            hw_4_task_5.all_languages(student_1=23)


if __name__ == '__main__':
    unittest.main()
