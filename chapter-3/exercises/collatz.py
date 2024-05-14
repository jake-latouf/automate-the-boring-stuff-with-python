def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

while True:
    print("Enter number:")
    number = input()
    try:
        number = int(number)
        while number > 1:
          number = collatz(number)
          print(number)
    except ValueError:
        print("Please enter a valid integer.")
