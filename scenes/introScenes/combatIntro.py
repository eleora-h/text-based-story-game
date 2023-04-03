# Author: Eleora Hamming

import menus.menu
import scenes.combat

class combatIntro():
    def __init__(self, character, party, inventory):
        self.character = character
        self.party = party
        self.inventory = inventory

        self.__play()

    def __room_two(self):
        scenes.combat.combat(self.character)
        print("You reached the end of the demo! Congrats.")
        exit()

    def __room_one(self):
        print("\nYou exit the room, and the statue that was outside your door last night is gone. You are in a dark corridor, and nothing is as you remember it.")

        while True:
            valid_commands = ["north", "east", "west", "south", "n", "e", "s", "w", "talk", "look", "attack", "atk", "equip", "read", "h", "i", "p", "c"]
            c = input().lower()
            menus.menu.main_menu(c, self.party, self.character, self.inventory)
            if c not in valid_commands:
                print("Command not recognized, try again.")
            else:
                if c in ["east", "e"]:
                    print("\nYou head south down the corridor. A passage opens to the west.")
                    valid_commands = ["north", "east", "west", "south", "n", "e", "s", "w", "talk", "look", "attack", "atk", "equip", "read"]
                    c = input().lower()
                    if c not in valid_commands:
                        print("Command not recognized, try again.")
                    if c in ["west", "w"]:
                        self.__room_two()
                        break
                    if c in ["north", "n"]:
                        print("You move back to previous scene. You are standing in a dark corridor stretching to both your left and right, and the entrance to your room is behind you.")
                    if c in ["read", "talk", "look", "attack", "atk", "equip", "read"]:
                        print("Action not available. Move back to previous scene.")
                if c in ["south", "s"]:
                    # go back to main room
                    print("\nYou re-enter your room.")
                    return
                if c in ["north", "n"]:
                    print("\nOnly a smooth stone wall lined with paintings..")
                if c in ["west", "w'"]:
                    print("You head west down the corridor. There's a locked door at the end.")
                if c == "equip":
                    print("\nNothing to equip.")
                if c == "read":
                    print("\nNothing to read.")
                if c == "look":
                    print("\nNothing to look at.")
                if c == "talk":
                    print("\nNo one to talk to.")
                if c == "attack" or c == "atk":
                    print("\nNothing to attack.")

        # go north on to enemy
        # go south

    # this is actually a dungeon sequence
    def __play(self):
        print("\n\nSunlight streams through the window. You can hear birds outside. The sky is a soft pink.")

        while True:
            print("\nHow do you wish to proceed?")
            valid_commands = ["north", "east", "west", "south", "n", "e", "s", "w", "talk", "look", "attack", "atk", "equip", "read", "h", "i", "p", "c", "sleep"]
            c = input().lower()
            menus.menu.main_menu(c, self.party, self.character, self.inventory)
            if c not in valid_commands:
                print("Command not recognized, try again.")
            else:
                if c in ["east", "e"]:
                    print("\nThere's only a smooth stone wall.")
                if c in ["south", "s"]:
                    print("\n Stone wall with a painting on it.")
                if c in ["north", "n"]:
                    # go next scene
                    self.__room_one()
                if c in ["west", "w'"]:
                    print("You look out the window. It overlooks a garden of flowers surrounded by tall stone walls.")
                if c == "equip":
                    print("\nNothing to equip.")
                if c == "read":
                    print("\nThere are two books on a plush chair by the fire. One is named 'A Hopeless Romantic' and the other is titled 'An Exhausted Student's Memoirs'.")
                if c == "look":
                    print("\nA spacious bedroom with blue and gold decor. There's a 4-poster bed with royal blue sheets against the wall. The fire died during the night.")
                    continue
                if c == "talk":
                    print("\nNo one to talk to.")
                if c == "attack" or c == "atk":
                    print("\nNothing to attack.")
