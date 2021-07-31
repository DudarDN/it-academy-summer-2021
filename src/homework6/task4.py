from functools import lru_cache
"""Задача 463. Странные рекурсивные отношения.

Функция f определена для всех натуральных аргументов следующим образом:
f(1)=1
f(3)=3
f(2n)=f(n)
f(4n+1)=2f(2n+1)−f(n)
f(4n+3)=3f(2n+1)−2f(n)
Функция S(n) определена как ∑ni=1f(i).
S(8)=22 и S(100)=3604.
Найдите S(3**37).
В качестве ответа приведите последние 9 цифр полученного числа.

"""


@lru_cache(maxsize=None)
def func_f(num):
    result = 0
    if num == 1:
        return 1
    elif num == 3:
        return 3
    elif not num % 2:
        result = func_f(num / 2)
    elif not (num - 1) % 4:
        result = 2 * func_f((num - 1) / 2 + 1) - func_f((num - 1) / 4)
    elif not (num - 3) % 4:
        result = 3 * func_f((num - 3) / 2 + 1) - 2 * func_f((num - 3) / 4)
    return result


def func_s(number):
    count_summa = 0
    for num in range(1, number + 1):
        count_summa += func_f(num)
    return count_summa


print(func_s(100))
print(func_f.cache_info())
