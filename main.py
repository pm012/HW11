from collections import UserDict
import re


class Field:
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError("Value is not valid")
        self.value = value

    def __str__(self):
        return str(self.value)
    
    # Validation of fields
    def is_valid(self, value)->bool:
        return bool(value)


   
# Removed usless constructor    
class Name(Field):
    pass
    

class Phone(Field):
    
    def is_valid(self, phone)->bool:
        return bool(re.match(r'^\d{10}$', phone))

   
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)        
        self.phones.append(phone)
        
    
    def edit_phone(self, phone_old, phone_new):
        phone_new = Phone(phone_new)
        for i, phone in enumerate(self.phones):
            if phone.value == phone_old:
                self.phones[i] = phone_new                
                return
        raise ValueError("Phone not found")
    
    def find_phone(self, phone):
        # Removed enumarate
        for phone_item in self.phones:
            if phone_item.value == phone:
                return phone_item
            
        return None
    
    def remove_phone(self, phone):
        for _, phone_item in enumerate(self.phones):
            if phone_item.value == phone:
                self.phones.remove(phone_item)

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        if not record.name:
            return
        self.data[record.name.value] = record

    def find(self, name:str):
        return  self.data.get(name, None)
    
    def delete(self, name:str):        
            self.pop(name, None)


if __name__ == '__main__':
 # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
    book.delete("Jane")
    john_record.remove_phone('5555555555')

    for name, record in book.data.items():
        print(record)