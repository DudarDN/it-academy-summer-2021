"""Даны два списка чисел.
Посчитайте, сколько различных чисел содержится одновременно
как в первом списке, так и во втором.

"""

str_num_1 = input("Введите числа через пробел: ")
str_num_2 = input("Введите числа через пробел: ")
list_1 = str_num_1.split()
list_2 = str_num_2.split()
list_sum = list_1 + list_2
total = set(list_sum)
print(len(total))
