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
    description = CharField()
    category = CharField()
    still_actual = CharField()

# if I have time need to play with data format


db.create_tables([Notes])


# starting here functional part

def search():
    category_search = input("Please enter the category: ")
    search_results = Notes.select().where(Notes.category == category_search)
    for note in search_results:
        print("Your note: "+note.description + "." +
              " Is it still actual? " + note.still_actual+".")
    return True

# function returns true to continue, false to exit the program


def delete():
    delete_category = input(
        "Please enter the category you want to delete: ")
    delete_category = Notes.get(Notes.category == delete_category)
    delete_category.delete_instance()
    # it deletes but print not the name of category but a number
    print(f"Your note titled {delete_category} has been deleted")
    return True


def create():
    new_description = input("Please enter your note: ")
    new_category = input("Please enter category: ")
    new_still_actual = "Yes"
    new_note = Notes(description=new_description,
                     category=new_category, still_actual=new_still_actual)
    new_note.save()
    print(
        f"Here is your note with category {new_note.category}: {new_note.description}")
    return True


def update():
    update = input(
        "Please chose what you would like to update: \n category (print 1) \n note (print 2) \n if the note is still actual (print 3) \n")
    if update == "1":
        chose_category = input(
            "What category you would like to update: ")
        new_category = input("Please enter a new category: ")

        update_category = Notes.get(Notes.category == chose_category)

        # for note in update_category:
        print("d: "+update_category.description + " c:" +
              update_category.category + " a:" + update_category.still_actual)

        # update_category.update(category=new_category)
        update_category.category = new_category
        update_category.save()

        print(
            f"Successfully updated from from {chose_category} to {new_category}")
        return True
    elif update == "2":
        chose_description = input(
            "What note you would like to update: ")
        new_description = input("Please enter a new note: ")
        update_description = Notes.get(
            Notes.description == chose_description)
        update_description.description = new_description
        update_description.save()
        print(
            "Successfully updated")
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
