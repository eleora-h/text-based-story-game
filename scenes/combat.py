# Author: Eleora Hamming

# Imports
import random

class combat():
    def __init__(self, character):
        self.character = character
        self.enemy_hp = 10

        self.__play()

    def __play(self):
        print("\n\nThe passage opens up into a cavernous hall that almost looks like the inside of a church, with stained glass windows and pews lining it. Dim light streams in through the windows. At the end of the hall there is a massive creature, a looming silhouette rather like a bear with a disfigured face and scars all along its body. It rears up onto its hind paws and unhinges its gaping jaws, letting out a roar.")
        print("\nSTARTING COMBAT. Enter 'f' to flee.")
        while True:
            print("Enemy turn: ")
            score = random.randint(0, 5)
            if score == 0:
                print("The bear lunges at you, but you dodge to the side.")
            elif score >= 1 and score < 3:
                print("The bear lunges at you and you dodge to side. Fangs cut through your light clothing, but luckily the bite is shallow. -" + str(score) + " health points.")
            else:
                print("With a roar, the bear swats at you with its paw. Unable to move fast enough, claws sink deep into your leg and you scream You don't have time to react though - you have to act before something worse happens. -" + str(score) + " health points.")
            self.character.lose_health(score)

            print("\nYOUR TURN: \n1. Heal \n2. Attack with your dagger.")
            text = input().lower()
            if text == "1":
                score = random.randint(0, 10)
                self.character.add_health(score)
                print("A soft glow emits from your fingertips and you feel a surge of energy as the pain diminishes. You heal for " + str(score) + " health points.")
            elif text == "2":
                score = random.randint(0, 5)
                self.enemy_hp = self.enemy_hp - score
                if score == 0:
                    print("You missed!")
                elif score == 5:
                    print("Critical hit! You strike the bear deep and true with your dagger! -" + str(score) + " health points.")
                else:
                    print("Your dagger scrapes along the bear's flank! -" + str(score) + " health points.")

                if self.enemy_hp <= 0:
                    print("With a final scream, the bear topples to the ground.")
                    print("Earned 1 level up point!")
                    self.character.level_up(1)
                    self.character.learn_spell()
                    break
                if text == "f":
                    break
                elif int(self.character.get_health()) <= 0:
                    print("Fangs latch onto you and you die a brutal and horrible death. So much for your story.")
                elif int(self.character.get_health()) < 10:
                    print("Approaching critical health! You should flee!")
            else:
                print("Not a valid option.")
                
            

