"""Реализовать свой словарь, который запоминает 10
создание новых пар "ключ-значение".
есть метод get_history который возвращет историю вставок."""


class MyDict(dict):
    def __init__(self, data=None):
        if data is None:
            self.data = {}
        else:
            self.data = data
        self.history = []
        self.count = 0

    def __setitem__(self, key, value):
        self.data[key] = value


