"""Напишите программу, которая считает общую цену. Вводится M рублей и N копеек
цена, а также количество S товара.
Посчитайте общую цену в рублях и копейках за L товаров.

"""
from string import ascii_letters


def total_price():
    rubles = int(input("Введите цену товара (рублей): "))
    penny = int(input("Введите цену товара (копеек): "))
    number = int(input("Введите количество товара(шт.): "))
    summa = (rubles * 100 + penny) * number
    total_rubles = summa // 100
    total_penny = summa % 100
    print("Общая цена составит", str(total_rubles) + " рублей",
          str(total_penny) + " копеек.")


"""Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.

"""


def longest_word():
    my_string = input("Введите предложение: ")
    for punctuation_mark in (".", ",", "?", "!", ":", ";", '"', "(", ")"):
        my_string = my_string.replace(punctuation_mark, "")
    my_list = my_string.split()
    largest_word = max(my_list, key=len)
    print("Самое длинное слово в предложении:", largest_word)


"""Вводится строка.
Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".

"""


def clean_string():
    string = list(input("Введите строку: "))
    string_1 = []
    for i in string:
        if i not in string_1 and i != " ":
            string_1.append(i)
    print("".join(string_1))


"""Посчитать количество строчных (маленьких)
и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.

"""


def big_small_letters():
    my_str = list(input("Введите строку: "))
    up = 0
    low = 0
    for i in my_str:
        if i in ascii_letters and i.isupper():
            up += 1
        elif i in ascii_letters and i.islower():
            low += 1
    print("В введённой строке", str(up) + " прописных (больших) и",
          str(low) + " строчных (маленьких) английских букв.")


"""Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы.
n - вводится

"""


def fib_num():
    n = int(input("Введите номер в последовательности чисел Фибоначчи: "))
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


"""Определите, является ли число палиндромом
(читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще).

"""


def palindrome():
    number = int(input('Введите число: '))
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


"""Даны: три стороны треугольника.
Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных.

"""


def triangle():
    print("Введите значения трех сторон треугольника (см):")
    side_a = int(input())
    side_b = int(input())
    side_c = int(input())
    if side_a + side_b > side_c and \
            side_a + side_c > side_b and side_b + side_c > side_a:
        P = (side_a + side_b + side_c) / 2
        S = (P * (P - side_a) * (P - side_b) * (P - side_c)) ** 0.5
        print("Площадь треугольника составит", str(S) + " кв. см")
    else:
        print("Данные неверны.")


def runner(*args):
    if not args:
        for key in functions_dict:
            func = functions_dict[key]
            func()
    else:
        for key in args:
            func = functions_dict[key]
            func()


functions_dict = {
    "total_price": total_price, "longest_word": longest_word,
    "clean_string": clean_string, "big_small_letters": big_small_letters,
    "fib_num": fib_num, "palindrome": palindrome, "triangle": triangle,


}

runner()
