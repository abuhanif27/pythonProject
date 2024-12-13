def view_all_books(all_books):
    if all_books:
        for book in all_books:
            print(
                f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']} | Added At: {book['bookAddedAt']} | Updated At: {book['bookLastUpdatedAt']} | Lent To: {book['lent_to']}")
    else:
        print("No books available.")
