from utility import search_utility


def search_contact():
    SEARCH_OPTIONS = ('name', 'email', 'phone', 'address')

    search_by = input("Find by (name|email|phone|address): ").lower()

    if search_by not in SEARCH_OPTIONS:
        print("Incorrect Keyword to Search")
        return

    search_term = input(
        f"Enter an {search_by} to search: " if search_by == 'email' or search_by == 'address' else f"Enter a {search_by} to search: ").lower()

    with open('contacts.csv', 'r') as f:
        contacts = f.readlines()

    search_results = search_utility(search_by, search_term, contacts)

    if isinstance(search_results, str):
        print("!" * 109)
        print(search_results.center(109 ))
        print("!" * 109)
    else:
        print("=" * 109)
        print(f"       SEARCH BY '{search_term}'       ".center(109))
        print("=" * 109)
        print(
            "name".center(25) + " | " + "email".center(25) + " | " + "phone".center(25) + " | " + "address".center(25))
        print("-" * 25 + " + " + "-" * 25 + " + " + "-" * 25 + " + " + "-" * 25)

        for result in search_results:
            print(result)
            print("-" * 25 + " + " + "-" * 25 + " + " + "-" * 25 + " + " + "-" * 25)
