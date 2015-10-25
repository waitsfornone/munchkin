__author__ = 'time'

import player
from peewee import *
import sys

db = SqliteDatabase('munchkin.db')

def main_menu(plyr=None):
    print("What would you like to do?")
    print("1 - create player")
    print("2 - equip a new card")
    print("3 - unequip a card")
    print("4 - BATTLE")
    print("5 - play a card")
    print("q - quit")
    choice = input('Make a selection  ')
    if choice == '1':
        plyr = player.Player()
        main_menu(plyr)
    elif choice == '2':
        if plyr:
            plyr.equip()
        else:
            print("You have not created a player yet.")
            main_menu(plyr)
    elif choice == '3':
        if plyr:
            print("need to write this function")
            player1.unequip()
            main_menu(plyr)
        else:
            print("You have not created a player yet.")
            main_menu(plyr)
    elif choice == '4':
        if plyr:
            print("Dont have battles yet, sorry")
            # battle()
            main_menu(plyr)
        else:
            print("You have not created a player yet.")
            main_menu(plyr)
    elif choice == '5':
        if plyr:
            print("We can't play other cards yet")
            # play_card()
            main_menu(plyr)
        else:
            print("You have not created a player yet.")
            main_menu(plyr)
    elif choice == 'q':
        sys.exit(0)
    else:
        print("Not a valid choice")
        main_menu(plyr)

# print("Hello! Welcome to the Munchkin Battle Calculator!")
# player1 = False
# main_menu(player1)
# print(player1)


if __name__ == '__main__':
    db.connect()
    while True:
        # instantiate your class
        # raise the exit from wihin the script
