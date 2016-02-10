__author__ = 'time'
"""
This file holds all player-based functions.
"""

# import models
import utils.player_utils

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



    def __init__(self, name, race, gender, level=1):
        self.name = name
        self.level = level
        self.race = race
        self.gender = gender


    def equip(self, selection):
        """function to equip a card onto a Player"""
        try:
            card = models.Treasure.get(models.Treasure.name == selection)
            player_utils.player_equip_check(card, self)
        except models.Treasure.DoesNotExist:
            print('card not found, try again')
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
