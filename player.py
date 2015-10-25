__author__ = 'time'
"""
This file holds all player-based functions.
"""

import models
import player_utils


class Player:
    name = ''
    level = 1
    gender = ''
    left_hand = None
    right_hand = None
    head = None
    armor = None
    feet = None
    hireling = False
    hireling_hand = None
    big = False
    battle_power = 1
    other_equips = []
    roll_modifier = 0
    super_munchkin = False
    card_class = []
    affected_class = []
    halfbreed = False
    card_race = ['Human']
    affected_race = ['Human']



    def __init__(self):
        self.name = input("What is your name? ")
        temp_lvl = -1
        while temp_lvl == -1:
            try:
                temp_lvl = int(input("What is your current level? "))
            except ValueError:
                print("Not a number, please enter a number.")
        self.level = temp_lvl
        self.race_input()
        self.class_input()
        self.gender_input()


    def __str__(self):
        print("Player: {} of Level {}".format(self.name, str(self.level)))
        print("is a {} {} {}".format(self.gender, self.card_race, self.card_class))
        print("Head {}".format(str(self.head)))
        print("Armor {}".format(self.armor))
        print("Left Hand {}".format(self.left_hand))
        print("Right Hand {}".format(self.right_hand))
        print("Feet " + str(self.feet))
        print("Others " + str(self.other_equips))
        print("Hireling? " + str(self.hireling))
        return 'player'


    def equip(self):
        # Insert call to __str__ to show the current equipment
        again = 'y'
        while again == 'y':
            selection = input("Enter a card: ")
            card = models.Treasure.get(models.Treasure.name == selection)
            # Write a function that checks validity of the card
            player_utils.player_equip_check(card, self)
            again = input("Do you want to equip another card? [yN]").lower()
            if again != 'y':
                break
            # Write a function that adds to battle_power


    def race_input(self):
        chk = input("Do you have a Race? [yN]").lower()
        if chk == 'y':
            card = input("Please enter the Race card you would like to play. ")
            # call the card from the database and add to the player
            if self.halfbreed:
                self.card_race.append(card)
            elif not self.super_munchkin:
                self.card_race = [card]
            if len(self.card_race) == 1 and self.halfbreed:
                self.affected_race = []
            else:
                self.affected_race = self.card_race


    def class_input(self):
        chk = input("Do you have a Class? [yN]").lower()
        if chk == 'y':
            card = input("Please enter the Class card you would like to play. ")
            # call the card from the database and add to the player
            if self.super_munchkin:
                self.card_class.append(card)
            elif not self.super_munchkin:
                self.card_class = [card]
            if len(self.card_class) == 1 and self.super_munchkin:
                self.affected_class = []
            else:
                self.affected_class = self.card_class


    def gender_input(self):
        chk = input("What is your gender? [mf]").lower()
        if chk == 'm':
            self.gender = 'Male'
        elif chk == 'f':
            self.gender = 'Female'
        else:
            self.gender_input()


    def unequip(self):
        pass


    def play_card(self, card):
        pass