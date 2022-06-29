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
                    other_letter = "O"
                    self.board[player_row - 1][player_col - 1] = other_letter
            else:
                print("This space has already been taken")
        #    letter = "X"
        #    self.board[player_row - 1][player_col - 1] = letter
            self.get_board()
        #    print(x_count)
            if "-" not in self.board:
                return False


if __name__ == "__main__":
    tictactoe_game = TicTacToe()
    tictactoe_game.play()
