from restore_books_file import restore_all_books
from advancedLibraryManagementSystemCLI.add_books import add_books
from view_all_books import view_all_books
from update_book_file import update_books
from delete_book_file import delete_books
from lend_book import lend_book
from return_book import return_book

all_books = restore_all_books()

while True:
    print("\nWelcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Lend Book")
    print("6. Return Book")

    menu = input("Select an option: ")

    if menu == "0":
        print("Thank you for using the Library Management System!")
        break
    elif menu == "1":
        add_books(all_books)
    elif menu == "2":
        view_all_books(all_books)
    elif menu == "3":
        update_books(all_books)
    elif menu == "4":
        delete_books(all_books)
    elif menu == "5":
        lend_book(all_books)
    elif menu == "6":
        return_book(all_books)
    else:
        print("Invalid Option. Please try again.")
