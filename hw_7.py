from collections import UserDict
from datetime import datetime, date, timedelta

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


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                return ph
        return None
    
    def remove_phone(self, phone):
        ph = self.find_phone(phone)
        if ph:
            self.phones.remove(ph)
            return
        raise ValueError(f"Номер {phone} не видалено, бо не знайдено.")

    def edit_phone(self, old_phone, new_phone):
        if self.find_phone(old_phone):
            self.add_phone(new_phone)
            self.remove_phone(old_phone)
            return
        raise ValueError(f"Номер {old_phone} не знайдено.")
    
    def add_birthday(self, bd):
        self.birthday = Birthday(bd)
                
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError(f"Запис з ім'ям {name} не знайдено.")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
    
    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = date.today()
        for record in self.data.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                days_until_birthday = (birthday_this_year - today).days
                if 0 <= days_until_birthday <= days:
                    congratulation_date = self.adjust_for_weekend(birthday_this_year)
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "birthday": congratulation_date
                    })
        return sorted(upcoming_birthdays, key=lambda x: x["birthday"])

    def find_next_weekday(self, start_date, weekday):
        start_weekday = start_date.weekday()
        if  start_weekday >= weekday : weekday += 7
        return start_date + timedelta(days = weekday - start_weekday)

    def adjust_for_weekend(self, birthday):
        if birthday.weekday() >= 5: birthday = self.find_next_weekday(birthday, 0)
        return birthday

    # def date_to_string(self, date):
    #     return date.strftime("%d.%m.%Y")
        

    
 # Тестування
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_birthday('02.01.1999')
# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
jane_record.add_phone("9884652112")
jane_record.add_birthday('31.12.2000')
book.add_record(jane_record)

# Виведення всіх записів у книзі
print(book)

# # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1116524823")
# print(john)

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")

# # видалення номеру телефону
# john.remove_phone('5555555555')

# # Видалення запису Jane
# book.delete("Jane")
# print(book)
print(book.get_upcoming_birthdays())