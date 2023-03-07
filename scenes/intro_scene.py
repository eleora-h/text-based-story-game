# Author: Eleora Hamming

import menus.menu
import scenes.dialogue
import scenes.combat

class intro_scene():
    def __init__(self, character, party, inventory):
        self.character = character
        self.party = party
        self.inventory = inventory

        self.play()

    def play(self):
        print("\n\nSCENE 1. This would describe the scene you are currently in and what the surroundings look like.\n You cannot leave this space (i.e. you can infinitely write north or east without getting anything new.) \n This is really just meant to demo a few of what the systems might look like. \n Recommend testing combat and dialogue.")

        while True:
            print("\nScene description. How do you wish to proceed?")
            valid_commands = ["north", "east", "west", "south", "n", "e", "s", "w", "talk", "look", "attack", "atk", "equip", "read", "h", "i", "p", "c"]
            c = input().lower()
            menus.menu.main_menu(c, self.party, self.character, self.inventory)
            if c not in valid_commands:
                print("Command not recognized, try again.")
            else:
                if c == "north" or c == "n":
                    print("\n you head north")
                    continue
                if c == "east" or c == "e":
                    print("\n you head east.")
                    continue
                if c == "west" or c == "w":
                    print("\n you head west.")
                    continue
                if c == "south" or c == "s":
                    print("\n you head south.")
                    continue
                if c == "look":
                    print("\n you look around and find nothing of interest.")
                    continue
                if c == "talk":
                    scenes.dialogue.dialogue()
                if c == "attack" or c == "atk":
                    scenes.combat.combat(self.character)
                
