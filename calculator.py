print("""Welcome to Calculator Project
1. Addition
2. Subtraction
3. Multiplication
4. Division
""""")

option = int(input("Select an option for Basic Calculator Operation: "))

if option in (1, 2, 3, 4):
    number1 = int(input("Enter 1st Number: "))
    number2 = int(input("Enter 2nd Number: "))
    if option == 1:
        result = number1 + number2
        print("Addition is: " + str(result))
    elif option == 2:
        result = number1 - number2
        print("Subtraction is: " + str(result))
    elif option == 3:
        result = number1 * number2
        print("Multiplication is: " + str(result))
    else:
        result = number1 / number2
        print("Division is: " + str(result))
else:
    print("Invalid Input")
