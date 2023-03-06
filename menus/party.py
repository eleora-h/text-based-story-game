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
        self.companions = ["Cat"]

    def get_party(self):
        if self.active_party:
            print("Your active party is: " + self.active_party)
        else:
            print("No members in your party.")

    def set_active_party(self):
        print("Available companions: " + str(self.companions))
        print("Who do you want to add to your party?")
        name = input()
        if name not in self.companions:
            print("Companion not found.")
        else:
            self.active_party.append(name)
            print(name + " added to party.")
            print(self.active_party)

    def get_menu(self):
        self.get_party()
        print("Do you want to change your party? (Y/N)")
        text = input()
        if text == "Y" or text == "y":
            self.set_active_party()