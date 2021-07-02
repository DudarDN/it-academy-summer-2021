def new():
    print("Hello!")


def factorial(n):
    new()
    if n != 1:
        return n * factorial(n - 1)
    else:  # условия выхода из рекурсии
        return 1


print(factorial(4))



