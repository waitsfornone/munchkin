__author__ = 'time'

import models
import ast
import data_loader
from peewee import *

db = SqliteDatabase('munchkin.db')

db.connect()

card = models.Treasure.get(models.Treasure.name == "Staff Of Napalm")

cls_lim = ast.literal_eval(card.class_limit)

print(card.armor)