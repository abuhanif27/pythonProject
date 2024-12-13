from save_all_books import save_all_books


def delete_books(all_books):
    search_term = input("Enter Book Title or ISBN to Delete: ")
    for book in all_books:
        if book["title"] == search_term or str(book["isbn"]) == search_term:
            all_books.remove(book)
            save_all_books(all_books)
            print("Book Deleted Successfully!")
            return

    print("Book Not Found.")
