# from colorama import Fore, Back, Style
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
    owner = CharField()
    title = CharField()
    description = CharField()

    # (unique=True)


# if I have time need to play with data format


db.create_tables([Notes])


# starting here functional part

def search():
    all_or_one = input(
        "If you want to see all the owner's notes, type 1.\nIf you want to find one note by title, type 2: \n")
    if all_or_one == "1":
        search_note = Notes.select().where(Notes.owner == "Igor")
    for note in search_note:
        print(note.title, note.description)
        # return True
        # return stops the loop. If there is no return the function
    elif all_or_one == "2":
        title_search = input("Please enter the title: ")
        search_results = Notes.select().where(Notes.title == title_search)
    for note in search_results:
        print("Your note: "+note.description + ".")
        return True
    else:
        print("You typed smth wrong")
        return True
    # function returns true to continue, false to exit the program


def delete():
    delete_title = input(
        "Please enter the title of the note you want to delete: ")
    delete_title = Notes.get(Notes.title == delete_title)
    delete_title.delete_instance()
    # it deletes but print not the name of category but a number
    print(f"Your note titled {delete_title} has been deleted")
    return True


def create():
    new_owner = "Igor"
    new_title = input("Please enter a title: ")
    new_description = input("Please enter a note: ")
    new_note = Notes(description=new_description,
                     title=new_title, owner=new_owner)
    new_note.save()
    print(
        f"{new_owner}, here is your note with title: \"{new_note.title}\": {new_note.description}")
    return True


def update():
    update = input(
        "Please chose what you would like to update: \n title (print 1) \n note (print 2)\n")
    if update == "1":
        chose_title = input(
            "What title you would like to update: ")
        new_title = input("Please enter a new title: ")
        update_title = Notes.get(Notes.title == chose_title)
        update_title.title = new_title
        update_title.save()
        print(
            f"Note \"{update_title.description}\" successfully updated from  title \"{chose_title}\" to title \"{new_title}\"")
        return True
    elif update == "2":
        chose_description = input(
            "What note you would like to update: ")
        new_description = input("Please enter a new note: ")
        update_description = Notes.get(Notes.description == chose_description)
        update_description.description = new_description
        update_description.save()
        print(
            f"Successfully updated note {chose_description} to note {new_description}")
        return True
    else:
        print("You typed smth wrong")
        return True


def chose_action():
    action = input(
        "What do you want to do?: \n see all the notes (type: 1), \n delete notes (type: 2), \n create a note (type: 3) \n update existing note (type: 4) \n exit(type: 5) \n ")
    if action == '1':
        return search()
    elif action == '2':
        return delete()
    elif action == '3':
        return create()
    elif action == '4':
        return update()
    elif action == '5':
        print("See you next time!")
        # raise SystemExit
        return False
    else:
        print("You have made a mistake. Please type carefully")
        return True


while True:
    cont = chose_action()
    # print("loop")
    if not cont:
        break
