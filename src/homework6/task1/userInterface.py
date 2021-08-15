from src.homework6.task1 import car_rental_service
from src.homework6.task1.customer import Customer


class UserInterface:
    """Класс содержащий методы для взаимодействия с пользователем сервиса"""

    @staticmethod
    def do_something():
        more_cars = int(input("Здравствуйте! Мы рады видет Вас на нашем "
                              "сервисе по аренде автомобилей!\n"
                              "Для аренды авто введите 1.\n"
                              "Для возврата авто введите 2.\n"
                              "Для выхода из сервиса введите 0.\n"))

        return more_cars

    @staticmethod
    def ask_for_seats():
        seats = input("Введите минимальное количество мест, "
                      "необходимое Вам в автомобиле учитывая "
                      "место водителя: ")

        return seats

    @staticmethod
    def ask_for_budget():
        budget = input("Введите максимальную сумму, которую Вы готовы "
                       "выплатить за сутки аренды (у.е.): ")

        return budget

    @staticmethod
    def ask_for_model():
        model = input("Введите марку и модель автомобиля, которую Вы "
                      "желали бы взять в аренду: ")
        return model

    @staticmethod
    def let_user_chose_car(cars):
        if not cars:
            print("К сожалению, у нас нет автомобилей соответствующих Вашему "
                  "запросу.\nДо свидания!")
            return quit()
        else:
            print("Для Вас доступны следующие автомобили:")
            for i, car in enumerate(cars):
                print(f"{i + 1}. Model: {car.model}. Price: {car.price}")

            index_chosen_car = int(input("Введите порядковый номер автомобиля,"
                                         " который Вы хотели бы арендовать: "))

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
