import os
from termcolor import colored
from peewee import *
from datetime import date

db = PostgresqlDatabase('notes', user='postgres', password='',
                        host='localhost', port=5432)


class BaseModel(Model):
    """A base model that will use our Postgresql database. We don't have to do
    this, but it makes connecting models to our database a lot easier."""
    class Meta:
        database = db


class notes(BaseModel):
    id = CharField(primary_key=True)
    description = CharField(unique=True)
    category = CharField(choices=True)
    deadline = DateField()
    importance = IntegerField
    #(validate_range(low=1, high=5))
    still_actual = BooleanField()


db.connect()
db.drop_tables([notes])
db.create_tables([notes])
