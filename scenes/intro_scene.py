# Author: Eleora Hamming

import menus.menu
import scenes.dialogue
import scenes.combat
import scenes.introScenes.introDialogue
import scenes.introScenes.esdeathIntro
import scenes.introScenes.misaIntro

class intro_scene():
    def __init__(self, character, party, inventory):
        self.character = character
        self.party = party
        self.inventory = inventory

        self.play()

    def play(self):
        textbox = """
        	\nWelcome to Eden. You are Edyth, the first woman to have an affinity for life magic in hundreds of years. Born in a small farming village, you are plucked from your family and brought to the Capitol, where you are brought before the Queen herself. You find yourself in a gilded throne room, with a tall and stern woman facing you on a throne of gold. She has dark hair and cold eyes, and her lips are painted cherry red. There is no smile on her face. “Welcome, my daughter,” she says to you. 
        """
        print(textbox)

        while True:
            print("\nHow do you wish to proceed?")
            valid_commands = ["north", "east", "west", "south", "n", "e", "s", "w", "talk", "look", "attack", "atk", "equip", "read", "h", "i", "p", "c"]
            c = input().lower()
            menus.menu.main_menu(c, self.party, self.character, self.inventory)
            if c not in valid_commands:
                print("Command not recognized, try again.")
            else:
                if c in ["north", "n", "east", "e", "west", "w", "south", "s"]:
                    print("\nYou cannot leave this room!")
                    continue
                if c == "equip":
                    print("\nNothing to equip.")
                if c == "read":
                    print("\nNothing to read.")
                if c == "look":
                    print("\n A grand hall with soft, plush red carpets and vinery along the back wall beyond the gildened gold throne. Tall stained glass windows let bright morning light stream in.")
                    continue
                if c == "talk":
                    scene_dialogue = scenes.introScenes.introDialogue.introDialogue()
                    next_scene = scene_dialogue.get_next_scene()
                    if next_scene == 1:
                        scenes.introScenes.misaIntro.misaIntro()
                    else:
                        scenes.introScenes.esdeathIntro.esdeathIntro()
                    print("End scene.")
                    break
                if c == "attack" or c == "atk":
                    print("\nYou cannot attack this character.")
                    #scenes.combat.combat(self.character)
                
