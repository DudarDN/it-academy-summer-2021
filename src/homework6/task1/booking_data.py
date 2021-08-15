class BookingData:
    """Класс имитирующий работу с базой данных заказов"""

    def __init__(self):
        self.bookings = {}

    def add_booking(self, new_booking):
        """Добавляет в 'базу данных' бронь"""
        self.bookings[new_booking.customer_id] = new_booking.car_id

    def get_booking(self, phone_number):
        """Находит в 'базе данных' машину по номеру телефона клиента"""
        return self.bookings.get(phone_number)

    def del_bookings(self, phone):
        """Удаляет из 'базы данных' бронь"""
        return self.bookings.pop(phone, None)
