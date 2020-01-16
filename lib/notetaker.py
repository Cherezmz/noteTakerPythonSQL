import os
from termcolor import colored
from peewee import *
from datetime import date

db = PostgresqlDatabase('people', user='postgres', password='',
                        host='localhost', port=3000)

db.connect()


class BaseModel(Model):
    """A base model that will use our Postgresql database. We don't have to do
    this, but it makes connecting models to our database a lot easier."""
    class Meta:
        database = db


class Notes(BaseModel):
    id = CharField(primary_key=True)
    description = CharField(unique=True)
    category = CharField(choices=True)
    deadline = DateField()
    importance = IntegerField(validate_range(low=1, high=5))
    still_actual = BooleanField()


db.drop_tables([Notes])
db.create_tables([Notes])
