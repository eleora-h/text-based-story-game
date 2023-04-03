# Author: Eleora Hamming

import scenes.introScenes.castleRoom

class esdeathIntro():
    def __init__(self, character, party, inventory):
        self.character = character
        self.party = party
        self.inventory = inventory
        self.__play()

    def __play(self):
        print("\n\nYou follow her out of the throne room and the doors slam shut behind you. You follow her in silence, contemplating how far you had come, and how badly you wanted to go home. The hallways are dark and labyrinthine, and go on forever and ever. Eventually she comes to a halt outside a dark door, and she beckons you inside. Inside the room there is a table, with a gardening pot and a small bud blossoming from it. Looking bored, Esdeath says: 'Make it grow'.")
        print("\n\nTry spellcasting... press 'M' to bring up available spells.")
        text = input()
        if text == "m" or "M":
            print("\nAvailable spells:\n   1. Grow\n    2. Heal")
            print("\nInput spell by number:")
            while True:
                text = input()
                if text == "1":
                    print("\nYou stare at the plant, and focus your attention onto it. A single bud blooms from it.")
                    break
                if text == "2":
                    print("\n You stare at the plant, but nothing happens. Maybe you tried the wrong spell.")
            print("\n\nEsdeath seems unimpressed, and raises one of her eyebrows. 'That's what the fuss is all about? Whatever. I'll bring you to your room.'")
        scenes.introScenes.castleRoom.castleRoom(self.character, self.party, self.inventory)

