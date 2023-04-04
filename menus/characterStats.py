# Author: Eleora Hamming

class characterStats():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating character stat class.")
            cls._instance = super(characterStats, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.health = 100
        self.mana = 100
        self.intellect = 5
        self.strength = 2
        self.resilience = 3
        self.level_points = 0

    def level_up(self, points):
        self.level_points += points
        if self.level_points == 0:
            print("Error: No points to spend.")
        else:
            print("What attribute do you want to level? Intellect (1), Strength (2), or Resilience (3).")
            while True:
                text = input()
                if text == "1":
                    self.level_points = self.level_points - 1
                    self.intellect += 1
                    print("Levelled intellect successfully.")
                    break
                elif text == "2":
                    self.level_points = self.level_points - 1
                    self.strength += 1
                    print("Levelled strength successfully.")
                    break
                elif text == "3":
                    self.level_points = self.level_points - 1
                    self.resilience += 1 
                    print("Levelled resilience successfully.")
                    break
                else:
                    print("Not a valid option.")

    def learn_spell(self):
        print("Current spells: \n1. Heal \n2. Grow")
        print("What spell do you want to learn? \n1. Heal \n2. Grow \n3. Iceshard \n4. Fireball")
        while True:
            text = input()
            if text == "1":
                print("Heal (II) learned.")
                break
            elif text == "2":
                print("Grow (II) learned.")
                break
            elif text == "3":
                print("Iceshard learned.")
                break
            elif text == "4":
                print("Fireball learned.")
                break
            else:
                print("Not a valid option.")

    def get_health(self):
        return self.health

    def add_health(self, amount):
        self.health = self.health + amount
    
    def lose_health(self, amount):
        self.health = self.health - amount
    
    def print_stats(self):
        print("CHARACTER STATS:")
        print("Health: " + str(self.health))
        print("Mana: " + str(self.mana))
        print("Intellect: " + str(self.intellect))
        print("Strength: " + str(self.strength))
        print("Resilience: " + str(self.resilience))
