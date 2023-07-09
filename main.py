import csv
import re
import pickle

from get_upcoming_birthday import get_upcoming_birthdays
from collections import UserDict
from datetime import datetime
from pathlib import Path
from fake_content_2 import user_1

file_name = "addressbook.bin"

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
        return f'# {self.name}: {self.phones} {self.birthday} {self.email} {self.address}' # '#' - selector

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
    def __init__(self):
        self.data = []
    
    def add_record(self, record):
        self.data.append(record)

    def del_record(self, name):
        if name not in self.data:
            print(f'bot>> Record with the name {name} not found')
        else:
            self.data.pop(name)


def write_ab(file_name, adr_book):    #write AddressBook in file
    with open(file_name, 'w', newline=',', encoding='utf-8') as fh:
        field_names = ['name', 'phone', 'birthday', 'email', 'address']
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        for rec in adr_book.values():
            writer.writerow(rec.__dict__)
            
def dump_file(addressbook):
    with open(file_name, "wb") as fh:
        pickle.dump(addressbook, fh)

def load_file():
    with open(file_name, "rb") as fh:
        addressbook = pickle.load(fh)
    return addressbook


def name_is_free(name):
    names = []
    with open(file_name, newline=',') as fh:
        spam_reader = csv.reader(fh)
        for raw in spam_reader:
            names.append(raw[1])
        
    if name in names:
        return False
    
    return True
        

def create_record():
    while True:
        name = input("Введіть ім'я контакту\n>_")
        if name_is_free(name):
            name = Name(name)
            break
        else:
            print("Такий контакт вже існує!")
            continue
    
    phone = input("Введіть номер телефону\n>_")
    phone = Phone(phone) or None
    
    email = input("Введіть електронну пошту\n>_")
    email = Email(email) or None
    
    birthday = input("Введіть дату народження у форматі дд/мм/рррр\n>_")
    birthday = Birthday(birthday) or None
    
    address = input("Введіть адресу\n>_")
    address = Address(address) or None
    
    contact = Record(name, phone, birthday, email, address)
    
    return contact
    

def users(addressbook):
    


def run_addressbook():
    ab = AddressBook()
    print("Вітаю!")
    while True:
        command = input(">_ ")
        match command:
            case "створити контакт":
                contact = create_record()
                ab.add_record(contact)
                print("Контакт створено!")
            case "привітання":
                users = 
                get_upcoming_birthdays(users)
                
       
    

if __name__ == "__main__":
    run_addressbook()