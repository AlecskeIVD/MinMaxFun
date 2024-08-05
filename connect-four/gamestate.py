RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'


class Gamestate:
    def __init__(self, board=None, turn=1):
        if board is None:
            board = [
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
            ]
        else:
            board = [row.copy() for row in board]
        self.board = board
        self.turn = turn

    def is_terminal(self):
        return self.turn > len(self.board)*len(self.board[0]) or (self.utility() != 0)

    def to_string(self):
        output = ""
        for row in self.board:
            for position in row:
                output += position
        return output

    def copy(self):
        return Gamestate(self.board, self.turn)

    def make_move(self, j) -> bool:
        if j > 7 or j < 0:
            return False
        if self.board[0][j] != "-":
            return False
        char = "r" if self.turn % 2 == 1 else "y"
        for i in range(len(self.board)-1, -1, -1):
            if self.board[i][j] == "-":
                self.board[i][j] = char
                break
        self.turn += 1
        return True

    def red_wins(self):
        return self.utility() == 1

    def yellow_wins(self):
        return self.utility() == -1

    def utility(self):
        if self.turn <= 7:
            # Not enough turns to win
            return 0
        # Check horizontal locations for win
        for row in range(len(self.board)):
            for col in range(len(self.board[0]) - 3):
                if self.board[row][col] != '-' and self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] == \
                        self.board[row][col + 3]:
                    return 1 if self.board[row][col] == "r" else -1

        # Check vertical locations for win
        for row in range(len(self.board) - 3):
            for col in range(len(self.board[0])):
                if self.board[row][col] != '-' and self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == \
                        self.board[row + 3][col]:
                    return 1 if self.board[row][col] == "r" else -1

        # Check positively sloped diagonals
        for row in range(len(self.board) - 3):
            for col in range(len(self.board[0]) - 3):
                if self.board[row][col] != '-' and self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == \
                        self.board[row + 3][col + 3]:
                    return 1 if self.board[row][col] == "r" else -1

        # Check negatively sloped diagonals
        for row in range(3, len(self.board)):
            for col in range(len(self.board[0]) - 3):
                if self.board[row][col] != '-' and self.board[row][col] == self.board[row - 1][col + 1] == self.board[row - 2][col + 2] == \
                        self.board[row - 3][col + 3]:
                    return 1 if self.board[row][col] == "r" else -1

        return 0  # No winner

    def draw(self):
        print(" ---"*len(self.board[0]) + " ")
        for row in self.board:
            print("|", end="")
            for char in row:
                print(" ", end="")
                if char == "-":
                    print(" ", end="")
                elif char == "r":
                    print(f"{RED}0{RESET}", end="")
                else:
                    print(f"{YELLOW}0{RESET}", end="")
                print(" |", end="")
            print("")
            print(" ---"*len(self.board[0]) + " ")

    def random(self):
        pass

    def pc(self):
        pass
