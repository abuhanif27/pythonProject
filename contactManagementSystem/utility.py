from Contact import Contact


def search_utility(search_by, search_term, contacts):
    search_results = []
    for c in contacts:
        name, email, phone, address = c.split(",")
        contact = Contact(name, email, phone, address)

        search_attribute = {
            "name": name.lower(),
            "email": email.lower(),
            "phone": phone.lower(),
            "address": address.lower(),
        }

        if search_attribute[search_by] == search_term:
            search_results.append(contact)

    if not search_results:
        return f"Contact {search_by.capitalize()} Not Found"

    return search_results


def delete_utility(delete_by, delete_value, contacts):
    remaining_contacts = []
    contact_found = False

    for c in contacts:
        name, email, phone, address = c.split(",")

        delete_attribute = {
            "name": name.lower(),
            "email": email.lower(),
            "phone": phone.lower(),
            "address": address.lower(),
        }

        if delete_attribute[delete_by] != delete_value:
            remaining_contacts.append(c)
        else:
            print(f"{delete_attribute[delete_by]} contact has been deleted successfully!")
            contact_found = True

    if not contact_found:
        return f"Contact {delete_by.capitalize()} Not Found"

    return remaining_contacts


def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    return False
