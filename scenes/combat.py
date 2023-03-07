# Author: Eleora Hamming

# Imports
import random

class combat():
    def __init__(self, character):
        self.character = character
        self.enemy_hp = 10

        self.__play()

    def __play(self):
        print("\nSTARTING COMBAT. Enter 'f' to flee.")
        while True:
            print("Enemy turn: ")
            score = random.randint(0, 5)
            if score == 0:
                print("Enemy misses!")
            elif score >= 1 and score < 3:
                print("Enemy scores light hit on you. -" + str(score) + " health points.")
            else:
                print("Enemy scores heavy hit on you. -" + str(score) + " health points.")
            self.character.set_health(score)

            print("\nYOUR TURN: (just press enter, this should have attack options and modifiers but didn't have time to add.)")
            text = input().lower()
            score = random.randint(0, 5)
            self.enemy_hp = self.enemy_hp - score
            if score == 0:
                print("You missed!")
            else:
                print("You score a hit! -" + str(score) + " health points.")

            if self.enemy_hp <= 0:
                print("Success! You killed your enemy!")
                print("Earned 1 level up point!")
                self.character.level_up(1)
                break
            if text == "f":
                break
            elif int(self.character.get_health()) <= 0:
                print("You died!")
            elif int(self.character.get_health()) < 10:
                print("Approaching critical health! You should flee!")
                
            

