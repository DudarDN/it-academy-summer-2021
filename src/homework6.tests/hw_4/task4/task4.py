def only_one_list_unique(list_num_1=None, list_num_2=None):
    """Домашняя работа № 4, задача № 4

    Даны два списка чисел.
    Посчитайте, сколько различных чисел входит только в один из этих списков.

    """
    if list_num_1 is None:
        list_num_1 = [num for num in range(1, 11, 2)]
    if list_num_2 is None:
        list_num_2 = [num for num in range(1, 11, 3)]
    set_1, set_2 = set(list_num_1), set(list_num_2)
    diff_num = set_1 ^ set_2
    return len(diff_num)
