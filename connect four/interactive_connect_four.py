import connect_four as c


def main():
    game = c.ConnectFour()
    result = False
    print("\nThe board is: ")
    print(game)
    print("Please choose from the following commands:")
    print("A: Player add a piece to the game")
    print("U: Player wish to undo the previous step")
    print("Q: Player wish to quit the game")
    while result is not True:
        command = input("Please select command A, U, or Q: ")
        if command.lower() == "a":
            try:
                input_column = int(input("Player choose column from \
0 to 6: "))
                game.add_piece(input_column)
                print(game)
            except ValueError:
                print("Invalid input column.")
                continue
        elif command.lower() == "u":
            try:
                game.undo()
                print(game)
            except ValueError:
                print("There is no step to be undo.")
                continue 
        elif command.lower() == "q":
            break
        elif command.lower() not in ["a", "u", "q"]:
            print("Please enter a valid command.")
            continue
        result = game.is_game_over()
    print("\nThe final state of the board:")
    print(game)
    print("Game Over")
    if game.get_winner() is not None:
        print("Winner is " + game.win)
    else:
        print("Winner is None")


if __name__ == "__main__":
    main()
