import json

def restore_all_books():
    try:
        with open("all_books.json", "r") as fp:
            return json.load(fp)
    except FileNotFoundError:
        return []
