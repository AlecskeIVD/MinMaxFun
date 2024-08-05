from gamestate import Gamestate


def main():
    print("Welcome to this game of tic-tac-toe!")
    print("The objective of this game is to get 4 pieces of your colour in a row.")
    print("You can make a move by entering your chosen column, make a random move by typing random")
    print("or make a perfect move by typing pc.")
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
        else:
            i = int(command.strip())
            if not gs.make_move(i):
                print("That is an invalid column")
            else:
                gs.draw()
        if gs.red_wins():
            print("Player 1 has won!")
        elif gs.yellow_wins():
            print("Player 2 has won!")
        elif gs.turn >= 10:
            print("Game has ended in a draw")


if __name__ == "__main__":
    main()
