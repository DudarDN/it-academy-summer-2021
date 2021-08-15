class Customer:
    """Класс для представления клиента"""

    def __init__(self, name, age, email, phone):
        """Конструктор класса.

        Принимает имя, возраст, e-mail, а также номер телефона клиента

        """
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
