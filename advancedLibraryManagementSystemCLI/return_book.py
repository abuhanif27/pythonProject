from save_all_books import save_all_books


def return_book(all_books):
    search_term = input("Enter Book Title or ISBN to Return: ")
    borrower_name = input("Enter Borrower's Name: ")
    for book in all_books:
        if book["title"] == search_term or str(book["isbn"]) == search_term:
            for borrower in book["lent_to"]:
                if borrower["name"] == borrower_name:
                    book["lent_to"].remove(borrower)
                    book["quantity"] += 1
                    save_all_books(all_books)
                    print("Book Returned Successfully!")
                    return

            print("Borrower Not Found.")
            return

    print("Book Not Found.")
