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
    print("You wake up in a dark, damp castle chamber. A torch flickers on the wall.")
    player_input = input("Take the torch? (yes/no): ")
    if player_input == "yes":
        print("[Torch taken]. You can see better now.")
        print("There are two doors: one to the left and one to the right.")
        player_input = input("Which door do you take? (left/right): ")
        if player_input == "left":
            print("You enter a grand hall with a throne. A shadowy figure sits there.")
            player_input = input("Approach the figure or explore the hall? (approach/explore): ")
            if player_input == "approach":
                print("The figure is a ghostly king! He asks you to solve a riddle.")
                print("'I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?'")
                player_input = input("Your answer: ")
                if player_input.lower() == "echo":
                    print("The king nods. He grants you safe passage out of the castle. You win!")
                else:
                    print("The king frowns. The torches go out. You are trapped forever! Game Over.")
            else:
                print("You explore the hall and find a hidden passage behind a bookshelf.")
                print("It leads to a treasure room! But a giant snake guards it.")
                player_input = input("Fight the snake or sneak past? (fight/sneak): ")
                if player_input == "fight":
                    print("You grab a sword from a statue and battle the snake. You win and claim the treasure!")
                else:
                    print("You sneak past successfully and take some treasure. You escape the castle rich! You win!")
        else:
            print("You enter a dark dungeon. The door locks behind you.")
            print("A pair of glowing eyes stare at you. A dragon awakens!")
            player_input = input("Fight, hide, or flee? (fight/hide/flee): ")
            if player_input == "fight":
                print("You grab a rusty sword from the ground and charge. The dragon breathes fire. Game Over!")
            elif player_input == "hide":
                print("You hide behind a pile of bones. The dragon goes back to sleep, allowing you to escape. You win!")
            else:
                print("You run through a hidden tunnel and escape the castle. You win!")
    else:
        print("You stumble in the dark and fall into a hidden pit. Game Over!")

def space_adventure() -> None:
    print("You are an astronaut on a space station when an alarm blares. Oxygen levels are dropping!")
    player_input = input("Head to the control room or the escape pod? (control/pod): ")
    if player_input == "control":
        print("You enter the control room and see a warning: a meteor is approaching!")
        player_input = input("Try to steer the station or repair the oxygen system first? (steer/repair): ")
        if player_input == "steer":
            print("You grab the controls and manage to dodge the meteor. The station is saved! But you still need oxygen.")
            player_input = input("Try to repair the oxygen system now? (yes/no): ")
            if player_input == "yes":
                print("You fix the system just in time. You survive and call for help. You win!")
            else:
                print("The lack of oxygen takes its toll. You pass out. Game Over!")
        else:
            print("You attempt to repair the oxygen system, but it takes too long. The meteor crashes into the station. Game Over!")
    else:
        print("You run to the escape pod and launch into space.")
        print("However, you realize too late that your pod is off course, drifting into the void.")
        player_input = input("Attempt to signal for help or try to manually steer? (signal/steer): ")
        if player_input == "signal":
            print("You send a distress signal. A rescue ship picks you up. You win!")
        else:
            print("You attempt to steer but fail. Your oxygen runs out. Game Over!")
        
        player_input = input("Try to fix the pod’s navigation system? (yes/no): ")
        if player_input == "yes":
            print("You manage to correct your course and land on a nearby planet.")
            print("You step out and see a strange alien city in the distance. Adventure continues!")
        else:
            print("You remain lost in space. Game Over!")