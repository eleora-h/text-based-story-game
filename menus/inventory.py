# Author: Eleora Hamming

import yaml


class inventory():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating inventory class.")
            cls._instance = super(inventory, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.items = { "Weapons": { "sword": { "attack": 5, "options": ["stab", "parry", "cut"] }}, "Consumables": { "HP": { "health": 25, "quantity": 4 }}}

    def get_items(self):
        print(yaml.dump(self.items, default_flow_style=False))

    def use_consumable(self, consumable):
        if consumable in self.items.get("Consumables"):
            print("found")
        else:
            print("Consumable not found!")

    def add_item(self, item):
        # to do
        pass

    def print_stats(self):
        print("THIS IS THE INVENTORY")
