# Author: Eleora Hamming

class party():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating party class.")
            cls._instance = super(party, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.active_party = []
        self.companions = ["Kathy"]

    def get_items(self):
        print(self.items)

    def use_consumable(self, consumable):
        if consumable in self.items.get("Consumables"):
            print("found")
        else:
            print("Consumable not found!")

    def add_item(self, item):
        # to do
        pass

def printmessage():
    print("THIS IS THE INVENTORY")
