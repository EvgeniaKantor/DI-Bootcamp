print('Welcome to TIC TAC TOE!\n')

def display_board(cell):
    """A Function to display the board"""
    board = (f"TIC TAC TOE\n"
             f"***************\n"
             f"*  {cell[1]} | {cell[2]} | {cell[3]}  *\n"
             f"* ---|---|--- *\n"
             f"*  {cell[4]} | {cell[5]} | {cell[6]}  *\n"
             f"* ---|---|--- *\n"
             f"*  {cell[7]} | {cell[8]} | {cell[9]}  *\n"
             f"***************\n")
    print(board)

def player_input(player, cell):
    """A function to get the position from the player"""
    while True:
        row = int(input(f"Player {player}, enter the number of the row (1-3): "))
        if row < 1 or row > 3:
            print("Invalid row selected, please pick another")
            continue  # Ask for input again
        column = int(input(f"Player {player}, enter the number of the column (1-3): "))
        if column < 1 or column > 3:
            print("Invalid column selected, please pick another")
            continue  # Ask for input again
        position = (row - 1) * 3 + column
        if cell[position] != 'X' and cell[position] != 'O':
            return position
        else:
            print("The position already taken, please pick another")

def check_win(board, marker):
    """A function that checks whether there is a winner or not"""
    winning_conditions = [
        {1, 2, 3}, {4, 5, 6}, {7, 8, 9},  # Rows
        {1, 4, 7}, {2, 5, 8}, {3, 6, 9},  # Columns
        {1, 5, 9}, {3, 5, 7}              # Diagonals
    ]
    for condition in winning_conditions:
        if condition.issubset({k for k, v in board.items() if v == marker}):
            return True
    return False

def play():
    """A function that calls all the functions created above"""
    cell = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    display_board(cell)
    for turn in range(9):
        player = 1 if turn % 2 == 0 else 2
        position = player_input(player, cell)
        marker = 'X' if player == 1 else 'O'
        cell[position] = marker
        display_board(cell)
        # Check if the current player has won
        if turn >= 4:  # The earliest a player can win is on their 5th turn
            if check_win(cell, marker):
                print(f"Player {player} wins!")
                break
    else:
        print("It's a tie!")

# Call the play function to start the game
play()
