# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Входные данные
# Программа получает на вход количество стран N.
# Далее идет N строк, каждая строка начинается с названия страны,
# затем идут названия городов этой страны.
# В следующей строке записано число M,
# далее идут M запросов — названия каких-то M городов, перечисленных выше.
# Для каждого из запроса выведите название страны,
# в котором находится данный город.

n_countries = int(input("Введите кол-во стран: "))
dict_country_and_cities = {}
for i in range(n_countries):
    str_country_and_cities = (input("Введите сначала страну, "
                                    "а затем города,"
                                    " находящиеся в этой стране: "))
    list_country_and_cities = str_country_and_cities.split()
    for city in list_country_and_cities[1:]:
        dict_country_and_cities[city] = list_country_and_cities[0]
cities = int(input("Введите кол-во запросов на поиск страны по городу: "))
countries = ""
for i in range(cities):
    city_search = input("Введите название города: ")
    countries += dict_country_and_cities[city_search] + "\n"
print(countries)
