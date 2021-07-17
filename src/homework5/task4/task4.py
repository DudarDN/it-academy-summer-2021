"""
В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия фильмов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""

import json

try:
    with open("ratings.list") as rating_list:
        top_250 = []
        is_read = False
        for line in rating_list:
            if line == "BOTTOM 10 MOVIES (1500+ VOTES)\n":
                break
            if line != "New  Distribution  Votes  Rank  Title\n" \
                    and not is_read:
                continue
            is_read = True
            split_list = line.split()
            top_250.append(split_list[2:])
        top_250 = top_250[1:-1]

    dict_rank = {}
    for rank in top_250:
        count = 0
        for films in top_250:
            if rank[0] in films:
                count += 1
        dict_rank[rank[0].lstrip()] = count

    with open("levels.txt", "w") as levels:
        json.dump(dict_rank, levels, indent="\n")

    top_250_titles_and_years = []
    for films in top_250:
        films = films[1::]
        top_250_titles_and_years.append(films)

    dict_years = {}
    for year in top_250:
        count = 0
        for films in top_250:
            if year[-1] in films:
                count += 1
        dict_years[year[-1].strip("()")] = count

    with open("years.txt", "w") as years:
        json.dump(dict_years, years, indent="\n")

    top_250_titles = []
    for title in top_250_titles_and_years:
        title = title[:-1]
        top_250_titles.append(" ".join(title))

    with open("top250_movies.txt", "w") as top:
        for title in top_250_titles:
            top.write(str(title) + "\n")
except FileNotFoundError:
    print("No such file")
