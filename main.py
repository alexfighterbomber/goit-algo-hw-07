# from datetime import date, timedelta
from base_classes import *
from record import *
from address_book import *
from input_error import *


    # def date_to_string(self, date):
    #     return date.strftime("%d.%m.%Y")
        

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
            pass
        elif command == "add":
            # реалізація
            pass
        elif command == "change":
            # реалізація
            pass
        elif command == "phone":
            # реалізація
            pass
        elif command == "all":
            # реалізація
            pass
        elif command == "add-birthday":
            # реалізація
            pass
        elif command == "show-birthday":
            # реалізація
            pass
        elif command == "birthdays":
            # реалізація
            pass
        else:
            print("Invalid command.")
            pass



# if __name__ == "__main__":
#     main()


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