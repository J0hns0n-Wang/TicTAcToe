import numpy as np

class TicTacToe:
    
    def __init__(self):
        self.board = ["-" for num in range(9)]
        # self.board = np.array(board)
        
    
    def get_board(self):
        for i in [self.board[j] * 3 for j in range(3)]:
            print( "|".join(i))
        
        
    def play(self):
       self.get_board()
    #    print(self.board)
        
        
if __name__ == "__main__":
    tictactoe_game = TicTacToe()
    tictactoe_game.play()