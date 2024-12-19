import random

ROCK = 'rock'
PAPER = 'paper'
SCISSOR = 'scissor'
choices = [ROCK, PAPER, SCISSOR]
positive = [[PAPER, ROCK], [SCISSOR, PAPER], [ROCK, SCISSOR]]
negative = [[ROCK, PAPER], [PAPER, SCISSOR], [SCISSOR, ROCK]]

def get_computer_move():
    return random.choice(choices)

def find_winner(user_move, computer_move):
    if [user_move, computer_move] in positive:
        return 1
    elif [user_move, computer_move] in negative:
        return -1
    return 0

print("===== Welcome to Rock, Paper And Scissor Game =====")
while True:
    choice = input("Do you wanna play (y/n): ").strip().lower()
    if choice == 'y':
        computer_move = get_computer_move()
        while True:
            move = input("Select a move ('r' for rock/'p' for paper/'s' for scissor): ").strip().lower()
            if move in ['r', 'p', 's']:
                user_move = {'r': ROCK, 'p': PAPER, 's': SCISSOR}[move]
                print(f"User Move: {user_move}")
                print(f"Computer's Move: {computer_move}")
                output = find_winner(user_move, computer_move)
                if output == 1:
                    print("User Won !!!")
                elif output == -1:
                    print("Computer Won !!!")
                else:
                    print("It's a Tie !!!")
                break
            else:
                print("Invalid input...please try again")
    elif choice == 'n':
        print("Exiting... Thanks for playing!")
        break
    else:
        print("Invalid input...please try again")
    print()
