# Author: Eleora Hamming

import scenes.introScenes.castleRoom

class esdeathIntro():
    def __init__(self, character, party, inventory):
        self.character = character
        self.party = party
        self.inventory = inventory
        self.__play()

    def __play(self):
        print("hello world")
        scenes.introScenes.castleRoom.castleRoom(self.character, self.party, self.inventory)

