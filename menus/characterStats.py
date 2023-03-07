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
            text = input()
            if text == "1":
                self.level_points = self.level_points - 1
                self.intellect += 1
                print("Levelled intellect successfully.")
            elif text == "2":
                self.level_points = self.level_points - 1
                self.strength += 1
                print("Levelled strength successfully.")

            elif text == "3":
                self.level_points = self.level_points - 1
                self.resilience += 1 
                print("Levelled resilience successfully.")

    def get_health(self):
        return self.health

    def set_health(self, amount):
        self.health = self.health + amount
    
    def print_stats(self):
        print("CHARACTER STATS:")
        print("Health: " + str(self.health))
        print("Mana: " + str(self.mana))
        print("Intellect: " + str(self.intellect))
        print("Strength: " + str(self.strength))
        print("Resilience: " + str(self.resilience))
