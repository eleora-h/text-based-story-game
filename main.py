# Author: Eleora Hamming
# Main scene

import scenes.intro_scene as intro_scene
import menus.menu as menu
import menus.characterStats
import menus.party
import menus.inventory

if __name__ == "__main__":

    while True:
        intro = """
        Welcome to this world. Here is a test sample.
        """
        print(intro)

        # Initialize character, party, inventory info.
        char = menus.characterStats.characterStats()
        inventory = menus.inventory.inventory()
        party = menus.party.party()

        print("Please enter a direction in which to explore.")
        valid_commands = ["north", "east", "west", "south"]
        command = input()
        menu.main_menu(command, party, char, inventory)
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