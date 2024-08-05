from gamestate import Gamestate


def main():
    print("Welcome to this game if tic-tac-toe!")
    print("The objective of this game is to get 3 x's in a row if you are Player 1 or 3 o's if you are Player 2")
    print("You can make a move by entering the coordinates of your preferable move as i, j or make a random move by typing random")
    print("or make a perfect move by typing pc")
    gs = Gamestate()
    gs.draw()
    while not gs.is_terminal():
        player = "1" if gs.turn % 2 == 1 else "2"
        command = input("Player "+player+"> ")
        if command.strip().lower() == "random":
            gs.random()
            gs.draw()
        elif command.strip().lower() == "pc":
            gs.pc()
            gs.draw()
        elif "," in command:
            ij = command.split(",")
            i, j = int(ij[0].strip()), int(ij[1].strip())
            if not gs.make_move(i, j):
                print("That is an invalid position")
            else:
                gs.draw()
        else:
            print("That is an invalid input")
        if gs.x_wins():
            print("Player 1 has won!")
        elif gs.o_wins():
            print("Player 2 has won!")
        elif gs.turn >= 10:
            print("Game has ended in a draw")


if __name__ == "__main__":
    main()
