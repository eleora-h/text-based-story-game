# Author: Eleora Hamming


class dialogue():
    def __init__(self):
        self.__play()

    def __play(self):
        print("This is a sample dialogue...")
        while True:
            print("\nSelect dialogue.\n 1. Moral answer \n 2. Immoral answer.")
            text = input()
            if text == "1":
                print("Initialize morally gray dialogue.")
            elif text == "2": 
                print("Initialize immoral dialogue.")
            else:
                print("Option not recogized, try again.")
            print("End conversation.")
            break