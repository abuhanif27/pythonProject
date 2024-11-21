import save_all_books

def remove_book(all_books):
    isbn = int(input("Enter ISBN of the book to remove: "))
    for book in all_books:
        if book["isbn"] == isbn:
            all_books.remove(book)
            save_all_books.save_all_books(all_books)
            print("Book removed successfully!")
            return all_books
    print("Book not found!")
    return all_books
