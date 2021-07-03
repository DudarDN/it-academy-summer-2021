"""Даны два списка чисел.
Посчитайте, сколько различных чисел входит только в один из этих списков.

"""

list_1 = [num for num in range(1, 11, 2)]
print("Список чисел 1:", list_1)
list_2 = [num for num in range(1, 11, 3)]
print("Список чисел 2:", list_2)
set_1, set_2 = set(list_1), set(list_2)
diff_num = set_1 ^ set_2
print("Чисел входящих тольлко в один из списков:", len(diff_num))
