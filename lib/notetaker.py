from peewee import *
from datetime import date

db = PostgresqlDatabase('notes1', user='postgres', password='',
                        host='localhost', port=5432)
db.connect()


class BaseModel(Model):
    """A base model that will use our Postgresql database. We don't have to do
    this, but it makes connecting models to our database a lot easier."""
    class Meta:
        database = db


class Notes(BaseModel):
    description = CharField()
    category = CharField()
    still_actual = CharField()

# if I have time need toplay with data format


# check it
db.create_tables([Notes])


# starting here functional part


def chose_action():
    action = input(
        "What do you want to do?: \n see all the notes (type: 1), \n delete notes (type: 2), \n create a note (type: 3) \n update existing note (type: 4)")
    if action == '1':
        see_all()
    elif action == '2':
        delete()
    elif action == '3':
        create()
    elif action == '4':
        update()
    else:
        print("You have a mistake. Please type carefully")


def see_all():
    print("see all")


def delete():
    print("delete")


def create():
    print("Please enter a new note: ")
    new_description = input("Please enter your note: ")
    new_category = input("Please enter category: ")
    new_still_actual = "Yes"

    new_note = Notes(description=new_description,
                     category=new_category, still_actual=new_still_actual)
    new_note.save()
    print(
        f"Here is your note with category {new_note.category}: {new_note.description}")


chose_action()


def update():
    print("update")


chose_action()
