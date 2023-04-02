# Author: Eleora Hamming

import scenes.introScenes.castleRoom

class misaIntro():
    def __init__(self):
        self.__play()

    def __play(self):
        print("\n\nThe throne room's doors swing shut behind you with a resounding bang. You stand in a small antechamber, empty except for Misa and you. The short woman turns, looking up to you. She looks - kind. In a way she reminds you of your mother, but you don't want to think about that. \n'Well, dear, how are you?' She asks gently.")
        print("\n1. Your gaze shifts to your feet. 'Okay, I guess.'\n2. 'Does it matter how I am?'")
        text = input()
        if text == "1":
            print("\n'You're brave, dear. I know it doesn't mean much know, but you'll come to recognie this is a good thing.")
        if text == "2":
            print("\n'Of course it matters! I promise you, we will take care of you here. Things will become easier with time.'")
        print('\n\nMisa turns away from you and begins to lead you deeper into the castle. You follow, and she begins to talk, mostly about cheerful things, like how there is always warm food in the kitchen or other students studying their own things. You cannot focus on that - you can only think of home. As she leads you deeper into the castle, the walls turn damp and the hallways begin to darken. Wax lamps cast a warm gold light to keep away the darkness. Eventually Misa comes to a halt in front of a dark wooden door. With a expectant look inside, she beckons you inside first. You push open the door and enter a well-lit study.')
        print("\n'Now darling, it's time to learn to use the magic within you.' She leads you to a wooden table situated in the middle of the room. There's a small gardening pot on the table, with a single sapling poking out of the dark soil. 'Try to make it grow.'")
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
            print("\nMisa gasps audibly, and claps her hands together in delight! 'Well done!' she exclaims. 'That's far more than I expected from a novice.' She launches into a long-winded dialogue about magic and safety and too much for you to follow. Hours past and eventually you must look dead on your feet, because she takes pity on you. 'Time to take you to your room,' she says, and you follow her out of the study.")
            scenes.introScenes.castleRoom.castleRoom()

