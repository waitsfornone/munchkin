__author__ = 'time'
'''
This file provides the models for the card tables in the SQLite database

Tables:
Treasure
Door
'''

from peewee import *

db = SqliteDatabase('munchkin.db')


class DBModel(Model):
    class Meta:
        DATABASE = db


class Treasure(DBModel):
    name = CharField(max_length=255, unique=True)
    card_type = CharField(max_length=30)
    battle_modifier = TextField()
    price = IntegerField()
    hands = IntegerField()
    armor = BooleanField()
    feet = BooleanField()
    head = BooleanField()
    class_limit = CharField(max_length=25)
    race_limit = CharField(max_length=25)
    gender_limit = CharField(max_length=25)
    special_use = TextField()
    big = BooleanField()
    roll_modifier = IntegerField()
    expansion = CharField(max_length=50)


class Door(DBModel):
    name = CharField(max_length=255, unique=True)
    card_type = CharField(max_length=30)
    battle_modifier = TextField()
    special_use = TextField()
    roll_modifier = IntegerField()
    expansion = CharField(max_length=50)


# class Player(DBModel):
#     name = CharField(max_length=25, unique=True)
#     level = IntegerField()
#     gender = CharField(max_length=6)
#     left_hand = CharField(max_length=255)
#     right_hand = CharField(max_length=255)
#     head = CharField(max_length=255)
#     armor = CharField(max_length=255)
#     feet = CharField(max_length=255)
#     hireling = BooleanField()
#     hireling_hand = CharField(max_length=255)
#     big = BooleanField()
#     battle_power = IntegerField()
#     other_equips = TextField()
#     roll_modifier = IntegerField()
#     super_munchkin = BooleanField()
#     card_class = TextField()
#     affected_class = TextField()
#     halfbreed = BooleanField()
#     card_race = TextField(default='Human')
#     affected_race = TextField(default='Human')
#
#     @classmethod
#     def create_player(cls, name, level, race):
#         try:
#             cls.create(
#                 name=name,
#                 level=level,
#                 card_race=race,
#                 affected_race=race
#                 # gender=gender
#             )
#         except IntegrityError:
#             raise ValueError('Player already exists')


def initialize():
    db.connect()
    db.create_tables([Treasure], safe=True)
    db.close()
