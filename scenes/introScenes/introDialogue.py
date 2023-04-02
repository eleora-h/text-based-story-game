# Author: Eleora Hamming

class introDialogue():
    def __init__(self):
        self.next_scene = None
        self.__play()

    # upsets the queen, esdeath as castle guide
    def __tree_two(self):
        print("\nThe queen stirs in her chair, and her lips thin. If she looked cold before, now she is the picture of cold fury. 'I bestowed a great honor upon you,' she snaps. 'Be thankful, or I will cast you out. Don't be an idiot.'")
        print("\n1. 'I don't care what you think, I want to leave.'\n 2. Apologize. \n 3. Stay silent.")
        text = input()
        if text == "1":
            print("\nFlames burst up around you, and there is an agony beyond belief. You are consumed by pain - filled with it until you are close to bursting. Tears stream down your face. Then as quick as the pain came, it is gone. The queen is still surveying you with a look of contempt. 'Don't test me again.'") # get tortured
        elif text == "2":
            print("\n'Just this once you are forgiven. Do it again and you will suffer for it.'")
        elif text == "3":
            pass
        else:
            print("Option not recognized, try again.")
        print("\n\nWith a deep sigh, the queen steeples her fingers together. There is silence, and you hear the birds singing beyond the castle walls. 'Edyth', she says suddenly. 'That is your name, correct? You have been brought here because of your magic. You have a true gift, and it has not been seen for hundreds of years. I wish to help you cultivate this gift, and learn to wield it to its fullest. But in order to this, you must accept my tutelage, and live within my walls.' Her eyes darken. 'You have been foolish thus far, to resist the Queen. And it does not bode well for your future. Your guide will be Esdeath.' She beckons towards a tall woman standing at one edge of the courtroom (presumably Esdeath.) Esdeath smiles at you, with lush blonde hair braided back and cool blue eyes. 'My daughter,' she says, and you have a sinking certainty you made a mistake in your resistance.")
        self.next_scene = 2

    # makes the queen happy
    def __tree_one(self):
        print("\n\nThe queen's eyes soften, and she slumps back in her seat, the tension draining out of her. 'It's good to know you will serve well,' she sighs. 'Well, you must udnerstand. I have brought you here because of your magic, a true gift to the realm. I expect you, under my tutelage, will learn to wield it completely. But first, I will have you acquainted with the castle. Misa will show you around.' The queen beckoned towards a chubby blonde woman at the corner of the room, who stepped forward eagerly at her gesture. Rosy cheeks and green eyes, dressed in homely clothes - she did not look like a lady at all. But nonetheless, you took your leave and followed her out of the room.")
        self.next_scene = 1

    def __play(self):
        while True:
            print("\nSelect dialogue.\n 1. Stay silent. \n 2. 'You had no right to take me from my family.' \n3. 'It's an honor being here, my Lady.'")
            text = input()
            if text == "1" or text == "2":
                self.__tree_two()
                break
            elif text == "3": 
                self.__tree_one()
                break
            else:
                print("Option not recogized, try again.")
            break

    def get_next_scene(self):
        return self.next_scene