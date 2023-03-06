# Author: Eleora Hamming

def main_menu(args, party, character, inventory):
    if args == "help" or args == "h":
        print("MENU COMMANDS:")
        print("-h help \t -i inventory\t -p party \t-c character stats")
        print("\nCOMMON MOVEMENTS:")
        print("\t attack/atk \t look \t talk \t equip \t read")
        print("\t north/n \t east/e \t south/s \t west/w")
    if args == "inventory" or args == "i":
        inventory.get_menu()
    if args == "character" or args == "c":
        character.print_stats()
    if args == "party" or args == "p":
        party.get_menu()
    if args == "quit" or args == "q":
        print("Are you sure you want to quit? No progress will be saved. (Y/N)")
        text = input()
        if text in ("y", "yes", "Yes", "Y"):
            exit()