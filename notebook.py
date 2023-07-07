from datetime import datetime
import os
import pickle




notes = {}
max_nunber = 1


file_name = 'Notes.bin'

def new_record():
    global max_id
    print('Введіть текст:')
    text = input()
    if len(text)<2:
        print("Занадто короткий запис.")
        return

    print('Тег') #'(або кілька, розділені комою)')
    tag = input()
    rec = [text, datetime.now()]
    if len(tag)>0:
        # tag = tag.split(',')
        rec.append(tag)
    max_id += 1
    # print(rec)
    notes.update({max_id:rec})
    # print(notes)

    

    
    

def view_records():
    pass

def search_record():
    pass

def tag_record():
    pass

if os.path.exists(file_name):
    with open(file_name, "rb") as fh:
        notes = pickle.load(fh)
    max_id = 0
    for i in notes:
        if i > max_id:
            max_id = i
else:
    notes = {}
    max_id = 0


while True:
    print("Робота із нотатками:")
    choice = input("Н - новий запис, З - перегляд всіх записів, П - пошук, Т - пошук за тегом, інше - вихід.")
    if choice == 'н' or choice == 'Н' or choice == 'y' or choice == 'Y':
        new_record()
    elif choice == 'з' or choice == 'З'  or choice == 'p' or choice == 'P':
        view_records()
    elif choice == 'п' or choice == 'П' or choice == 'g' or choice == 'G':
        search_record()
    elif choice == 'т' or choice == 'Т' or choice == 'n' or choice == 'N':
        tag_record()
    else:
        break









