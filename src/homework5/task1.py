"""
Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

from string import ascii_letters


def total_price(rubles=4, penny=50, number=8):
    """Домашняя работа № 2, задача № 1

    Напишите программу, которая считает общую цену.
    Вводится M рублей и N копеек
    цена, а также количество S товара.
    Посчитайте общую цену в рублях и копейках за L товаров.

    """
    summa = (rubles * 100 + penny) * number
    total_rubles = summa // 100
    total_penny = summa % 100
    print("Общая цена составит", str(total_rubles) + " рублей",
          str(total_penny) + " копеек.")


def longest_word(my_string="Hi, World! How are you?"):
    """ Домашняя работа № 2, задача № 2

    Найти самое длинное слово в введенном предложении.
    Учтите что в предложении есть знаки препинания.

    """
    for punctuation_mark in (".", ",", "?", "!", ":", ";", '"', "(", ")"):
        my_string = my_string.replace(punctuation_mark, "")
    my_list = my_string.split()
    largest_word = max(my_list, key=len)
    print("Самое длинное слово в предложении:", largest_word)


def clean_string(string="abc cde def"):
    """Домашняя работа № 2, задача № 3

    Вводится строка.
    Требуется удалить из нее повторяющиеся символы и все пробелы.
    Например, если было введено "abc cde def",
    то должно быть выведено "abcdef".

    """
    string_1 = []
    for i in string:
        if i not in string_1 and i != " ":
            string_1.append(i)
    print("".join(string_1))


def big_small_letters(my_str="Hello, World! Прривет, мир!"):
    """Домашняя работа № 2, задача № 4

    Посчитать количество строчных (маленьких)
    и прописных (больших) букв в введенной строке.
    Учитывать только английские буквы.

    """
    up = 0
    low = 0
    for i in my_str:
        if i in ascii_letters and i.isupper():
            up += 1
        elif i in ascii_letters and i.islower():
            low += 1
    print("В введённой строке", str(up) + " прописных (больших) и",
          str(low) + " строчных (маленьких) английских букв.")


def fib_num(n=4):
    """Домашняя работа № 2, задача № 5

    Выведите n-ое число Фибоначчи,
    используя только временные переменные,
    циклические операторы и условные операторы. n - вводится

    """
    if n < 2:
        print("Число Фибоначчи:", str(n - 1))
    else:
        i = 2
        f = [0, 1, 1]
        while i < n:
            f[2] = f[0] + f[1]
            f[0] = f[1]
            f[1] = f[2]
            i += 1
        print("Число Фибоначчи:", str(f[2]))


def palindrome(number=2442):
    """Домашняя работа № 2, задача № 6

    Определите, является ли число палиндромом
    (читается слева направо и справа налево одинаково).
    Число положительное целое, произвольной длины.
    Задача требует работать только с числами
    (без конвертации числа в строку или что-нибудь еще).

    """
    number_1 = number
    pal = 0
    while number > 0:
        digit = number % 10
        pal = pal * 10 + digit
        number = number // 10
    if number_1 == pal:
        print("Это палиндром!")
    else:
        print("Это не палиндром!")


def triangle(side_a=12, side_b=10, side_c=20):
    """Домашняя работа № 2, задача № 7
    Даны: три стороны треугольника.
    Требуется: проверить, действительно ли это стороны треугольника.
    Если стороны определяют треугольник, найти его площадь.
    Если нет, вывести сообщение о неверных данных.

    """
    if side_a + side_b > side_c and \
            side_a + side_c > side_b and side_b + side_c > side_a:
        P = (side_a + side_b + side_c) / 2
        S = (P * (P - side_a) * (P - side_b) * (P - side_c)) ** 0.5
        print("Площадь треугольника составит", str(S) + " кв. см")
    else:
        print("Данные неверны.")


def fizz_buzz():
    """Домашняя работа № 3, задача № 1

    Напишите программу, которая печатает цифры от 1 до 100,
    но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
    а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz.

    """
    for i in range(1, 101):
        if not i % 3 and not i % 5:
            print("FizzBuzz")
        elif not i % 3:
            print("Fizz")
        elif not i % 5:
            print("Buzz")
        else:
            print(i)


def list_comprehension():
    """Домашняя работа № 3, задача № 2

    Используйте генератор списков чтобы получить следующий:
    ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
    Используйте на предыдущий список slice чтобы получить следующий:
    ['ab', 'ad', 'bc'].
    Используйте генератор списков чтобы получить следующий:
    ['1a', '2a', '3a', '4a'].
    Одной строкой удалите элемент '2a' из прошлого списка и напечатайте его.
    Скопируйте список и добавьте в него элемент '2a' так,
    чтобы в исходном списке этого элемента не было.

    """
    list_1 = [i + j for i in "ab" for j in "bcd"]
    print(list_1)
    list_2 = list_1[::2]
    print(list_2)
    list_3 = [str(i) + j for i in range(1, 5) for j in "a"]
    print(list_3)
    print(list_3.pop(1))
    list_4 = list_3.copy()
    list_4.append("2a")
    print(list_3)
    print(list_4)


def tuples():
    """Домашняя работа № 3, задача № 3

    Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
    Создайте кортеж ('a', 'b', 'c'), и сделайте из него список
    Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
    Создайте кортеж из одного элемента, чтобы при итерировании по этому
    элементу последовательно выводились значения 1, 2, 3.
    Убедитесь что len() исходного кортежа возвращает 1.

    """
    list_1 = ["a", "b", "c"]
    tuple_1 = tuple(list_1)
    print(tuple_1)

    list_2 = list(tuple_1)
    print(list_2)

    a, b, c = "a", 2, "python"
    print(a, b, c)

    tuple_2 = ("123",)
    for i in tuple_2[0]:
        print(i)
    print("Длина кортежа:", len(tuple_2))


def pairs_of_numbers(string_num=(1, 1, 1, 2, 2)):
    """Домашняя работа № 3, задача № 4

    Дан список чисел.
    Посчитайте, сколько в нем пар элементов, равных друг другу.
    Считается, что любые два элемента, равные друг другу
    образуют одну пару, которую необходимо посчитать.
    Входные данные - строка из чисел, разделенная пробелами.
    Выходные данные - количество пар.
    Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар.

    """
    count = 0
    index = 0
    for num in string_num:
        for pair in string_num[index + 1:]:
            if num == pair:
                count += 1
                index += 1
    print("Количество пар чисел:", str(count))


def unique_elements(list_1=None):
    """Домашняя работа № 3, задача № 5

    Дан список. Выведите те его элементы,
    которые встречаются в списке только один раз.
    Элементы нужно выводить в том порядке, в котором они встречаются в списке.

    """
    if list_1 is None:
        list_1 = [0, 0, 0, 1, 2, 2, 4, 1, 0, 4, 5, 0, 3, 7]
    print(list_1)
    list_new = []
    for i in list_1:
        if list_1.count(i) == 1:
            list_new.append(i)
        else:
            continue
    print(list_new)


def ordered_list(list_num=None):
    """Домашняя работа № 3, задача № 6

    Дан список целых чисел.
    Требуется переместить все ненулевые элементы в левую часть списка,
    не меняя их порядок, а все нули - в правую часть.
    Порядок ненулевых элементов изменять нельзя,
    дополнительный список использовать нельзя,
    задачу нужно выполнить за один проход по списку.
    Распечатайте полученный список.

    """
    if list_num is None:
        list_num = [1, 0, 3, 0, 2, 0, 5, 0, 4, 0]
    for num in list_num:
        if num == 0:
            list_num.remove(num)
            list_num.append(num)
    print(list_num)


def dict_comprehension():
    """Домашняя работа № 4, задача № 1

    Создайте словарь с помощью генератора словарей,
    так чтобы его ключами были числа от 1 до 20, а значениями кубы этих чисел.

    """
    dict_new = {i: i ** 3 for i in range(1, 21)}
    print(dict_new, type(dict_new), sep="\n")


def country_and_cities(n_countries=3):
    """Домашняя работа № 4, задача № 2

    Дан список стран и городов каждой страны. Затем даны названия городов.
    Для каждого города укажите, в какой стране он находится.
    Входные данные:
    Программа получает на вход количество стран N.
    Далее идет N строк, каждая строка начинается с названия страны,
    затем идут названия городов этой страны.
    В следующей строке записано число M,
    далее идут M запросов — названия каких-то M городов, перечисленных выше.
    Для каждого из запроса выведите название страны,
    в котором находится данный город.

    """
    dict_country_and_cities = {}
    for i in range(n_countries):
        list_cities = []
        str_country_and_cities = (input("Введите сначала страну, "
                                        "а затем города,"
                                        " находящиеся в этой стране: "))
        list_country_and_cities = str_country_and_cities.split()
        for cities_of_thr_country in list_country_and_cities[1:]:
            list_cities.append(cities_of_thr_country)
            dict_country_and_cities[list_country_and_cities[0]] = list_cities
    cities = int(input("Введите кол-во запросов на поиск страны по городу: "))
    countries = ""
    for i in range(cities):
        city_search = input("Введите название города: ")
        for country, cities_of_the_country in dict_country_and_cities.items():
            if city_search in cities_of_the_country:
                countries += country + "\n"
    print(countries)


def two_lists_unique(list_num_1=None, list_num_2=None):
    """Домашняя работа № 4, задача № 3

    Даны два списка чисел.
    Посчитайте, сколько различных чисел содержится одновременно
    как в первом списке, так и во втором.

    """
    if list_num_1 is None:
        list_num_1 = [1, 2, 3, 4, 5]
    if list_num_2 is None:
        list_num_2 = [3, 4, 5, 6, 7]
    list_sum = list_num_1 + list_num_2
    total = set(list_sum)
    print(len(total))


def only_one_list_unique(list_num_1=None, list_num_2=None):
    """Домашняя работа № 4, задача № 4

    Даны два списка чисел.
    Посчитайте, сколько различных чисел входит только в один из этих списков.

    """
    if list_num_1 is None:
        list_num_1 = [num for num in range(1, 11, 2)]
    if list_num_2 is None:
        list_num_2 = [num for num in range(1, 11, 3)]
    print("Список чисел 1:", list_num_1)
    print("Список чисел 2:", list_num_2)
    set_1, set_2 = set(list_num_1), set(list_num_2)
    diff_num = set_1 ^ set_2
    print("Чисел входящих тольлко в один из списков:", len(diff_num))


def all_languages(**kwargs):
    """Домашняя работа № 4, задача № 5

    Каждый из N школьников некоторой школы знает Mi языков.
    Определите, какие языки знают все школьники
    и языки, которые знает хотя бы один из школьников.

    """
    if not kwargs:
        kwargs = {"first_student": ["English", "Russian", "Belarusian"],
                  "second_student": ["English", "Russian", "Belarusian",
                                     "German"],
                  "third_student": ["Polish", "Belarusian"]}
    list_languages_all = []
    for languages in kwargs.values():
        list_languages_all.append(set(languages))
    all_know = set.intersection(*list_languages_all)
    print("Кол-во языков, которые знают все школьники:", len(all_know))
    for lang_all in all_know:
        print(lang_all)
    anyone_know = set.union(*list_languages_all)
    print(
        "Кол-во языков, которые знает хотя бы один школьник:",
        len(anyone_know)
    )
    for lang_one in anyone_know:
        print(lang_one)


def unique_words(some_text="Привет!!!\nБудем, ребята, учиться писать код"
                           " на python?\tучиться (python)"
                           "  нравится всем всем всем  !"):
    """Домашняя работа № 4, задача №6

    Во входной строке записан текст.
    Словом считается последовательность непробельных символов идущих подряд,
    слова разделены одним или большим числом пробелов
    или символами конца строки.
    Определите, сколько различных слов содержится в этом тексте.

    """
    print(some_text)
    for punctuation_mark in (
            ".", ",", "?", "!", "!!!" ":", ";", '"', "(", ")"
    ):
        some_text = some_text.replace(punctuation_mark, "")
    list_words = some_text.split()
    set_unique_words = set(list_words)
    print("В тексте содержится", len(set_unique_words), "различных слов.")


def greatest_divisor(num_1=17, num_2=24):
    """Домашняя работа № 4, задача № 7

    Даны два натуральных числа.
    Вычислите их наибольший общий делитель
    при помощи алгоритма Евклида (мы не знаем функции и рекурсию).

    """
    a, b = num_1, num_2
    while num_1 != num_2:
        if num_1 > num_2:
            num_1 -= num_2
        else:
            num_2 -= num_1
    print(
        "Наибольший общий делитель чисел", a, "и", b,
        "равен " + str(num_1) + "."
    )


names_in_module = dir()
list_names_of_functions = []
for name in names_in_module:
    if name.startswith("__") and name.endswith("__"):
        continue
    elif name == "ascii_letters":
        continue
    else:
        list_names_of_functions.append(name)


def runner(*args):
    if not args:
        for func_name in list_names_of_functions:
            start = globals()[func_name]
            start()
    for func_name in args:
        start = globals()[func_name]
        start()


runner("all_languages")
