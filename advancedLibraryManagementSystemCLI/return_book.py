from save_all_books import save_all_books
import csv


def return_book(all_books):
    search_term = input("Enter Book Title or ISBN to Return: ")
    borrower = input("Enter Borrower's Name: ")

    for book in all_books:
        if book["title"] == search_term or str(book["isbn"]) == search_term:
            if borrower in book["lent_to"]:
                book["lent_to"].remove(borrower)
                book["quantity"] += 1

                try:
                    with open("borrowers.csv", "r") as file:
                        rows = list(csv.reader(file))

                    with open("borrowers.csv", "w", newline="") as file:
                        writer = csv.writer(file)
                        for row in rows:
                            if row[0] != borrower or row[2] != book["title"]:
                                writer.writerow(row)
                except FileNotFoundError:
                    print("Borrowers file not found.")

                save_all_books(all_books)
                print("Book Returned Successfully!")
                return

            print("Borrower Not Found.")
            return

    print("Book Not Found.")
