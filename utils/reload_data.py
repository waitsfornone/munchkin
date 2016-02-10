__author__ = 'tenders'

from peewee import *
import data_loader
import models

db = SqliteDatabase('munchkin.db')

db.connect()

models.Treasure.drop_table()

db.create_tables([models.Treasure], safe=True)

data_loader.load_treasure_data()