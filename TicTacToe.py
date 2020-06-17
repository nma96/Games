import random


def display_board(board):

    print('\n' + board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3] + '\n')


def player_input():
    player1 = ''
    player2 = ''
    while player1 != 'X' and player1 != 'O':
        player1 = input('Player 1: Choose either "X" or "O": ').upper()

    if player1 == 'X':
        player2 = 'O'
    elif player1 == 'O':
        player2 = 'X'

    return (player1, player2)


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark))


def choose_first():
    randomInt = random.randint(1, 2)
    if randomInt == 1:
        return 'Player 1'
    elif randomInt == 2:
        return 'Player 2'


def space_check(board, position):

    return board[position] == ' '


def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False
    else:
        return True  # True means board is full.


def player_choice(board, turn):

    nextPosition = 0
    while nextPosition not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, nextPosition):
        nextPosition = int(
            input('What is your position {}(1-9): '.format(turn)))
    return nextPosition


def replay():

    choice = input("Play again? Y or N: ").upper()
    return choice == 'Y'


print('Welcome to Tic Tac Toe!\n')

while True:
    # Set the game up here
    myBoard = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print('\n' + turn + ' will go first')
    print("Let's begin:")

    while True:
        # Player1 turn
        if turn == 'Player 1':
            display_board(myBoard)
            position = player_choice(myBoard, turn)
            place_marker(myBoard, player1_marker, position)

            # check for win
            if win_check(myBoard, player1_marker):
                display_board(myBoard)
                print('\n\nPLAYER 1 HAS WON!!')
                break
            # Check for tie
            elif full_board_check(myBoard):
                display_board(myBoard)
                print('\n\nThe game is a tie!')
                break
            # Change turn to other player
            else:
                turn = 'Player 2'

        # Player2's turn.
        elif turn == 'Player 2':
            display_board(myBoard)
            position = player_choice(myBoard, turn)
            place_marker(myBoard, player2_marker, position)

            # check for win
            if win_check(myBoard, player2_marker):
                display_board(myBoard)
                print('\n\nPLAYER 2 HAS WON!!')
                break
            # Check for tie
            elif full_board_check(myBoard):
                display_board(myBoard)
                print('The game is a tie!')
                break
            # Change turn to other player
            else:
                turn = 'Player 1'

    if not replay():
        break
