from save_all_books import save_all_books
from datetime import datetime, timedelta
import csv


def lend_book(all_books):
    search_term = input("Enter Book Title or ISBN to Lend: ")
    for book in all_books:
        if book["title"] == search_term or str(book["isbn"]) == search_term:
            if book["quantity"] > 0:
                borrower_name = input("Enter Borrower's Name: ")
                borrower_phone = input("Enter Borrower's Phone Number: ")
                due_date = (datetime.now() + timedelta(days=14)).strftime("%d-%m-%Y")

                if borrower_name and borrower_phone:
                    book["lent_to"].append({"name": borrower_name, "phone": borrower_phone, "due_date": due_date})
                    book["quantity"] -= 1

                    with open("borrowers.csv", "a", newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([borrower_name, borrower_phone, book["title"], due_date])

                    save_all_books(all_books)
                    print(f"Book Lent Successfully! Due Date: {due_date}")
                    return
                else:
                    print("Borrower's Name and Phone Cannot Be Empty.")
                    return
            else:
                print("Book Out of Stock.")
                return

    print("Book Not Found.")
