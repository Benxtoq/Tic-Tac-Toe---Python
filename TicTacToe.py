# Global variables

# Game board
board  = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]

# If game is still going
game_still_going = True

# Who won? or tie?
winner = None

# who's turn is it?
current_player = "X"

# Play a game of tic tac toe 
def play_game():

   # Show the initial game board
   display_board()

   # Loop until the game is over
   while game_still_going:

      # Handle a single turn of the current player
      handle_turn(current_player)

      # Check if the game has ended
      check_if_game_over()

      # Flip to the other player
      flip_player()

      # The game has ended
   if winner == "X" or winner == "O":
      print(winner + " won.")
   else:
      print("Tie.")

# Display the game board
def display_board():
   print(board[0] + " | " + board[1] + " | " + board[2])
   print("---------")
   print(board[3] + " | " + board[4] + " | " + board[5])
   print("---------")
   print(board[6] + " | " + board[7] + " | " + board[8])

# Handle a single turn of a single player 
def handle_turn(player):

   # Get position from the player
   print(player + " 's turn.")
   
   # What the user inputs, make sure its a valid input, and the spot is open
   valid = False
   while not valid:
      position = input("Choose a position from 1-9: ")

      while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
         position = input("Invalid input. Choose a position from 1-9: ")

      # Get correct index in our board list
      position = int(position) - 1  # Convert to 0-indexed

      # Make sure the spot is available
      if board[position] == "-":
         valid = True
      else:
         print("You can't go there. Try again.")
   
   # Put the game piece on the board 
   board[position] = player
   
   #Show the game board after the turn
   display_board()

# Check if the game is over 
def check_if_game_over():
   check_for_winner()
   check_if_tie()

# Check for a winner 
def check_for_winner():

   # Set up global variables 
   global winner

   # check rows
   row_winner = check_rows()
   # check columns
   column_winner = check_columns()
   # check diagonals
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

def check_rows():
   # Set up global variables
   global game_still_going

   # Check if any of the rows have all the same value (and is not empty)
   row_1 = board[0] == board[1] == board[2] != "-"
   row_2 = board[3] == board[4] == board[5] != "-"
   row_3 = board[6] == board[7] == board[8] != "-"
   
   # If any row has all the same value, there is a winner
   if row_1 or row_2 or row_3:
      game_still_going = False

      # Return the winner (X or O)
      if row_1:
         return board[0]
      elif row_2:
         return board[3]
      elif row_3:
         return board[6]
   else: 
      return None
# Check the columns for a winner
def check_columns():
   # Set up global variables
   global game_still_going

   # Check if any of the column have all the same value (and is not empty)
   column_1 = board[0] == board[3] == board[6] != "-"
   column_2 = board[1] == board[4] == board[7] != "-"
   column_3 = board[2] == board[5] == board[8] != "-"

   # If any columns has all the same value, there is a winner
   if column_1 or column_2 or column_3:
      game_still_going = False

      # Return the winner (X or O)
      if column_1:
         return board[0]
      elif column_2:
         return board[1]
      elif column_3:
         return board[2]
   else:
      return None

def check_diagonals():
      # Set up global variables
   global game_still_going

   # Check if any of the diagonals have all the same value (and is not empty)
   diagonals_1 = board[0] == board[4] == board[8] != "-"
   diagonals_2 = board[6] == board[4] == board[2] != "-"

   # If any diagonal has all the same value, there is a winner
   if diagonals_1 or diagonals_2:
      game_still_going = False

      # Return the winner (X or O)
      if diagonals_1:
         return board[0]
      elif diagonals_2:
         return board[6]
   else:
      return None

# Flip the current player
def flip_player():
   # Global variables 
   global current_player

   # If current player is X, make it O, otherwise make it X
   if current_player == "X":
      current_player = "O"
   elif current_player == "O":
      current_player = "X"

# Check if the game is a tie
def check_if_tie():
   # Set up global variables
   global game_still_going
   # If board is full and there is no winner, it's a tie
   if "-" not in board:
      game_still_going = False
      return True
   # Else, there is no tie 
   else:
      return False

# Start the game
play_game()
