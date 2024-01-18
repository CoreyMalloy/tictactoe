class Board():
  array_board = [
                [0,0,0],
                [0,0,0],
                [0,"O",0]
              ]

  winner = None

  def __init__(self):
    print("Board Made")

  def selection(self, x, y, player) -> bool:
    if self.array_board[x][y] == 0:
      self.array_board[x][y] = player
      return True
    return False
  
  def check_win(self) -> bool:
    for x in self.array_board:
      if x[1] == x[0] and x[0] == x[2]:
        self.set_Winner(x[0])
        return True
      
  def set_Winner(self, player) -> str: 
    self.winner = player
    
  def __str__(self) -> str:
    return str(self.array_board)
  
class Game:

  ExampleBoard = Board()

  while True:
    x = input("enter a x val")
    y = input("enter a y val")
    
    if ExampleBoard.selection(int(x) , int(y), "X"):
      break
    else:
      print("invalid position")


  print(ExampleBoard)


if __name__ == "__main__":
  runGame = Game()