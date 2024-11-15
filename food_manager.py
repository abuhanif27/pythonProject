favourite_foods = []

def display_menu():
    print("\n=== Favourite Foods Manager ===")
    print("0. Exit")
    print("1. Add food")
    print("2. Remove food")
    print("3. View all favourite foods")
    print("===============================\n")

while True:
    display_menu()
    choice = input("Choose an option (0-3): ").strip()

    if choice == "0":
        print("\nThank you for using Favourite Foods Manager. Goodbye!")
        break

    elif choice == "1":
        food = input("Enter the name of your favourite food: ").strip()
        if food:
            favourite_foods.append(food)
            print(f"'{food}' has been added successfully!")
        else:
            print("Invalid input. Please enter a valid food name.")

    elif choice == "2":
        if favourite_foods:
            food = input("Enter the name of the food you want to remove: ").strip()
            if food in favourite_foods:
                favourite_foods.remove(food)
                print(f"'{food}' has been removed successfully!")
            else:
                print(f"'{food}' does not exist in your list.")
        else:
            print("Your favourite foods list is empty. Nothing to remove.")

    elif choice == "3":
        if favourite_foods:
            print("\nYour favourite foods:")
            for index, food in enumerate(favourite_foods, start=1):
                print(f"{index}. {food}")
        else:
            print("Your favourite foods list is empty. Add some food first!")

    else:
        print("Invalid choice! Please select a number between 0 and 3.")
