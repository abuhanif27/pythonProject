import os
import csv


class Banking:
    def __init__(self, user_name, initial_balance=0):
        self.name = user_name
        self.balance = initial_balance if initial_balance >= 0 else 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Updated Balance: {self.balance}"
        else:
            return "Deposit amount must be greater than zero."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrawn Amount: {amount}\nUpdated Balance: {self.balance}"
            else:
                return "Insufficient balance for the requested withdrawal."
        else:
            return "Withdrawal amount must be greater than zero."

    def get_balance(self):
        return f"Your current balance is: {self.balance}"

    def save_account(self):
        with open('bank_account.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.balance])
        return f"Account details saved. Goodbye, {self.name}!"

    def load_account(self):
        if os.path.exists('bank_account.csv'):
            with open('bank_account.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    account_name, acc_balance = row
                    if account_name == self.name:
                        self.balance = float(acc_balance)
                        return
        self.balance = 0  # Default balance if account is not found

    def get_valid_amount(self, prompt):
        while True:
            amount = input(prompt)
            if amount.isnumeric():
                amount = float(amount)
                if amount > 0:
                    return amount
                else:
                    print("Amount must be greater than zero. Please try again.")
            else:
                print("Invalid input. Please enter a valid number.")

    def __str__(self):
        return f"Account Holder: {self.name}\nCurrent Balance: {self.balance}"


# Test result
print("Welcome to the Banking System!")

name = input("Please enter your name: ")

account = Banking(name)
account.load_account()
print(account)

while True:
    print("\nChoose an operation:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':  # Deposit
        amount = account.get_valid_amount("Enter the amount to deposit: ")
        print(account.deposit(amount))

    elif choice == '2':  # Withdraw
        amount = account.get_valid_amount("Enter the amount to withdraw: ")
        print(account.withdraw(amount))

    elif choice == '3':  # Check Balance
        print(account.get_balance())

    elif choice == '4':  # Exit
        print(account.save_account())
        break

    else:
        print("Invalid choice. Please try again.")
