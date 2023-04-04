# Author: Eleora Hamming

import scenes.introScenes.castleRoom

class esdeathIntro():
    def __init__(self, character, party, inventory):
        self.character = character
        self.party = party
        self.inventory = inventory
        self.__play()

    def __play(self):
        print("\n\nYou follow Esdeath out of the throne room and the doors slam shut behind you. You trail behind her in silence, contemplating how far you had come, and how badly you wanted to go home. The hallways are dark and labyrinthine, and go on forever and ever. Eventually she comes to a halt outside a dark door, and she beckons you inside. Inside the room there is a table, with a gardening pot and a small bud blossoming from it. Looking bored, Esdeath says: 'Make it grow'.")
        print("\n\nTry spellcasting... press 'M' to bring up available spells.")
        text = input()
        if text == "m" or "M":
            print("\nAvailable spells:\n   1. Grow\n   2. Heal")
            print("\nInput spell by number:")
            while True:
                text = input()
                if text == "1":
                    print("\nYou stare at the plant, and focus your attention onto it. A single bud blooms from it.")
                    break
                elif text == "2":
                    print("\nYou stare at the plant, but nothing happens. Maybe you tried the wrong spell.")
                else:
                    print("\nNot a valid option.")
            print("\nEsdeath seems unimpressed, and raises one of her eyebrows. 'That's what all the fuss is about? I don't understand why the Queen would want to waste her time on the likes of you.' \n1. Say nothing. \n2. 'I wish I wasn't here wasting my time on you either.'")
            text = input()
            while True:
                if text == "1":
                    print("\n'Nothing to say?' A sneer disfigures her otherwise beautiful face. 'I hate commoners like you. Mindless sheep!'")
                    break
                elif text == "2":
                    print("\nContempt disfigures her beautiful countenance. 'Worthless dog,' she snaps, and before you have a chance to blink she backhands you across the face. You stumble away from her, clutching at your cheek. 'Don't speak to me unless you're spoken to.'")
                    break
                else:
                    print("\nNot a valid option.")
            print("\nThe wolfish woman sighs, and rests her hands against the table. Her gaze is cast downwards, on the small bud blooming upwards - a pink rose. 'Regardless, I will do as the Queen commands. Let me tell you this, Edyth. You are unprecedented, and your arrival here will shake the foundations of our court. Follow my orders and no undue harm will come to you, at least not from anyone other than me.' There's a temporary silence you do not want to break. Then she looks up, fixing you beneath her ice blue eyes. 'Given time, you will become powerful. But for now, get settled. Tomorrow morning will have new trials for you.'")
        scenes.introScenes.castleRoom.castleRoom(self.character, self.party, self.inventory)

