from Contact import Contact


def add_contact():
    name = input("Enter contact's name: ")
    email = input("Enter contact's email: ")
    phone = input("Enter contact's phone: ")
    address = input("Enter contact's address: ")

    contact = Contact(name, email, phone, address)

    with open('contacts.csv', 'r') as f:
        contacts = f.readlines()
        for c in contacts:
            existing_name, existing_email, existing_phone, existing_address = c.split(",")
            if phone == existing_phone:
                print("This phone number already exists. Try again with a different number.")
                return # quit from adding

    with open('contacts.csv', 'a') as f:
        f.write(f"{contact.get_name()},{contact.get_email()},{contact.get_phone()},{contact.get_address()}\n")

    print(f"{name}'s contact has been added.")
