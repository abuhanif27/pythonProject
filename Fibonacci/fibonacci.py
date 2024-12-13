def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_by_terms(n):
    return [fibonacci(i) for i in range(n)]


def fibonacci_by_max(max_n):
    series = []
    i = 0
    while True:
        fib = fibonacci(i)
        if fib > max_n:
            break
        series.append(fib)
        i += 1
    return series


run = True
while run:
    print("\nChoose an option:")
    print("1. Generate Fibonacci series by number of terms")
    print("2. Generate Fibonacci series by maximum value")
    print("3. Exit")
    try:
        option = int(input("Your Choice: "))
        if option == 1:
            terms = int(input("Enter the number of terms: "))
            if terms < 0:
                print("Please enter a non-negative number.")
            else:
                series = fibonacci_by_terms(terms)
                print(f"Fibonacci series ({terms} terms): ", end="")
                for num in series:
                    print(num, end=" ")
                print("\n")
        elif option == 2:
            max_value = int(input("Enter the maximum value: "))
            if max_value < 0:
                print("Please enter a non-negative number.")
            else:
                series = fibonacci_by_max(max_value)
                print(f"Fibonacci series (up to {max_value}): ", end="")
                for num in series:
                    print(num, end=" ")
                print("\n")
        elif option == 3:
            run = False
            print("Thank you for using my Fibonacci program!")
        else:
            print("Invalid Choice. Please select 1, 2, or 3.")
    except ValueError:
        print("Please enter a valid number.")
