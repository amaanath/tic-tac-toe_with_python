#----- Global Variables -----

# Display Board
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

# If Game is still going
game_still_going_on = True

# Who Won ? or Tie ?
winner = None

# Who's turn is it ?
current_player = "X"

#Game Board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Handle Single Turn of a Player
def handle_turn(player):
    print(player + "'s Turn.")
    position = input("Choose a position from 1-9:" )

    valid = False
    while not valid:
        # This would keep on repeating the same response until you input
        # the correct answer, you could use an if statement but it breaks 
        # when you input an incorrect response the second time.

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a Number between 1-9.")

        position = int(position) - 1
        
        if board[position] == "-":
            valid = True
        else:
            print("You're Cheating. You can't go There")
    
    board[position] = player
    display_board()

# Check if game is over
def check_if_game_over():  
    check_if_win()
    check_if_tie()

# Check if a player is Won
def check_if_win():
    # Setup Global Variables
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return  

# Check Rows
def check_rows():
    # Setup Global Variables
    global game_still_going_on
    # Check if any row has the same value and is not empty
    row_1 = bool(board[0] == board[1] == board[2] !="-") 
    row_2 = board[3] == board[4] == board[5] !="-"
    row_3 = board[6] == board[7] == board[8] !="-"
    # Returns a Winner ( X or O )
    if row_1 or row_2 or row_3:
        game_still_going_on = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

# Check Columns
def check_columns():
    # Setup Global Variables
    global game_still_going_on
    # Check if any columns has the same value and is not empty
    column_1 = board[0] == board[3] == board[6] !="-"
    column_2 = board[1] == board[4] == board[7] !="-"
    column_3 = board[2] == board[5] == board[8] !="-"
    # Returns a Winner ( X or O )
    if column_1 or column_2 or column_3:
        game_still_going_on = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

# Check Diagonals
def check_diagonals():
    # Setup Global Variables
    global game_still_going_on
    # Check if any diagonals has the same value and is not empty
    diag_1 = board[0] == board[4] == board[8] !="-"
    diag_2 = board[2] == board[4] == board[6] !="-"
    # Returns a Winner ( X or O )
    if diag_1 or diag_2:
        game_still_going_on = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[6]
    return

# Check if a Game is Tie
def check_if_tie():
    global game_still_going_on
    if "-" not in board:
        game_still_going_on = False
    
    return

# Flip Player from Current Player to other Player
def flip_player():
    # Setup Global Variables
    global current_player
    # If current player is X change it to O
    if current_player == "X":
        current_player = "O"
    # And If current player is O change it to X
    elif current_player =="O":
        current_player = "X"
    return


# Play a game of Tic Tac Toe

def play_game():
    # This function displays the initial Game board
    display_board()
    #While game is still going on
    while game_still_going_on:
        # Handles Current Player
        handle_turn(current_player)
        # Checks if the Game is over
        check_if_game_over()
        # Flip Player from 
        flip_player()

    # The game has ended
    if winner=="X" or winner=="O":
        print(winner + " Won.")   
    elif winner==None:
        print("Tie.")


# By Calling this function you initiate the game.

play_game()