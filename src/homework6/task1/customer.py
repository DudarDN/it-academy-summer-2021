class Customer:
    """Класс для представления клиента

    Конструктор принимает имя, возраст, e-mail, а также номер телефона клиента

    """
    def __init__(self, name, age, email, phone):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
