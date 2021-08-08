class BookingData:

    def __init__(self):
        self.bookings = {}

    def add_book(self, new_booking):
        self.bookings[new_booking.customer_id] = new_booking.car_id

    def get_bookings(self, phone_number):
        return self.bookings.get(phone_number)

    def del_bookings(self, phone):
        return self.bookings.pop(phone)
