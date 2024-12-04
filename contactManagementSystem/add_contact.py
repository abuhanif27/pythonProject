from Contact import Contact
from utility import is_valid_email


def add_contact():
    name = input("Enter contact's name: ")
    email = input("Enter contact's email: ")
    phone = input("Enter contact's phone: ")
    address = input("Enter contact's address: ")

    if not name.isalpha():
        print("The Contact's name must be string")
        return
    if not phone.isnumeric():
        print("The Contact's phone must be numeric")
        return
    if not is_valid_email(email):
        print("The Contact's email is not valid")
        return

    contact = Contact(name, email, phone, address)

    with open('contacts.csv', 'r') as f:
        contacts = f.readlines()
        for c in contacts:
            existing_name, existing_email, existing_phone, existing_address = c.split(",")
            if phone == existing_phone:
                print("This phone number already exists. Try again with a different number.")
                return  # quit from adding

    with open('contacts.csv', 'a') as f:
        f.write(f"{contact.get_name()},{contact.get_email()},{contact.get_phone()},{contact.get_address()}\n")

    print(f"{name}'s contact has been added.")
