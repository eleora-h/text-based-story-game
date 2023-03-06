# Author: Eleora Hamming

import menus.characterStats
import menus.inventory
import menus.party
import menus.help

def main_menu(args):
    if args == "help" or args == "h":
        menus.help.printmessage()
    if args == "inventory" or args == "i":
        menus.inventory.printmessage()
    if args == "character" or args == "c":
        menus.characterStats.print_stats()
    if args == "party" or args == "p":
        menus.party.printmessage()

print("done")