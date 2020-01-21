# from clint.textui import colored, puts
import sys
from peewee import *


db_name = 'notes1'
db_user = 'postgres'
db_password = ''

try:
    db = PostgresqlDatabase(db_name, user=db_user,
                            password=db_password, host='localhost', port=5432)
    db.connect()
except:
    print("ERROR: unable to connect to local PostgreSQL database '" +
          db_name + "' as user '" + db_user + "'")
    print("create database by executing command \"CREATE DATABASE notes1\" at PostgreSQL console")
    print("to start PostgreSQL console type \"psql\" command at the system console")
    sys.exit(1)


class BaseModel(Model):
    class Meta:
        database = db


class Notes(BaseModel):
    title = CharField()
    description = CharField()


try:
    db.create_tables([Notes])
except:
    print("ERROR: unable to create table")
    sys.exit(1)


def search():
    all_or_one = input(
        "If you want to see all the notes, type 1.\nIf you want to find one note by title, type 2: \n")

    if all_or_one == "1":
        search_note = Notes.select()
        num_results = len(search_note)
        if num_results == 0:
            print("no notes found")
        else:
            print("found " + str(num_results) + " notes:\n")
            print("title | description\n")
            print("--------------------\n")
            for note in search_note:
                print(note.title + " | " + note.description)
            print()

    elif all_or_one == "2":
        title_search = input("Please enter the title: ")
        search_results = Notes.select().where(Notes.title == title_search)
        num_results = len(search_results)
        # print("num_results: " + str(num_results))

        if num_results == 0:
            print("could not find a note with title \"" + title_search + "\"")
        else:
            print()
            # if somehow we have several notes with this title - print them all
            for note in search_results:
                print("Your note: "+note.description + ".\n")

    else:
        print()
        print("Invalid input: \"" + all_or_one + "\"\n")

    return True


def delete():
    what_to_delete = input(
        "Please enter the title of the note you want to delete: ")
    print()

    # delete first (if any) note with title what_to_delete
    # because 'get' returns only one note
    try:
        note = Notes.get(Notes.title == what_to_delete)
    except:
        print("could not find a note with title \"" + what_to_delete + "\"")
        return True

    note.delete_instance()
    print(f"Your note with title \"{what_to_delete}\" has been deleted")

    print()
    return True


def create():
    title = input("Please enter a title: ")

    try:
        note = Notes.get(Notes.title == title)
        print("A note with title \"" + title + "\" already exists\n")
        return True
    except:
        print()
        # print("could not find a note with title """ + what_to_delete + "\""")
        # return True

    description = input("Please enter a note: ")

    new_note = Notes(description=description,
                     title=title)
    new_note.save()
    print()
    print(
        f"Added note with title \"{new_note.title}\": {new_note.description}")
    print()
    return True


def update():
    update = input(
        "Please chose what you would like to update: \n title (type 1) \n note (type 2)\n")

    if ((update != "1") and (update != "2")):
        print("invalid input. Try one more time, please \n")
        return True

    title = input("Type the title of the note you would like to update: ")

    try:
        note = Notes.get(Notes.title == title)
    except:
        print("could not find a note with title \"" + title + "\"")
        return True

    if update == "1":
        new_title = input("Please enter a new title: ")
        note.title = new_title
        note.save()
        print()
        print(
            f"Note \"{note.description}\" successfully updated from  title \"{title}\" to title \"{new_title}\"")
        print()
        return True
    elif update == "2":
        new_description = input("Please enter new note: ")
        note.description = new_description
        note.save()
        print()
        print(
            f"Successfully updated note titled \"{title}\" to \"{new_description}\"")
        print()
        return True
    else:
        print("invalid input. Try one more time, please \n")
        return True


def chose_action():
    action = input(
        "\nWhat do you want to do?\n see all the notes (type: 1),\n delete notes (type: 2),\n create a note (type: 3)\n update existing note (type: 4)\n exit (type: 5) \n ")
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
    # try:
    cont = chose_action()
    # except:
    #    print("unexpected error occurred")
    #    sys.exit(1)
    #    break
    # print("loop")
    if not cont:
        break
