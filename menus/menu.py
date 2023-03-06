# Author: Eleora Hamming

import menus.characterStats
import menus.inventory
import menus.party
import menus.help

def main_menu(args, party, character, inventory):
    if args == "help" or args == "h":
        menus.help.printmessage()
    if args == "inventory" or args == "i":
        menus.inventory.printmessage()
    if args == "character" or args == "c":
        character.print_stats()
    if args == "party" or args == "p":
        party.get_menu()
    return party, character, inventory