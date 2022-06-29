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
        
        
        
if __name__ == "__main__":
    tictactoe_game = TicTacToe()
    tictactoe_game.play()