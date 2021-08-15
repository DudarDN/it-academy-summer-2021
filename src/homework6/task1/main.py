from src.homework6.task1.car_rental_service import CarRentalService
from src.homework6.task1.userInterface import UserInterface

"""Домашнее задание № 6, задача № 1.

Попытался реализовать модель сайта по аренде автомобилей.
Пользователь вводит параметры поиска: кол-во сидений и цену желаемого авто.
Программа находит машины, соответствующие условию поиска и предлагает на выбор
список машин. Клиент выбирает авто, после чего его уникальные данные,
и уникальные данные машины, заносятся в список резерваций. Теперь, пока клиент
не вернет машину, арендовать ее не получится. Далее клиет может вернуть машину
введя свой уникальный номер телефона и машина снова доступна к заказу.
"""

car_service = CarRentalService()
while True:
    user_action = UserInterface.do_something()
    if user_action == 1:
        seats = UserInterface.ask_for_seats()
        budget = UserInterface.ask_for_budget()
        model = UserInterface.ask_for_model()
        result_cars = car_service.search(seats, budget, model)
        chosen_car = UserInterface.let_user_chose_car(result_cars)
        customer = UserInterface.customer_info()
        booking_info = car_service.rent_car(chosen_car, customer)
        print(booking_info)
    elif user_action == 2:
        back_car = UserInterface.give_car_back()
        car_back_info = car_service.give_car_back(back_car)
        print(car_back_info)
    elif user_action != 1 and user_action != 2:
        print("Спасибо, что заглянули на наш сервис!\n"
              "Будем рады видеть Вас вновь!\n")
        break
