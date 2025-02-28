def woods_adventure() -> None:
    print("(Crumbling noise) You are in the woods!")
    print("One lamp is hanging on the tree.\nBut you can see very little.")
    player_input = input("Pull out your phone? (yes/no): ")
    if player_input == "yes":
        print("[Phone].")
        player_input = input("Turn on flashlight? (yes/no): ")
        if player_input == "yes":
            print("[Flashlight].")
            print("Phone battery: 89%")
            player_input = input("Walk forward, backward or left? (forward/backward/left): ")
            if player_input == "forward":
                print("[Walking forward].")
                print("[Spotted a bag].")
                player_input = input("Open the bag? (yes/no): ")
                if player_input == "yes":
                    print("[Bag].")
                    print("[Bag inventory:\n1x Water bottle\n1x Snack\n1x Short knife\n1x Flashlight battery\n1x Rope]")
                    print("[Spotted a banner].")
                    player_input = input("Read the banner? (yes/no): ")
                    if player_input == "yes":
                        print("[Banner].")
                        print("[There is a map on it.]")
                        player_input = input("Take the map? (yes/no): ")
                        if player_input == "yes":
                            print("[Map].")
                            print("You have taken the map.")
                            print("Map:\n1. Bear Zone (Forward)\n2. Shop (Left)\n3. Train Station (Right)")
                            player_input = input("Go to the shop or station? (shop/station): ")
                            if player_input == "shop":
                                print("You are in the shop!")
                                print("[There is an old broken cashbox.]")
                                player_input = input("Open the cashbox? (yes/no): ")
                                if player_input == "yes":
                                    print("[Cashbox].")
                                    print("[Cashbox inventory:\n18$ \n1x Shotgun shells box]")
                                    print("You take the money and shells.")
                                print("You head to the station.")
                                print("You buy a ticket and board the train. You have won the game!")
                            else:
                                print("You are in the station but have no money.")
                                print("You head back to the shop, find the cashbox, take the money, and return.")
                                print("You buy a ticket and board the train. You have won the game!")
                        else:
                            print("Without a map, you get lost and never find a way out. Game Over!")
                    else:
                        print("Without the information on the banner, you wander into the bear zone. The bear attacks. Game Over!")
                else:
                    print("Without supplies, you don't survive the night. Game Over!")
            elif player_input == "backward":
                print("You stumble into a deep pit. Game Over!")
            else:
                print("You walk left and find an old house. It's abandoned, but you stay the night and survive. Game Over!")
        else:
            print("You are in the dark and hear strange noises. You are too scared to move. Game Over!")
    else:
        print("You are in the dark and hear strange noises. You panic and run into a tree, knocking yourself out. Game Over!")

def castle_adventure() -> None:
    print("You are in the castle!")

def space_adventure() -> None:
    print("You are in space!")