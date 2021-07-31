def get_ranges(list_num):
    """Домашнее задание №5, задача № 3

    Реализовать функцию get_ranges которая получает на вход
    непустой список неповторяющихся целых чисел,
    отсортированных по возрастанию, которая этот список “сворачивает”
    get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4, 7-8, 10"
    get_ranges([4, 7, 10]) // "4, 7, 10"
    get_ranges([2, 3, 8, 9]) // "2-3, 8-9

    """
    list_final = []
    list_new = [list_num[0]]
    for i in list_num[1::]:
        if int(i) - int(list_new[-1]) == 1:
            list_new.append(i)
        else:
            if list_new[0] == list_new[-1]:
                list_final.append((str(list_new[0]) + ","))
            else:
                list_final.append(str(list_new[0]) + "-" +
                                  str(list_new[-1]) + ",")
            list_new.clear()
            list_new.append(i)
    if list_new[0] == list_new[-1]:
        list_final.append(str(list_new[0]))
    else:
        list_final.append(str(list_new[0]) + "-" + str(list_new[-1]))
    str_final = " ".join(list_final)
    return str_final
