# import os
import psycopg2
from termcolor import colored
from peewee import *
from datetime import date

conn = psycopg2.connect(dbname='notes', user='postgres',
                        password='mypassword', host='localhost')
cursor = conn.cursor()


# db = PostgresqlDatabase('notes', user='postgres', password='',
#                         host='localhost', port=5432)


class BaseModel(Model):
    """A base model that will use our Postgresql database. We don't have to do
    this, but it makes connecting models to our database a lot easier."""
    class Meta:
        database = conn


class notes(BaseModel):
    # id = CharField(primary_key=True)
    description = CharField()
    category = CharField()
    deadline = DateField()
    importance = IntegerField()
    # (validate_range(low=1, high=5))
    still_actual = BooleanField()

# if I have time need toplay with data format


# conn.connect()
conn.drop_tables([notes])
conn.create_tables([notes])

# starting here functional part


def chose_action():
    action = input("What do you want to do: \n see notes (type: see), \n delete notes (type: delete), \n create note (type: create) \n update existing note (type: update)\n ")
    if action == 'see':
        def see_notes():

            # cur = db.cursor()
            cursor.execute("select description from notes")
            records = cursor.fetchall()

        #     rows = cur.fetchall()

        # for r in rows:
            print(records)


# cur.close()
# db.commit()

#    elif action == 'delete':
#         print("delete")
#     elif action == 'create':
#         print("create")
#     elif action == 'update':
#         print("update")
#     else:
#         print("You have a mistake. Please type carefully")


chose_action()

# NoteTaker

# str(input("Enter your username: "))

#     your_notes = NoteTaker.select().where(NoteTaker.user == name).count()
#     if your_notes >= 1:
#         view_note(name)
#     else:
#         print("Youve got 0 notes!")
#         create_note(name)
# elif note == 'create new note':
#     create_note(name)
