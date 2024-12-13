import csv
from save_all_books import save_all_books

def return_book(all_books):
    search_term = input("Enter Book Title or ISBN to Return: ").strip()
    borrower = input("Enter Borrower's Name: ").strip()

    for book in all_books:
        if book["title"].lower() == search_term.lower() or str(book["isbn"]) == search_term:
            matching_borrowers = [
                b if isinstance(b, str) else b.get('name', '')
                for b in book["lent_to"]
                if (isinstance(b, str) and b.lower() == borrower.lower()) or
                   (isinstance(b, dict) and b.get('name', '').lower() == borrower.lower())
            ]

            if matching_borrowers:
                book["lent_to"] = [
                    b for b in book["lent_to"]
                    if (isinstance(b, str) and b.lower() != borrower.lower()) or
                       (isinstance(b, dict) and b.get('name', '').lower() != borrower.lower())
                ]
                book["quantity"] += 1

                try:
                    # Read all rows
                    with open("borrowers.csv", "r") as file:
                        rows = list(csv.reader(file))


                    with open("borrowers.csv", "w", newline="") as file:
                        writer = csv.writer(file)
                        for row in rows:

                            if (row[0].lower() != borrower.lower() or
                                    row[2].lower() != book["title"].lower()):
                                writer.writerow(row)

                    save_all_books(all_books)
                    print("Book Returned Successfully!")
                    return

                except FileNotFoundError:
                    print("Borrowers file not found.")
                    return

            print("This book was not borrowed by this person.")
            return

    print("Book Not Found.")
    return