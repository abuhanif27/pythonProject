from Contact import Contact

run = True
while run:
    print("Choose Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Exit")

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
        search_by = input("Find by (name|email|phone|address): ")
        if search_by.lower() not in ('name', 'email', 'phone', 'address'):
            raise Exception("Incorrect Keyword to Search")
        search = input(f"Enter a {search_by} to search: ").lower()
        search_results = []
        with open('contacts.csv', 'r') as f:
            contacts = f.readlines()
            for c in contacts:
                name, email, phone, address = c.split(",")
                contact = Contact(name, email, phone, address)
                if search_by.lower() == "name":
                    if search == name.lower():
                        search_results.append(contact)
                    else:
                        raise Exception("Contact Name Not Found")
                elif search_by.lower() == 'email':
                    if search == email.lower():
                        search_results.append(Contact(name, email, phone, address))
                    else:
                        raise Exception("Contact Email Not Found")
                elif search_by.lower() == 'phone':
                    if search == phone.lower():
                        search_results.append(Contact(name, email, phone, address))
                    else:
                        raise Exception("Contact Phone Number Not Found")
                else:
                    if search == address.lower():
                        search_results.append(Contact(name, email, phone, address))
                    else:
                        raise Exception("Contact Address Not Found")

            for r in search_results:
                print(r)

    if choice == 4:
        run = False
        print("Thank You!")
