# Author: Eleora Hamming
# Imports
import yaml

class inventory():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating inventory class.")
            cls._instance = super(inventory, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.items = { "Weapons": { "sword": { "attack": 5, "options": ["stab", "parry", "cut"], "equipped": False }, "staff": { "intellect": 5, "options": [ "ice", "water" ], "equipped": True }}, "Consumables": { "HP Pot": { "health": 25, "quantity": 4 }}}

    def get_items(self):
        print('\n')
        print(yaml.dump(self.items, default_flow_style=False))

    def use_consumable(self, consumable):
        if consumable in self.items.get("Consumables"):
            print("found")
        else:
            print("Consumable not found!")

    def add_item(self, item):
        # to do
        pass

    def get_menu(self):
        self.get_items()
