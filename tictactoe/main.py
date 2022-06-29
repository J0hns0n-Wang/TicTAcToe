import numpy as np

class TicTacToe:
    
    def __init__(self):
        board = [["-" for num in range(3)] for num in range(3)]
        self.board = np.array(board)
        
    
    def get_board(self):
        for i in self.board:
            for j in i:
                print(j, end=" ")
            print()
        
        
    def play(self):
       self.get_board()
       while True: 
        #    self.get_board()
           player_row = int(input("Rows? (Only from 0 - 2)"))
           player_col = int(input("Col? (Only from 0 - 2)"))
           letter = "X"
           self.board[player_row][player_col] = letter
           self.get_board()
           if "-" not in self.board:
               return False

              
        
if __name__ == "__main__":
    tictactoe_game = TicTacToe()
    tictactoe_game.play()