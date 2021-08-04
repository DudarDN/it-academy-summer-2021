from src.homework6.task1.Car import Car
from src.homework6.task1.Customer import Customer


class UserInterface:
    @staticmethod
    def ask_for_seats():
        seats = int(input("Мы рады видет Вас на нашем сервисе по аренде "
                          "авто!\nВведите минимальное количество мест,"
                          " необходимое Вам в автомобиле учитывая "
                          "место водителя: "))

        return seats

    @staticmethod
    def ask_for_budget():
        budget = int(input("Введите максимальную сумму, которую Вы готовы"
                           " выплатить за сутки аренды (у.е.): "))

        return budget

    @staticmethod
    def let_user_chose_car(cars):
        print("Для Вас доступны следующие автомобили:")
        for i, car in enumerate(cars):
            print(f"{i + 1}. Model: {car.model}. Price: {car.price}")

        index_chosen_car = int(input("Введите порядковый номер автомобиля, "
                                     "который Вы хотели бы арендовать: "))

        return cars[index_chosen_car - 1]

    @staticmethod
    def customer_info():
        customer = Customer(input("Введите Ваше имя: "),
                            input("Введите Ваш возраст: "),
                            input("Введите Ваш e-mail: "),
                            input("Введите Ваш номер телефона: "))
        return customer

    @staticmethod
    def give_car_back():
        phone_number = input("Для возврата авто введите ваш номер телефона: ")
        return phone_number

