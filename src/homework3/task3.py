# Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
# Создайте кортеж ('a', 'b', 'c'), и сделайте из него список
# Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
# Создайте кортеж из одного элемента, чтобы при итерировании по этому
# элементу последовательно выводились значения 1, 2, 3.
# Убедитесь что len() исходного кортежа возвращает 1.


list_1 = ["a", "b", "c"]
tuple_1 = tuple(list_1)

list_2 = list(tuple_1)

a, b, c = "a", 2, "python"

tuple_2 = ("123",)
for i in tuple_2[0]:
    print(i)
print("Длина кортежа:", len(tuple_2))
