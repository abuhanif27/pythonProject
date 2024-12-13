from save_all_books import save_all_books


def lend_book(all_books):
    search_term = input("Enter Book Title or ISBN to Lend: ")
    for book in all_books:
        if book["title"] == search_term or str(book["isbn"]) == search_term:
            if book["quantity"] > 0:
                borrower = input("Enter Borrower's Name: ")
                if borrower:
                    book["lent_to"].append(borrower)
                    book["quantity"] -= 1
                    save_all_books(all_books)
                    print("Book Lent Successfully!")
                    return
                else:
                    print("Borrower's Name Cannot Be Empty.")
                    return
            else:
                print("Book Out of Stock.")
                return

    print("Book Not Found.")
