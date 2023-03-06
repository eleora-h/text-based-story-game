# Author: Eleora Hamming

def main_menu(args, party, character, inventory):
    if args == "help" or args == "h":
        print('help')
    if args == "inventory" or args == "i":
        inventory.print_stats()
    if args == "character" or args == "c":
        character.print_stats()
    if args == "party" or args == "p":
        party.get_menu()