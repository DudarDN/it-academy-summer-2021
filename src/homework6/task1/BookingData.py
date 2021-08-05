class BookingData:

    def __init__(self):
        self.bookings = []

    def add_book(self, new_book):
        self.bookings.append(new_book)

    def get_bookings(self, phone_number):
        for booking in self.bookings:
            if phone_number == booking.customer_id:
                return booking.car_id

    def del_bookings(self, phone, license_place):
        for booking in self.bookings:
            if license_place == booking.car_id\
                    and phone == booking.customer_id:
                self.bookings.remove(booking)

