from src.homework6.task1.car import Car


class CarData:
    """Класс имитирующий работу с базой данных автомобилей"""
    def __init__(self):
        self.cars = {"1771 BO-7": Car("1771 BO-7", "Ford Edge", 2015, 5, 50),
                     "1772 BO-7": Car("1772 BO-7", "BMW X-3", 2013, 5, 45),
                     "1773 BO-7": Car("1773 BO-7", "Opel Zafira", 2020, 7, 60),
                     "1774 BO-7": Car("1774 BO-7", "Audi Q-5", 2019, 5, 55),
                     "1775 BO-7":
                         Car("1775 BO-7", "Mercedes Vito", 2021, 8, 150),
                     }

    def find_by_seats_and_price(self, seats, price):
        """Находит в 'базе данных' авто по параметрам введенным клиентом"""
        list_cars_for_a_rent = []
        for auto in self.cars.values():
            if seats <= auto.seats and price >= \
                    auto.price and auto.status == "Free":
                list_cars_for_a_rent.append(auto)

        return list_cars_for_a_rent

    def change_status(self, license_plate, status):
        """Изменяет статус автомобиля в 'базе данных'"""
        self.cars[license_plate].status = status
        return self.cars[license_plate]
