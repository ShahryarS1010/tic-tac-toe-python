# Random is used to decide which player goes first.
import random

# Assume the board is filled, if any space is empty (denoted with -) then return false, otherwise return true and the game is a draw.
def is_board_filled(board):
    board_filled = True
    # i holds the row and j holds the column.
    # len(board) = 3 and len(board[i]) = 3
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "-":
                # There is an empty space.
                board_filled = False
    return board_filled

# The player wins the game if they get three of their symbols in a row (horizontally, vertically, or diagonally).
# Return true if the player has won the game, otherwise return false if player has not.
def has_player_won(board, symbol):
    won = False
    # len(board) = 3
    for i in range(len(board)):
        # i holds the row
        # We will check if the player has three of their symbol in a row horizontally.
        if board[i][0] == symbol and board[i][1] == symbol and board[i][2] == symbol:
            won = True
        # i holds the column
        # We will check if the player has three of their symbol in a row vertically.
        if board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
            won = True
    # We will check if the player has three of their symbol in a row diagonally on the two diagonals.
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        won = True
    if board[2][0] == symbol and board[1][1] == symbol and board[0][2] == symbol:
        won = True

    return won

# Give a hint in the form of telling a player if they can put their symbol to immediately win the game or stop the opponent from immediately winning the game, otherwise no hint provided.
# If a hint is available break out of the loop to return that hint to the player.
def hint(board, player_symbol, opponent_symbol):
    hint = "No hint available."

    # len(board) = 3
    for i in range(len(board)):
        # Check to see if the player can win by putting their symbol to match 3 in a row horizontally.
        # i holds the row.
        if board[i][0] == player_symbol and board[i][1] == player_symbol and board[i][2] == "-":
            hint = "Put the " + player_symbol + " on Row " + str(i) + " and Column 2 to win the Game."
            break
        if board[i][0] == player_symbol and board[i][2] == player_symbol and board[i][1] == "-":
            hint = "Put the " + player_symbol + " on Row " + str(i) + " and Column 1 to win the Game."
            break
        if board[i][1] == player_symbol and board[i][2] == player_symbol and board[i][0] == "-":
            hint = "Put the " + player_symbol + " on Row " + str(i) + " and Column 0 to win the Game."
            break
        # Check to see if the player can win by putting their symbol to match 3 in a row vertically.
        # i holds the column.
        if board[0][i] == player_symbol and board[1][i] == player_symbol and board[2][i] == "-":
            hint = "Put the " + player_symbol + " on Row 2 and Column " + str(i) + " to win the Game."
            break
        if board[0][i] == player_symbol and board[2][i] == player_symbol and board[1][i] == "-":
            hint = "Put the " + player_symbol + " on Row 1 and Column " + str(i) + " to win the Game."
            break
        if board[1][i] == player_symbol and board[2][i] == player_symbol and board[0][i] == "-":
            hint = "Put the " + player_symbol + " on Row 0 and Column " + str(i) + " to win the Game."
            break

    # If a hint is available for the player to win the game then no need to check further.
    if hint[0] == "N":
        # Check to see if the player can win by putting their symbol to match 3 in a row diagonally.
        if board[0][0] == player_symbol and board[1][1] == player_symbol and board[2][2] == "-":
            hint = "Put the " + player_symbol + " on Row 2 and Column 2 to win the Game."
        elif board[0][0] == player_symbol and board[2][2] == player_symbol and board[1][1] == "-":
            hint = "Put the " + player_symbol + " on Row 1 and Column 1 to win the Game."
        elif board[1][1] == player_symbol and board[2][2] == player_symbol and board[0][0] == "-":
            hint = "Put the " + player_symbol + " on Row 0 and Column 0 to win the Game."
        elif board[2][0] == player_symbol and board[1][1] == player_symbol and board[0][2] == "-":
            hint = "Put the " + player_symbol + " on Row 0 and Column 2 to win the Game."
        elif board[2][0] == player_symbol and board[0][2] == player_symbol and board[1][1] == "-":
            hint = "Put the " + player_symbol + " on Row 1 and Column 1 to win the Game."
        elif board[1][1] == player_symbol and board[0][2] == player_symbol and board[2][0] == "-":
            hint = "Put the " + player_symbol + " on Row 2 and Column 0 to win the Game."

    # If a hint is available for the player to win the game then no need to stop the opponent from winning the game.
    # The first character of hint being N means "No hint available".
    if hint[0] == "N":
        # len(board) = 3
        for i in range(len(board)):
            # Check to see if the player can stop their opponent from winning by them putting their symbol to match 3 in a row horizontally.
            # i holds the row.
            if board[i][0] == opponent_symbol and board[i][1] == opponent_symbol and board[i][2] == "-":
                hint = "Put the " + player_symbol + " on Row " + str(i) + " and Column 2 to avoid losing the Game."
                break
            if board[i][0] == opponent_symbol and board[i][2] == opponent_symbol and board[i][1] == "-":
                hint = "Put the " + player_symbol + " on Row " + str(i) + " and Column 1 to avoid losing the Game."
                break
            if board[i][1] == opponent_symbol and board[i][2] == opponent_symbol and board[i][0] == "-":
                hint = "Put the " + player_symbol + " on Row " + str(i) + " and Column 0 to avoid losing the Game."
                break
            # Check to see if the player can stop their opponent from winning by them putting their symbol to match 3 in a row vertically.
            # i holds the column.
            if board[0][i] == opponent_symbol and board[1][i] == opponent_symbol and board[2][i] == "-":
                hint = "Put the " + player_symbol + " on Row 2 and Column " + str(i) + " to avoid losing the Game."
                break
            if board[0][i] == opponent_symbol and board[2][i] == opponent_symbol and board[1][i] == "-":
                hint = "Put the " + player_symbol + " on Row 1 and Column " + str(i) + " to avoid losing the Game."
                break
            if board[1][i] == opponent_symbol and board[2][i] == opponent_symbol and board[0][i] == "-":
                hint = "Put the " + player_symbol + " on Row 0 and Column " + str(i) + " to avoid losing the Game."
                break

        # If a hint is available for the player to stop the opponent from winning the game then no need to check further.
        if hint[0] == "N":
            # Check to see if the player can stop their opponent from winning by them putting their symbol to match 3 in a row diagonally.
            if board[0][0] == opponent_symbol and board[1][1] == opponent_symbol and board[2][2] == "-":
                hint = "Put the " + player_symbol + " on Row 2 and Column 2 to avoid losing the Game."

            elif board[0][0] == opponent_symbol and board[2][2] == opponent_symbol and board[1][1] == "-":
                hint = "Put the " + player_symbol + " on Row 1 and Column 1 to avoid losing the Game."

            elif board[1][1] == opponent_symbol and board[2][2] == opponent_symbol and board[0][0] == "-":
                hint = "Put the " + player_symbol + " on Row 0 and Column 0 to avoid losing the Game."

            elif board[2][0] == opponent_symbol and board[1][1] == opponent_symbol and board[0][2] == "-":
                hint = "Put the " + player_symbol + " on Row 0 and Column 2 to avoid losing the Game."

            elif board[2][0] == opponent_symbol and board[0][2] == opponent_symbol and board[1][1] == "-":
                hint = "Put the " + player_symbol + " on Row 1 and Column 1 to avoid losing the Game."

            elif board[1][1] == opponent_symbol and board[0][2] == opponent_symbol and board[2][0] == "-":
                hint = "Put the " + player_symbol + " on Row 2 and Column 0 to avoid losing the Game."

    return hint

# Display the board before each player's turn and once the game is completed.
def display_board(board):
    # len(board) = 3
    for i in range(len(board)):
        # The symbol | draws the columns.
        print(board[i][0], "|", board[i][1], "|", board[i][2])
        # The - symbols draws the rows but not below the board.
        if (i < 2):
            print("----------")

# Start the Tic-Tac-Toe Game.
def tic_tac_toe(board):
    # Title.
    print("Tic-Tac-Toe")

    # Get the names of the two players.
    player_one = input("Enter the name of Player 1: ")

    player_two = input("Enter the name of Player 2: ")

    # Shuffle to decide which player goes first.
    shuffle = [0,1]

    random.shuffle(shuffle)

    # This determines who goes first, 0 means the first player goes first and 1 means the second player goes first.
    player_number = shuffle[0]

    if player_number == 0:
        print("Player 1 goes first")

    else:
        print("Player 2 goes first")

    # The Game will run through an infinite loop until there's a winner or the game is drawn.
    while True:
        # Display the board before each player's turn.
        display_board(board)

        # 0 is associated with player 1 and 1 is associated with player 2
        if player_number == 0:
            # Player 1's symbol is X
            print("Player 1's turn (X)")
            # Ask the player which row they want to put their symbol in or to ask for a hint.
            row_choice = int(input("Enter Row Number: (0 for top, 1 for middle, 2 for bottom, 3 for hint)"))

            # Get a hint if available.
            if row_choice == 3:
                print(hint(board, "X", "O"))
                continue

            # Validate if the row number exists, if not then ask the player to input again.
            if row_choice > 3 or row_choice < 0:
                print("Error, Invalid Choice")
                # Continue to go back to the move choice.
                continue
            # Ask the player which column they want to put their symbol in or to go back and select a different row.
            column_choice = int(input("Enter Column Number: (0 for left, 1 for middle, 2 for right, 3 to go back)"))

            # This goes back to the row choice.
            if column_choice == 3:
                continue

            # Validate if the column number exists, if not then ask the player to input the row and column again.
            if column_choice > 3 or column_choice < 0:
                print("Error, Invalid Choice")
                continue

            # If the space is already occupied then the move is illegal so the player is asked to input the row and column again.
            if board[row_choice][column_choice] != "-":
                print("Illegal move, that space is already occupied")
                continue

            # Put Player's 1 X on the selected spot
            board[row_choice][column_choice] = "X"

            # Check if Player 1 has won
            won = has_player_won(board, "X")

            # If Player 1 has won then display the victory line and the final position of the board and end the game.
            if won == True:
               print("Player 1 Wins")
               display_board(board)
               break

            # Check if the board is filled, if so then the game is a draw.
            draw = is_board_filled(board)

            # Print the drawn line and the final position of the board and end the game.
            if draw == True:
                print("The Game is a Draw")
                display_board(board)
                break


        else:
            # Player 2's symbol is O
            print("Player 2's turn (O)")

            # Ask the player which row they want to put their symbol in or to ask for a hint.
            row_choice = int(input("Enter Row Number: (0 for top, 1 for middle, 2 for bottom, 3 for hint)"))

            # Get a hint if available.
            if row_choice == 3:
                print(hint(board, "O", "X"))
                continue

            # Validate if the row number exists, if not then ask the player to input again.
            if row_choice > 3 or row_choice < 0:
                print("Error, Invalid Choice")
                continue

            # Ask the player which column they want to put their symbol in or to go back and select a different row.
            column_choice = int(input("Enter Column Number: (0 for left, 1 for middle, 2 for right, 3 to go back)"))

            # This goes back to the row choice.
            if column_choice == 3:
                continue

            # Validate if the column number exists, if not then ask the player to input the row and column again.
            if column_choice > 3 or column_choice < 0:
                print("Error, Invalid Choice")
                continue

            # If the space is already occupied then the move is illegal so the player is asked to input the row and column again.
            if board[row_choice][column_choice] != "-":
                print("Illegal move, that space is already occupied")
                continue

            # Put Player's 2 O on the selected spot
            board[row_choice][column_choice] = "O"

            # Check if Player 2 has won
            won = has_player_won(board, "O")

            # If Player 2 has won then display the victory line and the final position of the board and end the game.
            if won == True:
                print("Player 2 Wins")
                display_board(board)
                break

            # Check if the board is filled, if so then the game is a draw.
            draw = is_board_filled(board)

            # Print the drawn line and the final position of the board and end the game.
            if draw == True:
                print("The Game is a Draw")
                display_board(board)
                break

        # Switch Turns
        if player_number == 0:
            player_number = 1

        else:
            player_number = 0

# Create Board and fill the spots with the empty symbol -.
board = [["-","-","-"],["-","-","-"],["-","-","-"]]

# Start the Game.
tic_tac_toe(board)


