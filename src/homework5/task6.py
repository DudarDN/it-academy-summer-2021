"""Вводится число, найти его максимальный делитель,
 являющийся степенью двойки. 10(2) 16(16), 12(4).

"""

number = int(input("Введите число: "))
divisor = int()
power = 0
while (2 ** power) <= number:
    if number % (2 ** power) == 0:
        divisor = (2 ** power)
        power += 1
    else:
        break
print("Максимальный делитель, являющийся степенью двойки: ", divisor)