def printboard(board):
  for i in range(3):
    for j in range(3):
      print(board[i*3 + j], end=' ')
    print()
     

def check_win(board,player):
  win_cond=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  for com in win_cond:
    if board[com[0]]==player and board[com[1]]==player and board[com[2]]==player:
      return True
  return False
     

def is_bord_full(board):
  for space in board:
    if space!='X' and space!='O':
      return False
  return True
     

def main():
  board = [str(i) for i in range(1, 10)]
  player1 = 'X'
  player2 = 'O'
  game_over = False
  current_player = player1

  while not game_over:
    printboard(board)
    try:
      move = int(input(f"Player {current_player}, enter your choice (1-9): ")) - 1

      if not (0 <= move <= 8):
        print("Invalid move. Please enter a number between 1 and 9.")
        continue

      if board[move] in ['X', 'O']:
        print("This position is already taken. Please choose another.")
        continue

      board[move] = current_player

      if check_win(board, current_player):
        printboard(board)
        print(f"Player {current_player} won!")
        game_over = True
      elif is_bord_full(board):
        printboard(board)
        print("It's a tie!")
        game_over = True
      else:

        current_player = player2 if current_player == player1 else player1

    except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == '__main__':
  main()

OUTPUT:

1 2 3 
4 5 6 
7 8 9 
Player X, enter your choice (1-9): 3
1 2 X 
4 5 6 
7 8 9 
Player O, enter your choice (1-9): 2
1 O X 
4 5 6 
7 8 9 
Player X, enter your choice (1-9): 4
1 O X 
X 5 6 
7 8 9 
Player O, enter your choice (1-9): 5
1 O X 
X O 6 
7 8 9 
Player X, enter your choice (1-9): 9
1 O X 
X O 6 
7 8 X 
Player O, enter your choice (1-9): 6
1 O X 
X O O 
7 8 X 
Player X, enter your choice (1-9): 1
X O X 
X O O 
7 8 X 
Player O, enter your choice (1-9): 8
X O X 
X O O 
7 O X 
Player O won!
