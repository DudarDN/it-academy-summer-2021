"""Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники
и языки, которые знает хотя бы один из школьников.

"""

n_students = int(input("Введите кол-во школьников: "))
list_languages_all = []
for i in range(1, n_students + 1):
    set_languages = set()
    n_languages = int(input(f"Сколько языков знает школьник № {i}? "))
    for j in range(n_languages):
        languages = input("Введите язык: ")
        set_languages.add(languages)
    list_languages_all.append(set_languages)
all_know = set.intersection(*list_languages_all)
print("Кол-во языков, которые знают все школьники:", len(all_know))
for lang_all in all_know:
    print(lang_all)
anyone_know = set.union(*list_languages_all)
print("Кол-во языков, которые знает хотя бы один школьник:", len(anyone_know))
for lang_one in anyone_know:
    print(lang_one)
