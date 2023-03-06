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

    def get_health(self):
        return self.health

    def set_health(self, amount):
        self.health = self.health - amount
    
    def print_stats(self):
        print("CHARACTER STATS:")
        print("Health: " + str(self.health))
        print("Mana: " + str(self.mana))
        print("Intellect: " + str(self.intellect))
        print("Strength: " + str(self.strength))
        print("Resilience: " + self.resilience)
