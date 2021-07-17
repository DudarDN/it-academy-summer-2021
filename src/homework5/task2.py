"""
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы).
"""


def decorator(func_new):

    def wrapper(*args, **kwargs):
        results = func_new(*args, **kwargs)
        with open("results.txt", "a") as res:
            res.write(str(results) + "\n")
        return results

    return wrapper


@decorator
def func_addition(x, y):
    return x + y


print(func_addition("s", "f"))
print(func_addition(3, 5))
print(func_addition(5, 5))


@decorator
def func_multiplication(x, y):
    return x - y


print(func_multiplication(2, 3))
print(func_multiplication(3, 5))
print(func_multiplication(5, 5))
