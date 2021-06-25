# Даны два натуральных числа.
# Вычислите их наибольший общий делитель
# при помощи алгоритма Евклида (мы не знаем функции и рекурсию).

number_1, number_2 = int(input("Введите натуральное число: ")),\
                     int(input("Введите натуральное число: "))
a, b = number_1, number_2
while number_1 != number_2:
    if number_1 > number_2:
        number_1 -= number_2
    else:
        number_2 -= number_1
print('Наибольший общий делитель чисел', a, "и", b, "равен " + str(number_1) + ".")
