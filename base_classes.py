from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # def __init__(self, value):
    #     super().__init__(value)
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Номер телефону має складатися з 10 цифр.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.bd = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(self.bd)

    def __str__(self):
        return self.bd.strftime("%d.%m.%Y")   