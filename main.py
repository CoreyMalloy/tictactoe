import random

def make_board(board):
   for row in board:
      print("|".join(row))
      print("-+-+-")

def bot_move(board, player):
  rn = random.randint(1, 9)
  while(board[str(rn)] != ' '):
    rn = random.randint(1, 9)
    print(rn)
  board[str(rn)] = player
  check_winner(player, board)

def check_winner(player, board):
  #Horizontal
  for i in range(1, 10, 3):
    if (board[str(i)] != ' ') and (board[str(i)] == board[str(i + 1)] == board[str(i + 2)]):
      print(player, "You win")
      make_board([list(board.values())[i:i + 3] for i in range(0, 9, 3)])
      exit()
  
  #Vertical
  for i in range(1,4):
    if (board[str(i)] != ' ') and (board[str(i)] == board[str(i + 3)] == board[str(i + 6)]):
      make_board([list(board.values())[i:i + 3] for i in range(0, 9, 3)])
      print(player, "You win!!")
      exit()

  #diagonal
  if (board[str(i)] != ' ') and (board['1'] == board['5'] == board['9']):
    make_board([list(board.values())[i:i + 3] for i in range(0, 9, 3)])
    print(player, "You win!!")
    exit()
  if (board[str(i)] != ' ') and (board['3'] == board['5'] == board['7']):
    make_board([list(board.values())[i:i + 3] for i in range(0, 9, 3)])
    print(player, "You win!!")
    exit()

def check_full(board):
  count = 0
  for i in range(1,10):
    if board[str(i)] != ' ':
        count = count + 1;
  if count == 9:
     print("The Board is full, No one wins!!!!!")
     exit()

def play_tic_tac_toe():
    board = {'1': ' ', '2': ' ', '3': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '7': ' ', '8': ' ', '9': ' '}
    
    Answer = ""
    
    while(Answer != "no"):
      starter = random.randint(1, 2)

      mode = input("Choose whether you want to play against a person(p) or a bot(b)? ")

      if starter == 1:
        current_player = 'X'
        print("X is starting")
      if starter == 2:
        current_player = 'O'
        print("O is starting")
    
      if mode == 'p':
        while(True):
          make_board([list(board.values())[i:i + 3] for i in range(0, 9, 3)])
          square = input("Please Enter a Digit 1-9: ")
      
          while(square == '' or board[square] !=  ' '):
            square = input("please re-pick your square: ")
      
          board[square] = current_player

          check_winner(current_player, board)

          check_full(board)

          if current_player == 'X':
            current_player = 'O'
          else:
            current_player = 'X'
          print("The current Player is ", current_player)
      Answer = input("Do you wish to play another round? (yes or no): ")
      if mode == 'b':
        while(True):
          make_board([list(board.values())[i:i + 3] for i in range(0, 9, 3)])
          if current_player == 'O':
            bot_move(board, current_player)
            current_player = 'X'
            print("The current Player is ", current_player)
          else:
            square = input("Please Enter a Digit 1-9: ")
      
            while(square == '' or board[square] !=  ' '):
              square = input("please re-pick your square: ")
      
            board[square] = current_player

            check_winner(current_player, board)

            check_full(board)

            if current_player == 'X':
              current_player = 'O'
            else:
              current_player = 'X'

            print("The current Player is ", current_player)
      Answer = input("Do you wish to play another round? (yes or no): ")

if __name__ == "__main__":
  play_tic_tac_toe()
  print("hey")