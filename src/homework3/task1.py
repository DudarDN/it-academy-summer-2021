# Напишите программу, которая печатает цифры от 1 до 100,
# но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
# а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz.


list_num = list(range(1, 101))
list_FizzBuzz = []
for i in list_num:
    if not i % 3 and not i % 5:
        i = "FizzBuzz"
        list_FizzBuzz.append(i)
    elif not i % 3:
        i = "Fizz"
        list_FizzBuzz.append(i)
    elif not i % 5:
        i = "Buzz"
        list_FizzBuzz.append(i)
    else:
        list_FizzBuzz.append(i)

print(list_FizzBuzz)
