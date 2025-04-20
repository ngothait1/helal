def save_entry():
    id = input("ID: ")
    if not id.isdigit():
        print("ID must be a number.")
        return
    name = input("Name: ")
    age = input("Age: ")
    try:
        float(age)  # just to check it's a number
    except ValueError:
        print("Age must be a number.")
        return
    people.append({'id': id, 'name': name, 'age': age})
    print(f'ID [{id}] saved successfully')



def Search_id():
    a = input("Enter the ID you want to look for: ")
    if not a.isdigit():
        print("ID must be a number.")
        return

    found = False
    for person in people:
        if person['id'] == a:
            print('ID:', person['id'])
            print('Name:', person['name'])
            print('Age:', person['age'])
            found = True
            break
    if not found:
        print("ID not found.")



def age_avg():
    avg = 0
    num = 0
    for person  in people:
        num += float(person['age'])
        avg = num / len(people)

    return print(f"the average age of the people is {avg}")


def print_names():
    for i, person in enumerate(people):
        print(f"{i}. {person['name']}")

    return


def print_ids():
    for i, person in enumerate(people):
        print(f"{i}. {person['id']}")


    return

def print_all():
    for i, person in enumerate(people):
        print(f"{i}. ID: {person['id']}, Name: {person['name']}, Age: {person['age']}")

    return

def print_entry_indx():
    try:
        ind = int(input("Please enter the index of the entry you want to print: "))
        print(people[ind])
    
    except ValueError:
        print(f"Error: index must be a number. {ind} is not a number")

    return
people = []
loop = True

while  loop:
    print('1. Save a new entry')

    print('2. Search by ID')

    print('3. Print ages average')

    print('4. Print all names')

    print('5. Print all IDs')

    print('6. Print all entries')

    print('7. Print entry by indes')

    print('8. Exit')
    
    print("")

    input_user = input('Please enter your choice: ')
    

    if input_user == '1':
        save_entry()
        input('Press Enter to continue ')

    elif input_user == '2':
        Search_id()
        input('Press Enter to continue ')
    
    elif input_user == '3':
        age_avg()
        input('Press Enter to continue ')
    
    elif input_user == '4':
        print_names()
        input('Press Enter to continue ')

    elif input_user == '5':
        print_ids()
        input('Press Enter to continue ')

    elif input_user == '6':
        print_all()
        input('Press Enter to continue ')
    
    elif input_user == '7':
        print_entry_indx()
        input('Press Enter to continue ')

    elif input_user == '8':
        loop = False 
        print("Exiting the program. Goodbye!")    

    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
        input('Press Enter to continue ')