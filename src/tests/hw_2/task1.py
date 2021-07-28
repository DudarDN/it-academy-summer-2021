def total_price(rubles=4, penny=50, number=8):
    """Домашняя работа № 2, задача № 1

    Напишите программу, которая считает общую цену.
    Вводится M рублей и N копеек
    цена, а также количество S товара.
    Посчитайте общую цену в рублях и копейках за L товаров.

    """
    summa = (rubles * 100 + penny) * number
    total_rubles = summa // 100
    total_penny = summa % 100
    return f"Общая цена составит {total_rubles} рублей {total_penny} копеек."
