# this is a guess the number game
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

# ask the player to guess 6 times.
for guesses_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break  # this condition is the correct guess

if guess == secretNumber:
    print('Good job! you guessed the number in ' + str(guesses_taken) + 'guesses!')
else:
    print('Nope. the number I was thinking of was ' + str(secretNumber))