from src.homework6.task1.UserInterface import UserInterface
from src.homework6.task1.CarRentalService import CarRentalService


car_service = CarRentalService()
count = 0
while count < 2:
    seats = UserInterface.ask_for_seats()
    budget = UserInterface.ask_for_budget()
    result_cars = car_service.search(seats, budget)
    chosen_car = UserInterface.let_user_chose_car(result_cars)
    customer = UserInterface.customer_info()
    booking_info = car_service.rent_car(chosen_car, customer)
    print(booking_info)
    seats = UserInterface.ask_for_seats()
    budget = UserInterface.ask_for_budget()
    result_cars = car_service.search(seats, budget)
    chosen_car = UserInterface.let_user_chose_car(result_cars)
    customer = UserInterface.customer_info()
    booking_info = car_service.rent_car(chosen_car, customer)
    print(booking_info)
    back_car = UserInterface.give_car_back()
    car_back_info = car_service.give_car_back(back_car)
    print(car_back_info)
    count += 1
