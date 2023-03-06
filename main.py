# Author: Eleora Hamming
# Main scene

import scenes.intro_scene as intro_scene
import menus.menu as menu
import menus.characterStats
import menus.party
import menus.inventory

class playGame():
    def __init__(self):
        self.character = menus.characterStats.characterStats()
        self.inventory = menus.inventory.inventory()
        self.party = menus.party.party()

    def play(self):

        while True:
            intro = """
            Welcome to this world. Here is a text sample.
            """
            print(intro)

            print("Please enter a direction in which to explore.")
            valid_commands = ["north", "east", "west", "south"]
            command = input()
            menu.main_menu(command, self.party, self.character, self.inventory)
            if command not in valid_commands:
                print("try again")
            else:
                if command == "north":
                    print("head north")
                elif command == "east":
                    print("head east")
                elif command == "west":
                    print("next step")
                else:
                    print("south")
                break

instance = playGame()
instance.play()