#from clint.textui import colored, puts
import sys
from peewee import *
from datetime import date

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
    print("create database by executing command \" CREATE DATABASE notes1 \" at PostgreSQL console")
    print("to start PostgreSQL console type \"psql\" command at the system console")
    sys.exit(1)


class BaseModel(Model):
    class Meta:
        database = db


class Notes(BaseModel):
    title = CharField()
    description = CharField()

    # (unique=True)


db.create_tables([Notes])


def search():
    all_or_one = input(
        "If you want to see all the notes, type 1.\nIf you want to find one note by title, type 2: \n")
    if all_or_one == "1":
        search_note = Notes.select()
        for note in search_note:
            print("Your notes are\n")
            print(note.title, note.description)
            print()
        return True
        # return stops the loop. If there is no return the function
    elif all_or_one == "2":
        title_search = input("Please enter the title: ")
        search_results = Notes.select().where(Notes.title == title_search)
        for note in search_results:
            print()
            print("Your note: "+note.description + ".\n")
            print()
        return True
    else:
        print()
        print("You input invalid value. Try one more time, please")
        print()
        return True
    # function returns true to continue, false to exit the program


def delete():
    what_to_delete = input(
        "Please enter the title of the note you want to delete: ")
    delete_title = Notes.get(Notes.title == what_to_delete)
    delete_title.delete_instance()
    print()
    print(f"Your note with title \"{what_to_delete}\" has been deleted")
    print()
    return True


def create():
    new_title = input("Please enter a title: ")
    new_description = input("Please enter a note: ")
    new_note = Notes(description=new_description,
                     title=new_title)
    new_note.save()
    print()
    print(
        f"Here is your note with title: \"{new_note.title}\": {new_note.description}")
    print()
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
        print()
        print(
            f"Note \"{update_title.description}\" successfully updated from  title \"{chose_title}\" to title \"{new_title}\"")
        print()
        return True
    elif update == "2":
        chose_description = input(
            "What note you would like to update: ")
        new_description = input("Please enter a new note: ")
        update_description = Notes.get(Notes.description == chose_description)
        update_description.description = new_description
        update_description.save()
        print()
        print(
            f"Successfully updated note \"{chose_description}\" to note \"{new_description}\"")
        print()
        return True
    else:
        print("You typed smth wrong")
        return True


def chose_action():
    action = input(
        "\nWhat do you want to do?: \nsee all the notes (type: 1), \n delete notes (type: 2), \n create a note (type: 3) \n update existing note (type: 4) \n exit(type: 5) \n ")
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
