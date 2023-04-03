# Author: Eleora Hamming

# Imports
import random

class combat():
    def __init__(self, character):
        self.character = character
        self.enemy_hp = 10

        self.__play()

    def __play(self):
        print("\n\nThe passage opens up into a dark and cavernous hall. You hear a hoarse rattling in the dark and the smell of death and decay. In the darkness you can see the silhouette of a monstrous creature, shaped vaguely like a bear but with thick tusks protruding from its mouth and sickly skin.")
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
            self.character.set_health(score)

            print("\nYOUR TURN: \n1. Cast a spell of light \n2. Attack with your sword.")
            text = input().lower()
            score = random.randint(0, 5)
            self.enemy_hp = self.enemy_hp - score
            if score == 0:
                print("You missed!")
            else:
                print("You score a hit! -" + str(score) + " health points.")

            if self.enemy_hp <= 0:
                print("With a final scream, the bear topples to the ground.")
                print("Earned 1 level up point!")
                self.character.level_up(1)
                break
            if text == "f":
                break
            elif int(self.character.get_health()) <= 0:
                print("Fangs latch onto you and you die a brutal and horrible death. So much for your story.")
            elif int(self.character.get_health()) < 10:
                print("Approaching critical health! You should flee!")
                
            

