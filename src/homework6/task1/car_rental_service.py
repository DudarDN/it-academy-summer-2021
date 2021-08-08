from src.homework6.task1.booking import Booking
from src.homework6.task1.booking_data import BookingData
from src.homework6.task1.car_data import CarRepository


class CarRentalService:
    def __init__(self):
        self.car_repository = CarRepository()
        self.booking_repository = BookingData()

    def search(self, seats, price):
        cars = self.car_repository.find_by_seats_and_price(seats, price)
        return cars

    def rent_car(self, car, customer):
        new_booking = Booking(car.license_plate, customer.phone)
        self.booking_repository.add_book(new_booking)
        self.car_repository.change_status(car.license_plate, "Reserved")
        return f"Поздравляем, {customer.name}! " \
               f"Вы забронировали автомобиль {car.model}," \
               f" регистрационный номер: {car.license_plate}. " \
               f"Приятной поездки!"

    def give_car_back(self, phone):
        license_plate = self.booking_repository.del_bookings(phone)
        car = self.car_repository.change_status(license_plate, "Free")
        return f"Автомобиль {car.model}, регистрационный номер:" \
               f" {car.license_plate} успешно возвращен!. " \
               f"Спасибо, что выбрали нашу компанию."
