__author__ = 'time'
"""
This file reads a .csv file and loads the cards into the Treasure table in the SQLite database.
File must be formatted as follows:

enter it here
"""

import csv
import models
from peewee import *


db = SqliteDatabase('munchkin.db')

def load_treasure_data():
    with open('treasure_data.csv', 'r') as dat:
        data = csv.DictReader(dat)
        data_list = []
        for row in data:
            data_list.append(row)

    with db.atomic():
        for dict in data_list:
            truthy_fields = ["armor", "feet", "head"]
            for k, v in dict.items():
                if k in truthy_fields:
                    if v == "1":
                        dict[k] = True
                    else:
                        dict[k] = False

             models.Treasure.create(**dict)

             created = models.Treasure.get(models.Treasure.name == dict["name"])

def load_door_data():
    pass

if __name__ == '__main__':
    db.connect()
    db.create_tables([models.Treasure], safe=True)