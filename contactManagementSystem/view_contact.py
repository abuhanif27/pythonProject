def view_contact():
    print("=" * 109)
    print("       ALL CONTACTS LIST       ".center(109))
    print("=" * 109)
    with open('contacts.csv', 'r') as f:
        contacts = f.readlines()
        print(
            "name".center(25) + " | " + "email".center(25) + " | " + "phone".center(25) + " | " + "address".center(25))
        print("-" * 25 + " + " + "-" * 25 + " + " + "-" * 25 + " + " + "-" * 25)
        for c in contacts[1:]:
            name, email, phone, address = c.split(",")
            print(f"{name.center(25)} | {email.center(25)} | {phone.center(25)} | {address.center(25)}")
            print("-" * 25 + " + " + "-" * 25 + " + " + "-" * 25 + " + " + "-" * 25)

        print("=" * 109)
