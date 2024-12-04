from utility import delete_utility


def delete_contact():
    DELETE_OPTIONS = ('name', 'email', 'phone', 'address')

    delete_by = input("Delete Contact By (name|email|phone|address): ").lower()

    if delete_by not in DELETE_OPTIONS:
        print("Incorrect Keyword to Delete")
        return

    delete_value = input(
        f"Enter an {delete_by} to delete: " if delete_by == 'email' or delete_by == 'address' else f"Enter a {delete_by} to delete: ").lower()

    with open('contacts.csv', 'r') as f:
        contacts = f.readlines()

    remaining_contacts = delete_utility(delete_by, delete_value, contacts)

    if isinstance(remaining_contacts, str):
        print("!" * 109)
        print(remaining_contacts.center(109 ))
        print("!" * 109)
    else:
        with open('contacts.csv', 'w') as f:
            for contact in remaining_contacts:
                f.write(contact)
