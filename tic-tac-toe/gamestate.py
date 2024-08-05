import random


class Gamestate:
    def __init__(self, board=None, lookup_table=None, turn=1):
        if lookup_table is None:
            lookup_table = {}
        if board is None:
            board = [
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "],
            ]
        else:
            board = [row.copy() for row in board]
        self.board = board
        self.turn = turn

        # It will be useful for different gamestates to share a lookup_table since this may lead to a quicker evaluation
        self.lookup_table = lookup_table

    def is_terminal(self):
        return self.turn >= 10 or (self.utility() != 0)

    def to_string(self):
        output = ""
        for row in self.board:
            for position in row:
                output += position
        return output

    def copy(self):
        return Gamestate(self.board, self.lookup_table, self.turn)

    def make_move(self, i, j) -> bool:
        if self.board[i][j] != " ":
            return False
        char = "x" if self.turn % 2 == 1 else "o"
        self.board[i][j] = char
        self.turn += 1
        return True

    def utility(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                if self.board[i][0] == "x":
                    # X WON
                    return 1
                elif self.board[i][0] == "o":
                    # O WON
                    return -1
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                if self.board[0][i] == "x":
                    # X WON
                    return 1
                elif self.board[0][i] == "o":
                    # O WON
                    return -1

        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            if self.board[0][0] == "x":
                # X WON
                return 1
            elif self.board[0][0] == "o":
                # O WON
                return -1

        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[0][2] == "x":
                # X WON
                return 1
            elif self.board[0][2] == "o":
                # O WON
                return -1
        return 0

    def draw(self):
        print(" ---"*3 + " ")
        for row in self.board:
            print("|", end="")
            for char in row:
                print(" "+char + " |",end="")
            print("")
            print(" ---"*3 + " ")

    def random(self):
        i, j = random.randint(0, 2), random.randint(0, 2)
        while not self.make_move(i, j):
            i, j = random.randint(0, 2), random.randint(0, 2)

    def pc(self):
        pass

    def x_wins(self):
        return self.utility() == 1

    def o_wins(self):
        return self.utility() == -1
