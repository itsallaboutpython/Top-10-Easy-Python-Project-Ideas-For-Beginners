board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
X = 'X'
O = 'O'

def displayBoard():
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(" ----------")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(" ----------")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")

def updateBoard(character, position):
    row = (position-1)//3
    column = (position-1)%3
    board[row][column] = character

def check_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return 1
        elif board[0][i] == board[1][i] == board[2][i]:
            return 1
    
    if board[0][2] == board[1][1] == board[2][0]:
        return 1
    elif board[0][0] == board[1][1] == board[2][2]:
        return 1
    return 0

def check_position(position):
    row = (position-1)//3
    column = (position-1)%3
    if board[row][column] == X or board[row][column] == O:
        return 0
    return 1

print("===== Welcome to Tic Tac Toe Game =====")
counter = 0
while 1:
    if counter % 2 == 0:
        displayBoard()
        while 1:
            choice = int(input(f"Player {(counter%2)+1}, enter your position ('{X}'): "))
            if choice < 1 or choice > 9:
                print('Invalid input...please try again.')
            if check_position(choice):
                updateBoard(X, choice)
                if check_win():
                    print(f"Conguratulations !!! Player {(counter%2)+1} won !!!")
                    exit(0)
                else:
                    counter += 1
                    break
            else:
                print(f"Position {choice} is already occupied. Choose another position.")
        if counter == 9:
            print("The match ended with a draw !!! Better luck next time")
            exit(0)
    else:
        displayBoard()
        while 1:
            choice = int(input(f"Player {(counter%2)+1}, enter your position ('{O}'): "))
            if choice < 1 or choice > 9:
                print('Invalid input...please try again.')
            if check_position(choice):
                updateBoard(O, choice)
                if check_win():
                    print(f"Conguratulations !!! Player {(counter%2)+1} won !!!")
                    exit(0)
                else:
                    counter += 1
                    break
            else:
                print(f"Position {choice} is already occupied. Choose another position.")
    print()