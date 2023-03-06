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
        print("SCENE 1. blah blah blah.\nHow do you wish to proceed?")

        while True:
            valid_commands = ["north", "east", "west", "south", "n", "e", "s", "w", "talk", "look", "attack", "atk"]
            c = input().lower()
            menus.menu.main_menu(c, self.party, self.character, self.inventory)
            if c not in valid_commands:
                print("Command not recognized, try again.")
            else:
                if c == "north" or c == "n":
                    print("\nhead north")
                if c == "east" or c == "e":
                    print("\nhead east")
                if c == "west" or c == "w":
                    print("\nnext step")
                if c == "south" or c == "s":
                    print("\nsouth")
                    continue
                if c == "look":
                    print("\nlook")
                if c == "talk":
                    print("\ntalking")
                    scenes.dialogue.dialogue()
                    # open dialogue options
                if c == "attack" or c == "atk":
                    print("\nattack")
                
