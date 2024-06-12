
# write 'hello world' to the console
# print('hello world')


# write an user interactive rock paper scissors game played in the terminal against the computer. the user can choose each round whether or not to play again, and the player's score is displayed at the end.
# the computer's choice is randomly generated each round.
# the game should be able to handle invalid inputs and prompt the user to try again.
# the game should also be able to handle invalid inputs for whether or not the user wants to play again, and prompt the user to try again.
# the game should be able to handle invalid inputs for the user's choice of rock, paper, or scissors, and prompt the user to try again.
# the game should be able to handle invalid inputs for the user's choice of yes or no for whether or not to play again, and prompt the user to try again.
# the game should be able to handle invalid inputs for the user's choice of yes or no for whether or not to play again, and prompt the user to try again.

import random

print('Welcome to Rock, Paper, Scissors!')

user_score = 0

while True:
    user_choice = input('Choose rock, paper, or scissors: ').lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    if user_choice == 'rock':
        if computer_choice == 'rock':
            print('Computer chose rock. It\'s a tie!')
        elif computer_choice == 'paper':
            print('Computer chose paper. You lose!')
        elif computer_choice == 'scissors':
            print('Computer chose scissors. You win!')
            user_score += 1
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print('Computer chose rock. You win!')
            user_score += 1
        elif computer_choice == 'paper':
            print('Computer chose paper. It\'s a tie!')
        elif computer_choice == 'scissors':
            print('Computer chose scissors. You lose!')
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print('Computer chose rock. You lose!')
        elif computer_choice == 'paper':
            print('Computer chose paper. You win!')
            user_score += 1
        elif computer_choice == 'scissors':
            print('Computer chose scissors. It\'s a tie!')
    else:
        print('Invalid input. Please try again.')
        continue


    play_again = input('Do you want to play again? (yes/no): ')
    # make it so that the play_again input is case insensitive
    play_again = play_again.lower()

    if play_again == 'yes':
        continue
    elif play_again == 'no':
        break
    else:
        print('Invalid input. Please try again.')
        continue

print(f'Your score is {user_score}. Thanks for playing!') 