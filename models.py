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
        database = db


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
    big = BooleanField(default=)
    roll_modifier = IntegerField()
    expansion = CharField(max_length=50)


class Door(DBModel):
    name = CharField(max_length=255, unique=True)
    card_type = CharField(max_length=30)
    battle_modifier = TextField()
    special_use = TextField()
    roll_modifier = IntegerField()
    expansion = CharField(max_length=50)
