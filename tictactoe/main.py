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
            
    # def win(self, letter):
        
    #     #check col
    #     if self.board[0][0] == self.board[0][1] == self.board[0][2]:
    #         print(f"Player {letter} won!")
            
            
            

    def play(self):
        self.get_board()
        while True:
            #    self.get_board()
            player_row = int(input("Row? (Only from 1 - 3)"))
            player_col = int(input("Col? (Only from 1 - 3)"))
            x_count = np.count_nonzero(self.board == "X")
            o_count = np.count_nonzero(self.board == "O")
            dash_count = np.count_nonzero(self.board == "-")
            if self.board[player_row - 1][player_col - 1] == "-":
                if o_count >= x_count or dash_count == 9:
                    letter = "X"
                self.board[player_row - 1][player_col - 1] = letter
                if x_count > o_count:
                    letter = "O"
                    self.board[player_row - 1][player_col - 1] = letter
            else:
                print("This space has already been taken")

            self.get_board()
            # self.win(letter)
            
            #check row
            if self.board[0][0] == self.board[0][1] == self.board[0][2] == letter:
                print(f"Player {letter} won!")
                return False
            elif self.board[1][0] == self.board[1][1] == self.board[1][2] == letter:
                print(f"Player {letter} won!")
                return False  
            elif self.board[2][0] == self.board[2][1] == self.board[2][2] == letter:
                print(f"Player {letter} won!")
                return False 
            
            
            #check col
            if self.board[0][0] == self.board[1][0] == self.board[2][0] == letter:
                print(f"Player {letter} won!")
                return False
            elif self.board[0][1] == self.board[1][1] == self.board[2][1] == letter:
                print(f"Player {letter} won!")
                return False  
            elif self.board[0][2] == self.board[1][2] == self.board[2][2] == letter:
                print(f"Player {letter} won!")
                return False 
            
            #check diagonal
            if self.board[0][0] == self.board[1][1] == self.board[2][2] == letter:
                print(f"Player {letter} won!")
                return False
            elif self.board[0][2] == self.board[1][1] == self.board[2][0] == letter:
                print(f"Player {letter} won!")
                return False     
        
            if "-" not in self.board:
                print("The game is a tie!")
                return False


if __name__ == "__main__":
    tictactoe_game = TicTacToe()
    tictactoe_game.play()
