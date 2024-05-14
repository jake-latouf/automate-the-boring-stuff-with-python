def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

while True:
    print("Enter number:")
    user_input = input()

    if user_input.lower() == 'exit':
        break
    
    try:
        number = int(user_input)
        while number > 1:
          number = collatz(number)
          print(number)
    except ValueError:
        print("Please enter a valid integer.")
