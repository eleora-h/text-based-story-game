# Author: Eleora Hamming
# Main scene

import scenes.intro_scene
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
            Welcome to the initial prototype for Witch Hunt. 
            Please type 'h' or 'help' for a quick overview of common commands.
            """
            print(intro)

            start = input()
            if start == "h" or start == "help":
                print("MENU COMMANDS:")
                print("-h help \t -i inventory\t -p party \t-c character stats")
                print("\nCOMMON MOVEMENTS:")
                print("\t attack/atk \t look \t talk \t equip \t read")
                print("\t north/n \t east/e \t south/s \t west/w")
                print("\nAre you ready to start the first demo? (Y/N)")
                s = input().lower()
                if s not in ("y", "yes"):
                    print("Exiting demo.")
                    exit()
                else:
                    print('done')
                    scenes.intro_scene.intro_scene(self.character, self.party, self.inventory)

instance = playGame()
instance.play()