class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 5)

    def make_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        else:
            print("Invalid move. Try again.")
            return False

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ' or
                self.board[0][i] == self.board[1][i] == self.board[2][i] != ' '):
                return True

        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ' or
            self.board[0][2] == self.board[1][1] == self.board[2][0] != ' '):
            return True

        return False

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.print_board()

            row = int(input(f"Enter the row (0, 1, or 2) for {self.current_player}: "))
            col = int(input(f"Enter the column (0, 1, or 2) for {self.current_player}: "))

            if self.make_move(row, col):
                if self.check_winner():
                    self.print_board()
                    print(f"{self.current_player} wins!")
                    break
                elif self.is_board_full():
                    self.print_board()
                    print("It's a tie!")
                    break

                self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
