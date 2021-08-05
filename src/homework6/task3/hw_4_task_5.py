def all_languages(**kwargs):
    """Домашняя работа № 4, задача № 5

    Каждый из N школьников некоторой школы знает Mi языков.
    Определите, какие языки знают все школьники
    и языки, которые знает хотя бы один из школьников.

    """
    if not kwargs:
        kwargs = {"first_student": ["English", "Russian", "Belarusian"],
                  "second_student": ["English", "Russian", "Belarusian",
                                     "German"],
                  "third_student": ["Polish", "Belarusian"]}
    list_languages_all = []
    for languages in kwargs.values():
        list_languages_all.append(set(languages))
    all_know = set.intersection(*list_languages_all)
    lang_all = []
    for lang in all_know:
        lang_all.append(lang)
    anyone_know = set.union(*list_languages_all)
    lang_one = []
    for lang in anyone_know:
        lang_one.append(lang)
    return len(all_know), lang_all, len(anyone_know), lang_one
