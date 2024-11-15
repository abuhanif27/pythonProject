def multiplication(number):
    for _ in range(1, 11):
        result = number * _
        print(f"{number}x{_} = {result}")


if __name__ == '__main__':
    multiplication(5)
