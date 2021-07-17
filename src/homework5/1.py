"""Реализовать класс Counter, у которого имеется два метода:
1. увелчиение счетчика (increment)
2. получение текущего значения (get)
start - начальное значение
stop - конечное значение, до которого считаем. Если достигнуто крайнее значение,
то вывести сообщение "Достигнуто максимальное знаечние" при вызове increment.

 """


class Counter:
    def __init__(self, start=0, stop=None, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.number = start

    def increment(self):
        if self.number < self.stop:
            self.number += self.step
        else:
            print("Достигнуто максимальное значение")

    def get(self):
        return self.number

    def __str__(self):
        return "Текущее значение счетчика: {}".format(self.number)


counter = Counter(4, 6)
counter.increment()
print(counter)
