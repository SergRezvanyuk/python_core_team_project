from collections import UserDict
import csv
from datetime import datetime
from pathlib import Path
import re
from fake_content_2 import user_1


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return self.__str__()    

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Name(Field):
    def __init__(self, name):
        super().__init__(name)
    

class Phone(Field):
    def __init__(self, phone):
        if phone:
            if phone.isdigit():
                self.phone = phone
            else:
                self.phone = None
                print('Error, phone must contain only digits')
        super().__init__(phone)


class Email(Field):
    def __init__(self, name):
        super().__init__(name)   


class Birthday(Field):
    def __init__(self, birthday: str):  #format: 'dd.mm.YYYY or dd/mm/YYYY or dd-mm-YYYY'
        if birthday:
            self.data_str = re.sub(r'[/-]', '.', birthday.strip())
            try:
                data = datetime.strptime(self.data_str, '%d.%m.%Y')
            except ValueError as err:
                print('bot>> Error, ' + str(err))
            else:
                self.data = data 
        else:
            self.data_str = ''

    def __str__(self):
        return self.data_str

    
class Address(Field):
    def __init__(self, name):
        super().__init__(name)   


class Record:
    def __init__(self, name, phone=None, birthday=None, email=None, address=None): 
        self.name = name
        self.phones = []
        self.birthday = birthday
        self.email = email
        self.address = address
        
        if phone:            
            self.phones.append(phone)



    def __str__(self):
        return f'# {self.name}: {self.phones} ({self.birthday})' # '#' - selector

    def __repr__(self):
        return self.__str__()
    
    def add_new_phone(self, new_phone):
        if type(new_phone) is Phone:
            self.phones.append(new_phone)
        else:
            self.phones.append(Phone(new_phone))

    def del_phone(self, phone=''):
        if not phone:
            self.phones.pop()  #delete the last phone number
        else:
            phone = phone.strip()
            if phone in self.phones:
                self.phones.remove(phone)
                return 'Phone number was deleted'
            else:
                return 'Error. This number is not in the phone list'



class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def del_record(self, name):
        if name not in self.data:
            print(f'bot>> Record with the name {name} not found')
        else:
            self.data.pop(name)



# *********************************************************************************************************


def write_AB(path, adr_book):    #write AddressBook in file
    if not len(adr_book):
        print('AddressBook is empty!')
    else:
        field_names = list(adr_book.data[list(adr_book.data)[0]].__dict__) # if type(adr_book) = class AddressBook
        # field_names = list(adr_book[list(adr_book)[0]].__dict__) # if type(adr_book) = dict
        with open(path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            for rec in adr_book.values():
                writer.writerow(rec.__dict__)


def main():
    path_file = Path(__file__).parent / 'AddressBook.csv'
    user_name = Name(user_1["name"])
    user_phone_1 = Phone(user_1["phone"])
    user_phone_2 = Phone("236598545")
    user_email = Email(user_1["email"])
    user_birthday = Birthday(user_1["birthday"])
    user_address = user_1["address"]
    
    record = Record(user_name, user_phone_1, user_birthday, user_email)
    ab = AddressBook()
    ab.add_record(record)
    print(ab)
    write_AB(path_file, ab)
    

if __name__ == "__main__":
    main()