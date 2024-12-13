from save_all_books import save_all_books
from datetime import datetime


def update_books(all_books):
    search_term = input("Enter Book Title or ISBN to Update: ")
    for book in all_books:
        if book["title"] == search_term or str(book["isbn"]) == search_term:
            book["title"] = input("Enter New Title: ") or book["title"]
            book["author"] = input("Enter New Author: ") or book["author"]
            book["year"] = int(input("Enter New Publishing Year: ")) or book["year"]
            book["price"] = int(input("Enter New Price: ")) or book["price"]
            book["quantity"] = int(input("Enter New Quantity: ")) or book["quantity"]
            book["bookLastUpdatedAt"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            save_all_books(all_books)
            print("Book Updated Successfully!")
            return

    print("Book Not Found.")
