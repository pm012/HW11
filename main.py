from collections import UserDict
from dateutil.parser import parse
from datetime import datetime
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


   
class Birthday(Field):
    def __init__(self, birthday):
        self.birthday = birthday


    def is_valid(self, birthday)->bool:
        #check if it is possible to convert exact string (fuzzy = False) to date
        try:
            birthday_date = parse(birthday, fuzzy=False)
            print(birthday_date)
            return True
        except ValueError:
            return False



class Name(Field):
    pass
    

class Phone(Field):
    
    def is_valid(self, phone)->bool:
        return bool(re.match(r'^\d{10}$', phone))

   
class Record:
    def __init__(self, name, birthday:Birthday=""):
        self.name = Name(name)
        self.birthday = ""
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)        
        self.phones.append(phone)

    def days_to_birthday(self, birthday: Birthday)->int:
        current_date = datetime.now().date()
        birthday_date_this_year = parse(birthday, fuzzy=False).replace(year = datetime.now().year).date()
        delta = birthday_date_this_year - current_date
        # if birthdate in future current year
        if delta.days>0:
            return delta.days
        else: 
            # if birthdate in current year has passed (calculate days to next year's date)
            return (birthday_date_this_year.replace(year=current_date.year+1) - current_date).days
                
    
    def edit_phone(self, phone_old, phone_new):
        phone_new = Phone(phone_new)
        for i, phone in enumerate(self.phones):
            if phone.value == phone_old:
                self.phones[i] = phone_new                
                return
        raise ValueError("Phone not found")
    
    def find_phone(self, phone):        
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

    def __next__(self):
        #TODO
        pass
    
    def __iter__(self):
        #TODO
        return dict()


if __name__ == '__main__':
    pass