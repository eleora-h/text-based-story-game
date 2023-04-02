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
        self.companions = []


    def get_party(self):
        if self.active_party:
            print("Your active party is: " + ', '.join(self.active_party))
        else:
            print("No members in your party.")

    def add_to_active_party(self):
        print("Available companions: " + str(self.companions))
        print("Who do you want to add to your party?")
        name = input()
        if name not in self.companions:
            print("Companion not found.")
        else:
            self.active_party.append(name)
            print(name + " added to party.")

    def remove_from_active_party(self):
        print("Who do you want to remove from your party?")
        name = input()
        if name not in self.active_party:
            print("Companion not found.")
        else:
            self.active_party.remove(name)
            print(name + " removed from party.")

    def get_menu(self):
        self.get_party()
        print("Do you want to change your party? (Y/N)")
        text = input()
        if text == "Y" or text == "y":
            print("Do you want to add or remove a member? (A/R)")
            n_text = input()
            if n_text in ("add", "a", "A"):
                self.add_to_active_party()
            else:
                self.remove_from_active_party()