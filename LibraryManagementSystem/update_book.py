import save_all_books

def update_book(all_books):
    isbn = int(input("Enter ISBN of the book to update: "))
    for book in all_books:
        if book["isbn"] == isbn:
            print("Current details:", book)
            book["title"] = input("New title (leave blank to keep): ") or book["title"]
            book["author"] = input("New author(s) (leave blank to keep): ") or book["author"]
            book["year"] = input("New year (leave blank to keep): ") or book["year"]
            book["price"] = input("New price (leave blank to keep): ") or book["price"]
            book["quantity"] = input("New quantity (leave blank to keep): ") or book["quantity"]
            save_all_books.save_all_books(all_books)
            print("Book updated successfully!")
            return all_books
    print("Book not found!")
    return all_books
