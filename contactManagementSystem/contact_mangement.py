from Contact import Contact

run = True
while run:
    print("Choose Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter contact's name: ")
        email = input("Enter contact's email: ")
        phone = input("Enter contact's phone: ")
        address = input("Enter contact's address: ")
        contact = Contact(name, email, phone, address)
        with open('contacts.csv', 'r') as f:
            contacts = f.readline()
            for c in contacts.split(','):
                if c[2] == contact.get_phone():
                    print("this Phone number already exists try again with different number.")
                    raise Exception("This Phone number already exists try again with different number.")

        with open('contacts.csv', 'a') as f:
            f.write(f"{contact.get_name()},{contact.get_email()},{contact.get_phone()},{contact.get_address()}\n")

    if choice == 2:
        with open('contacts.csv', 'r') as f:
            contacts = f.readlines()
            print("name | email | phone | address")
            for c in contacts[1:]:
                name, email, phone, address = c.split(",")
                print(f"{name} | {email} | {phone} |{address}", end='')
    if choice == 3:
        run = False
        print("Thank You!")
