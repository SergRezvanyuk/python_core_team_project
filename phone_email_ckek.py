import re

from fake_content import user_1

phone1 = user_1['phone']
phone2 = '0679377063'
phone3 = '+369(56)5698874'
phone4 = '569 874 11'
phone5 = '9fvf336sv565'
phone6 = '16685190#$'

def is_valid_phone(phone):
    phone = phone.strip()
    pattern = r'^\+?\d+[-.\s]?\(?\d{1,3}\)?[-.\s]?\d+[-.\s]?\d+$'
    
    if re.match(pattern, phone):
        return True
    else:
        return False
    

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False
    
print(is_valid_phone(phone1))
print(is_valid_phone(phone2))
print(is_valid_phone(phone3))
print(is_valid_phone(phone4))
print(is_valid_phone(phone5))
print(is_valid_phone(phone6))