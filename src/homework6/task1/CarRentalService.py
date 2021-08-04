from src.homework6.task1.BookRepository import BookRepository
from src.homework6.task1.Booking import Booking
from src.homework6.task1.CarRepository import CarRepository
from src.homework6.task1.Customer import Customer
from src.homework6.task1.UserInterface import UserInterface


class CarRentalService:
    def __init__(self):
        self.car_repository = CarRepository()
        self.book_repository = BookRepository()

    def search(self, seats, price):
        cars = self.car_repository.find_by_seats_and_price(seats, price)
        return cars

    def rent_car(self, car, customer):
        new_booking = Booking(car.license_plate, customer.phone)
        self.book_repository.add_book(new_booking)
        self.car_repository.change_status(car.license_plate, "Reserved")
        return f"Поздравляем, {customer.name}! " \
               f"Вы забронировали автомобиль {car.model}," \
               f" регистрационный номер: {car.license_plate}."

    def give_car_back(self, phone):
        license_plate = self.book_repository.get_bookings(phone)
        self.book_repository.del_bookings(phone, license_plate)
        car = self.car_repository.change_status(license_plate, "Free")
        return f"Автомобиль {car.model}, регистрационный номер:" \
               f" {car.license_plate} успешно возвращен!." \
               f"Спасибо, что выбрали нашу компанию."

