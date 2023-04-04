# Author: Eleora Hamming

import menus.menu
import scenes.introScenes.combatIntro

class castleRoom():
    def __init__(self, character, party, inventory):
        self.character = character
        self.party = party
        self.inventory = inventory

        self.__play()

    def __play(self):
        print("\nYou follow your guide to a room in one of the tall towers. She departs with a quick goodbye. Also note, in your room, you can exit to next scene by typing in 'sleep.'")
        found_dagger = False

        while True:
            print("\nHow do you wish to proceed?")
            valid_commands = ["north", "east", "west", "south", "n", "e", "s", "w", "talk", "look", "attack", "atk", "equip", "read", "h", "i", "p", "c", "sleep"]
            c = input().lower()
            menus.menu.main_menu(c, self.party, self.character, self.inventory)
            if c not in valid_commands:
                print("Command not recognized, try again.")
            else:
                if c in ["north", "n", "east", "e", "south", "s", "west", "w"]:
                    print("\nYou cannot leave this room. Try 'sleep' for next scene.")
                if c == "sleep":
                    if not found_dagger:
                        print("\nYou missed an item from this room! Try using the 'equip' command.")
                    else:
                        scenes.introScenes.combatIntro.combatIntro(self.character, self.party, self.inventory)
                if c == "equip":
                    print("\nYou squat down beside the bed and you see a strange glitter. Curious, you reach underneath - and your hand touches something hard and sharp. Carefully, you draw out a shining dagger. It's plain, with a silver hilt, but it's polished and it's edge is sharp. Dagger added to inventory.")
                    found_dagger = True
                    self.inventory.add_item()
                if c == "read":
                    print("\nThere are two books on a plush chair by the fire. One is named 'A Hopeless Romantic' and the other is titled 'An Exhausted Student's Memoirs'.")
                if c == "look":
                    print("\nA spacious bedroom with blue and gold decor. There's a 4-poster bed with royal blue sheets against the wall. The fire is lit and crackling.")
                    continue
                if c == "talk":
                    print("\nNo one to talk to.")
                if c == "attack" or c == "atk":
                    print("\nNothing to attack.")
                    #scenes.combat.combat(self.character)
                
