from add_contact import add_contact
from delete_contact import delete_contact
from search_contact import search_contact
from view_contact import view_contact

run = True
while run:
    print("~" * 109)
    print("            CONTACT MANAGEMENT APP            ".center(109, "~"))
    print("~" * 109)
    print("\nChoose an Option:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Remove Contact")
    print("5. Exit")

    print("=" * 109)

    try:
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contact()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            delete_contact()
        elif choice == 5:
            run = False
            print("\nThank you for using the app!")
        else:
            print("\nInvalid choice. Please select a number between 1 and 5.")

    except ValueError:
        print("\nInvalid input. Please enter a valid number.")
