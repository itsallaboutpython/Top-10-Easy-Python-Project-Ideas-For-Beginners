database = {'entries': []}

SRNO = 'srno'
NAME = 'name'
AGE = 'age'
GENDER = 'gender'
OCCUPATION = 'occupation'

def get_serial_no():
    return len(database['entries']) + 1

def add_entry(entry):
    entry = {
        'srno': get_serial_no(),
        'name': entry['name'],
        'age': entry['age'],
        'gender': entry['gender'],
        'occupation': entry['occupation']
    }
    database['entries'].append(entry)

def check_entry_presence(value):
    for num, entry in enumerate(database['entries']):
        if entry[value[0]] == value[1]:
            return 1
    return 0

def search_entry(value):
    for num, entry in enumerate(database['entries']):
        if entry[value[0]] == value[1]:
            return entry

def update_entry(value, updated_entry):
    for num, entry in enumerate(database['entries']):
        if entry[value[0]] == value[1]:
            database['entries'][num] == updated_entry

def delete_entry(value):
    for num, entry in enumerate(database['entries']):
        if entry[value[0]] == value[1]:
            database['entries'].remove(entry)

def display_entry(entry):
    print(f"SRNO: {entry['srno']}")
    print(f"Name: {entry['name']}")
    print(f"Age: {entry['age']}")
    print(f"Gender: {entry['gender']}")
    print(f"Occupation: {entry['occupation']}\n")

def display_all_entries():
    for entry in database["entries"]:
        display_entry(entry)

def select_entry_and_value():
    value_type = ''
    value = ''
    while 1:
        print('Choose an entry based on which to search entries in database: ')
        print("1. srno")
        print("2. name")
        print("3. age")
        print("4. gender")
        print("5. occupation")
        choice = int(input("Enter your choice: "))
        if choice < 1 or choice > 5:
            print("Invalid input...please try again")
        else:
            if choice == 1:
                value_type = SRNO
                value = input("Enter serial number to search: ")
                return (value_type, value)
            elif choice == 2:
                value_type = NAME
                value = input("Enter name to search: ")
                return (value_type, value)
            elif choice == 3:
                value_type = AGE
                value = input("Enter age to search: ")
                return (value_type, value)
            elif choice == 4:
                value_type = GENDER
                value = input("Enter gender to search: ")
                return (value_type, value)
            elif choice == 5:
                value_type = OCCUPATION
                value = input("Enter occupation to search: ")
                return (value_type, value)

def get_entry_details():
    output = {}
    output[NAME] = input("Enter name: ")
    output[AGE] = input("Enter age: ")
    output[GENDER] = input("Enter gender: ")
    output[OCCUPATION] = input("Enter occupation: ")
    return output

print("===== Welcome To User Management System =====")
while 1:
    print("\nWhat would you like to do:-")
    print("1. Add an entry")
    print("2. Update an entry")
    print("3. Delete an entry")
    print("4. Search an entry")
    print("5. Display all entries")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice > 7 or choice < 1:
        print("Invalid input...please try again")
    else:
        if choice == 1:
            print("Enter details for the new entry:-")
            entry = get_entry_details()
            add_entry(entry)
            print("Entry successfully created...")
        elif choice == 2:
            value = select_entry_and_value()
            print('Enter the details of the updated entry:-')
            entry = get_entry_details()
            update_entry(value, entry)
            print("Entry successfully updated...")
        elif choice == 3:
            value = select_entry_and_value()
            delete_entry(value)
            print("Entry successfully deleted...")
        elif choice == 4:
            value = select_entry_and_value()
            entry = search_entry(value)
            display_entry(entry)
        elif choice == 5:
            display_all_entries()
        elif choice == 6:
            print('Exiting')
            break