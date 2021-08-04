from src.homework6.task1.Car import Car


class CarRepository:
    def __init__(self):
        self.cars = [Car("1771 BO-7", "Ford Edge", 2015, 5, 50),
                     Car("1772 BO-7", "BMW X-3", 2013, 5, 45),
                     Car("1773 BO-7", "Opel Zafira", 2020, 7, 60),
                     Car("1774 BO-7", "Audi Q-5", 2019, 5, 55)]

    def find_by_seats_and_price(self, seats, price):
        list_cars_for_a_rent = []
        for auto in self.cars:
            if seats <= auto.seats and price >= \
                    auto.price and auto.status == "Free":
                list_cars_for_a_rent.append(auto)

        return list_cars_for_a_rent

    def change_status(self, license_plate, status):
        for auto in self.cars:
            if license_plate == auto.license_plate:
                auto.status = status
                return auto






