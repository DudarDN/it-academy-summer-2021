"""
Написать программу которая находит ближайшую степень двойки
к введенному числу. 10(8), 20(16), 1(1), 13(16)
"""


def power_of_two(number):
    two_power_big = 2
    power = 1
    while two_power_big < number:
        power += 1
        two_power_big = 2 ** power
    two_power_small = 2 ** (power - 1)
    if two_power_big - number <= number - two_power_small:
        print("Ближайшее число, являющееся степенью двойки: ", two_power_big)
    else:
        print("Ближайшее число, являющееся степенью двойки: ", two_power_small)


power_of_two(8)
power_of_two(2)
power_of_two(1)
