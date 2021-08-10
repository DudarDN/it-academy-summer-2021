class Car:
    """Класс для представления автомобиля

    Конструктор принимает гос. номер, модель, год выпуска, количество сидений
    автомобиля, а также стоимость аренды в сутки.

    """
    def __init__(self, license_plate, model, year, seats, price):
        self.license_plate = license_plate
        self.model = model
        self.year = year
        self.seats = seats
        self.price = price
        self.status = "Free"
