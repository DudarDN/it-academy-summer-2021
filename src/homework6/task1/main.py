from src.homework6.task1.UserInterface import UserInterface
from src.homework6.task1.CarRentalService import CarRentalService

"""Домашнее задание № 6, задача № 1.

Попытался реализовать модель сайта по аренде автомобилей.
Пользователь вводит параметры поиска: кол-во сидений и цену желаемого авто.
Программа находит машины, соответствующие условию поиска и предлагает на выбор
список машин. Клиент выбирает авто, после чего его уникальные данные,
и уникальные данные машины, заносятся в список резерваций. Теперь, пока клиент
не вернет машину, арендовать ее не получится. Далее клиет может вернуть машину 
введя свой уникальный номер телефона и машина снова доступна к заказу.
P.S. Понимаю, что модель можно улучшать и улучшать, добавить, к примеру,
подключение к базе данных, добавить базу данных для клиентов и т.д.
Но после лекций про flask и Django пребываю в легком шоке и очень хочу на
выходных выйти из этого состояния.)) 

"""

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
