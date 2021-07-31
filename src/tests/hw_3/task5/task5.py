def unique_elements(list_1=None):
    """Домашняя работа № 3, задача № 5

    Дан список. Выведите те его элементы,
    которые встречаются в списке только один раз.
    Элементы нужно выводить в том порядке, в котором они встречаются в списке.

    """
    if list_1 is None:
        list_1 = [0, 0, 0, 1, 2, 2, 4, 1, 0, 4, 5, 0, 3, 7]
    list_new = []
    for i in list_1:
        if list_1.count(i) == 1:
            list_new.append(i)
        else:
            continue
    return list_new

