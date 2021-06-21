# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу
# образуют одну пару, которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар.

string_num = input("Введите числа, разделенные пробелами: ")
list_num = string_num.split()
count = 0
for num in range(len(list_num)):
    for pair in range(int(num) + 1, len(list_num)):
        if list_num[num] == list_num[pair]:
            count += 1
print("Количество пар чисел:", str(count))
