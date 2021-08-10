class Booking:
    """Класс для представления брони услуги по аренде автомобиля

    Конструктор принимает номер телефона клиента
    и государственный номер автомобиля
    (уникальные параметры клиента и авто).

    """
    def __init__(self, car_id, customer_id):
        self.car_id = car_id
        self.customer_id = customer_id
