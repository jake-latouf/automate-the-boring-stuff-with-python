import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables will keep track of the number of wins, losses, and ties
wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # main game loop
        print('Enter your move: (r)ock (p)aper, (s)cissors, or (q)uit')
        player_move = input()
        if player_move == 'q':
            sys.exit() # quit the program
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break
        print('Type one of r, p, s, or q.')

    # Display what the player chose
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # Display what the computer chose
    randomNumber = random.randint(1, 3)

    if randomNumber == 1:
        computer_move = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computer_move = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computer_move = 's'
        print('SCISSORS')

    if player_move == computer_move:
        print('It is a tie!')
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        losses = losses + 1