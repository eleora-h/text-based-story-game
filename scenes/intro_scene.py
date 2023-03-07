# Author: Eleora Hamming

import menus.menu
import scenes.dialogue

class intro_scene():
    def __init__(self, character, party, inventory):
        self.character = character
        self.party = party
        self.inventory = inventory

        self.play()

    def play(self):
        print("\n\nSCENE 1. blah blah blah.")

        while True:
            print("\nScene description. How do you wish to proceed?")
            valid_commands = ["north", "east", "west", "south", "n", "e", "s", "w", "talk", "look", "attack", "atk"]
            c = input().lower()
            menus.menu.main_menu(c, self.party, self.character, self.inventory)
            if c not in valid_commands:
                print("Command not recognized, try again.")
            else:
                if c == "north" or c == "n":
                    print("\nhead north")
                    continue
                if c == "east" or c == "e":
                    print("\nhead east")
                    continue
                if c == "west" or c == "w":
                    print("\nnext step")
                    continue
                if c == "south" or c == "s":
                    print("\nsouth")
                    continue
                if c == "look":
                    print("\nlook")
                    continue
                if c == "talk":
                    scenes.dialogue.dialogue()
                if c == "attack" or c == "atk":
                    print("\nattack")
                
