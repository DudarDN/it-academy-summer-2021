# Дан список. Выведите те его элементы,
# которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

list_1 = list(input())
print(list_1)
list_new = []
for i in list_1:
    if i not in list_new:
        list_new += i
print(list_new)
