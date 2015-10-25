__author__ = 'time'

import models
import ast
import player

def class_check(obj,player):
    class_limit = ast.literal_eval(obj.class_limit)
    if len(class_limit) > 0:
        for rec in class_limit.keys():
            if rec not in player.card_class and class_limit[rec]:
                print("Your class cannot use this card")
                return False
            elif rec not in player.card_class and not class_limit[rec]:
                return True
            elif rec in player.card_class and not class_limit[rec]:
                print("Your class cannot use this card")
                return False
    else:
        return True

def race_check(obj, player):
    race_limit = ast.literal_eval(obj.race_limit)
    if len(race_limit) > 0:
        for rec in race_limit.keys():
            if rec not in player.card_race and race_limit[rec]:
                print("Your class cannot use this card")
                return False
            elif rec not in player.card_race and not race_limit[rec]:
                return True
            elif rec in player.card_race and not race_limit[rec]:
                print("Your class cannot use this card")
                return False
    else:
        return True

def gender_check(obj, player):
    gender_limit = ast.literal_eval(obj.gender_limit)
    if len(gender_limit) > 0:
        for rec in gender_limit.keys():
            if rec not in player.gender and gender_limit[rec]:
                print("Your class cannot use this card")
                return False
            elif rec not in player.gender and not gender_limit[rec]:
                return True
            elif rec in player.gender and not gender_limit[rec]:
                print("Your class cannot use this card")
                return False
    else:
        return True


def hand_check(obj, player):
    equip_tup = (obj.name, obj.battle_modifier)
    if obj.hands == 2:
        if player.right_hand is None and player.left_hand is None:
            player.right_hand = equip_tup
            player.left_hand = (obj.name, 0)
        elif player.hireling:
            player.hireling_hand = equip_tup
        else:
            print("you cannot equip this card.")
            player.equip()
    elif obj.hands == 1:
        if player.right_hand is None:
            player.right_hand = equip_tup
        elif player.left_hand is None:
            player.left_hand = equip_tup
        elif player.hireling:
            player.hireling_hand = equip_tup
        else:
            print("you cannot equip this card")
            player.equip()
    else:
        player.other_equips[obj.name] += obj.battle_modifier


def armor_check(obj, player):
    equip_tup = (obj.name, obj.battle_modifier)
    if player.armor is None:
        player.armor = equip_tup
    else:
        print("You cannot equip this card")
        player.equip()


def feet_check(obj, player):
    equip_tup = (obj.name, obj.battle_modifier)
    if player.feet is None:
        player.feet = equip_tup
    else:
        print("You cannot equip this card")
        player.equip()


def head_check(obj, player):
    equip_tup = (obj.name, obj.battle_modifier)
    if player.head is None:
        player.head = equip_tup
    else:
        print("You cannot equip this card")
        player.equip()


def big_check(obj, player):
    if not player.big:
        return True
    elif player.big and player.hireling:
        if player.hireling_hand is None:
            return True
        else:
            return False
    else:
        return False



def player_equip_check(obj, player):
    if isinstance(obj, models.Treasure):
        equip_tup = (obj.name, obj.battle_modifier)
        # Big check
        big_chk = big_check(obj, player)
        if not big_chk:
            print("This item is too big for you")
            player.equip()
        # Class check
        class_chk = class_check(obj, player)
        if not class_chk:
            player.equip()
        # Race Check
        race_chk = race_check(obj, player)
        if not race_chk:
            player.equip()
        # Gender Check
        gend_chk = gender_check(obj, player)
        if not gend_chk:
            player.equip()
        # Start equipping
        if obj.card_type == 'Weapon':
            hand_check(obj, player)
        elif obj.card_type == 'Armor':
            if obj.feet:
                feet_check(obj, player)
            elif obj.head:
                print('checking helmet')
                head_check(obj, player)
            elif obj.armor:
                print('checking armor')
                armor_check(obj, player)
        elif obj.card_type == 'Item':
            if obj.name in ['Really Impressive Title','Singing & Dancing Sword','Kneepads Of Allure']:
                player.other_equips.append(equip_tup)
            elif obj.name == 'Hireling':
                player.hireling = True
            else:
                print("You cannot equip this card")
                player.equip()
        else:
            print("Card cannot be equipped")
    elif isinstance(obj, models.Door):
        print("You have a door card!")
    else:
        print("I do not recognize this card. Try again.")
        return False