from game_mods import woods_adventure, castle_adventure, space_adventure
def game() -> None:
    print("Welcome to the game!")
    game_choice = input("1.Woods Adventure \n2.Castle Adventure? \n3.Space Adventure? \n4.Exit Game \nMake your choice(Enter 1 through 4 to choise a option): ")
    if game_choice == "1":
        woods_adventure()
    elif game_choice == "2":
        castle_adventure()
    elif game_choice == "3":
        space_adventure()
    elif game_choice == "4":
        print("See you  again!")


if __name__ == "__main__":
    game()