from save_all_books import save_all_books

def lend_book(all_books):
    isbn = int(input("Enter ISBN of the book to lend: "))
    for book in all_books:
        if book["isbn"] == isbn:
            if book["quantity"] > 0:
                book["quantity"] -= 1
                save_all_books(all_books)
                print(f"Book '{book['title']}' lent successfully!")
            else:
                print("No copies available to lend.")
            return all_books
    print("Book not found!")
    return all_books
