def woods_adventure() -> None:
    print("(Crumbling noise) You are in the woods!")
    print("One lampe in hanging on the tree.\n But you can see very little.")
    player_input = input("Pull out your phone? (yes/no): ")
    if player_input == "yes":
        print("[Phone].")
        player_input = input("Turn on flashlight? (yes/no): ")
        if player_input == "yes":
            print("[Flashlight].")
            print("Phone battery: 89%")
            player_input = input("Walk forward, backward or left? (forward/backward/left): ")
            if player_input == "forward":
                print("[Waling forward].")
                print("[Spoted a bag].")
                player_input = input("Open the bag? (yes/no): ")
                if player_input == "yes":
                    print("[Bag].")
                    print("[Bag inventory:\n 1x Water bottle\n 1x Snack\n 1x Short knife\n 1x Flashlight battery\n 1x Rope]")
                    print("[Spoted a bannner].")
                    player_input = input("Read the banner? (yes/no): ")
                    if player_input == "yes":
                        print("[Banner].")
                        print("[There is a map on it.]")
                        player_input = input("Take the map? (yes/no): ")
                        if player_input == "yes":
                            print("[Map].")
                            print("You have taken the map.")
                            print("Map:\n 1. Bear Zone (Forward)\n 2. Shope (Left)\n 3. Train Station (Right)")
                            print("Player speaks: Walking forward is foolish, I should go to the shop or station, whrer to go first?")
                            player_input = input("Go to the shop or station? (shop/station): ")
                            if player_input == "shop":
                                print("You are in the shop!")
                            else:
                                print("You are in the station!")
                        else:
                            print("You are in the woods!")
                            player_input = input("Walk forward, backward or left? (forward/backward/left): ")
                            if player_input == "forward":
                                print("[A bear saw you!]")
                                print("[Bear is running towards you!]")
                                player_input = input("Run or fight? (run/fight): ")
                                if player_input == "run":
                                    print("[Running].")
                                    print("[You are lost in the woods!]")
                                else:
                                    print("[Fighting].")
                                    print("[You killed the bear with the shortgun!]")
                                    print("[You are lost in the woods!]")
                    else:
                        print("You are in the woods!")
                        player_input = input("Walk forward, backward or left? (forward/backward/left): ")
                        if player_input == "forward":
                            print("[A bear saw you!]")
                            print("[Bear is running towards you!]")
                            player_input = input("Run or fight? (run/fight): ")
                            if player_input == "run":
                                print("[Running].")
                                print("[You are dead!]")
                            else:
                                print("[Fighting].")
                                print("[You are dead!]")
                else:
                    print("[Walking forward].")
                    print("[A bear saw you!]")
                    print("[Bear is running towards you!]")
                    player_input = input("Run or fight? (run/fight): ")
                    if player_input == "run":
                        print("[Running].")
                        print("[You are dead!]")
                    else:
                        print("[Fighting].")
                        print("[You are dead!]")
            elif player_input == "backward":
                pass # add code here
            else:
                pass # add code here
        else:
            print("You are in the dark.")
            player_input = input("Walk forward, backward or left? (forward/backward/left): ")
            if player_input == "forward":
                print("[Walking forward].")
                print("[Heard strange noise].")
                player_input = input("Walk forward or backward? (forward/backward): ")
                if player_input == "forward":
                    print("[Walking forward].")
                    print("[You are dead!]")
                else:
                    print("[Walking backward].")
                    print("You are in the same sopt.")
            elif player_input == "backward":
                print("[Walking backward].")
                print("You trigered a trap!")
                print("You are dead!")
            else:
                print("Lost in the woods!")
    else:
        print("You are in the dark.")
        player_input = input("Walk forward, backward or left? (forward/backward/left): ")
        if player_input == "forward":
            print("[Walking forward].")
            print("[Heard strange noise].")
            player_input = input("Walk forward or backward? (forward/backward): ")
            if player_input == "forward":
                print("[Walking forward].")
                print("[You are dead!]")
            else:
                print("[Walking backward].")
                print("You are in the same sopt.")
        elif player_input == "backward":
            print("[Walking backward].")
            print("You trigered a trap!")
            print("You are dead!")
        else:
            print("Lost in the woods!")
    

    

def castle_adventure() -> None:
    print("You are in the castle!")

def space_adventure() -> None:
    print("You are in space!")