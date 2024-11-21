import save_all_books

def return_book(all_books):
    isbn = int(input("Enter ISBN of the book to return: "))
    for book in all_books:
        if book["isbn"] == isbn:
            book["quantity"] += 1
            save_all_books.save_all_books(all_books)
            print(f"Book '{book['title']}' returned successfully!")
            return all_books
    print("Book not found!")
    return all_books
