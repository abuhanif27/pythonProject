def view_contact():
    with open('contacts.csv', 'r') as f:
        contacts = f.readlines()
        if len(contacts) > 1:
            print("=" * 109)
            print("       ALL CONTACTS LIST       ".center(109))
            print("=" * 109)
            print(
                "name".center(25) + " | " + "email".center(25) + " | " + "phone".center(25) + " | " + "address".center(
                    25))
            print("-" * 25 + " + " + "-" * 25 + " + " + "-" * 25 + " + " + "-" * 25)
            for c in contacts[1:]:
                name, email, phone, address = c.split(",")
                print(f"{name.center(25)} | {email.center(25)} | {phone.center(25)} | {address.center(25)}")
                print("-" * 25 + " + " + "-" * 25 + " + " + "-" * 25 + " + " + "-" * 25)

            print("=" * 109)
        else:
            print("!" * 109)
            print("Contact List is Empty!".center(109))
            print("!" * 109)
