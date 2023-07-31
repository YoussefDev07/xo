from colorama import Fore, Style

# create game board

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

# function to print game board

def print_board(board):
    for row in board:
        print(Fore.BLACK + " | ".join(row))
        print("-" * 9 + Fore.RESET)

# function to move x, o

def move():
    while True:
        row = int(input("Enter the row number (1, 2, 3): ")) - 1
        column = int(input("Enter the column number (1, 2 ,3): ")) - 1

        if 0 <= row <= 2 and 0 <= column <= 2 and board[row][column] == "":
            return row, column
        else:
            print(Fore.RED + "Enter a valid or unreserved row and column number." + Fore.RESET)

# function to check for win

def win(player):
    # check rows
    
    for row in board:
        if all(area == player for area in row):
            return True
        
    # check columns

    for column in range(3):
        if all(board[row][column] == player for row in range(3)):
            return True
        
    # check areas

    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

# function to check to tie

def tie():
    return all(board[row][column] != "" for row in range(3) for column in range(3))

# game

def xo():
    players = ("X", "O")
    index = 0

    while True:
        print_board(board)

        player = players[index]
        print(Fore.LIGHTCYAN_EX + "Player {}{}{} turn".format(Style.BRIGHT, player, Style.NORMAL) + Fore.RESET)

        row, column = move()
        board[row][column] = player

        if win(player):
            print_board(board)
            print(Fore.GREEN + "Player {}{}{} wins!".format(Style.BRIGHT, player, Style.NORMAL) + Fore.RESET)
            break
        
        if tie():
            print_board(board)
            print(Fore.YELLOW + "Tie." + Fore.RESET)
            break
        
        index = (index + 1) % 2

# start game

xo()