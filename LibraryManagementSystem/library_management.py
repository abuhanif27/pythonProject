from add_books import add_books
from view_all_books import view_all_books
from update_book import update_book
from remove_book import remove_book
from lend_book import lend_book
from return_book import return_book

try:
    with open("all_books.csv", "r") as fp:
        all_books = []
        for line in fp:
            title, author, isbn, year, price, quantity = line.strip().split(", ")
            book = {
                "title": title,
                "author": author,
                "isbn": int(isbn),
                "year": int(year),
                "price": int(price),
                "quantity": int(quantity),
            }
            all_books.append(book)
except FileNotFoundError:
    all_books = []

while True:
    print("\nWelcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Update Book")
    print("4. Remove Book")
    print("5. Lend a Book")
    print("6. Return a Book")

    menu = input("Select any number: ")

    if menu == "0":
        print("Thanks for using Library Management System!")
        break
    elif menu == "1":
        all_books = add_books(all_books)
    elif menu == "2":
        view_all_books(all_books)
    elif menu == "3":
        all_books = update_book(all_books)
    elif menu == "4":
        all_books = remove_book(all_books)
    elif menu == "5":
        all_books = lend_book(all_books)
    elif menu == "6":
        all_books = return_book(all_books)
    else:
        print("Choose a valid number")
