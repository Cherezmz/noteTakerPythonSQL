from colorama import Fore, Back, Style
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


db.create_tables([Notes])


# starting here functional part


def chose_action():
    action = input(
        "What do you want to do?: \n see all the notes (type: 1), \n delete notes (type: 2), \n create a note (type: 3) \n update existing note (type: 4) \n exit(type: 5) \n ")
    if action == '1':
        see_all()
    elif action == '2':
        delete()
    elif action == '3':
        create()
    elif action == '4':
        update()
    elif action == '5':
        go_out()
    else:
        print("You have a mistake. Please type carefully")


def see_all():
    category_search = input("Please enter the category: ")
    search_results = Notes.select().where(Notes.category == category_search)
    for note in search_results:
        print("Your note: "+note.description + "." +
              " Is it still actual? " + note.still_actual+".")


# one_more = input("Do you want to see smth else (y or n? ")
# if one_more == "y":
#     see_all()
# elif one_more == "n":
#     chose_action()
# else:
#     print("You have a mistake. Please type carefully")


chose_action()


# search_word = input("Please enter a word for search \n ")
# search_result = Notes.select().where(
#     Notes.description.contains(f"{search_word}"))
# print(search_result)


#     search_word = input("Please enter a word for search")


# for notes in Notes.select().where(Notes.description == test)
# print(Notes.description)

# search_result = Notes.where(Notes.description.name.contains("{search_word}"))
# print(search_result)


def delete():
    print("delete")


def create():
    new_description = input("Please enter your note: ")
    new_category = input("Please enter category: ")
    new_still_actual = "Yes"

    new_note = Notes(description=new_description,
                     category=new_category, still_actual=new_still_actual)
    new_note.save()
    print(
        f"Here is your note with category {new_note.category}: {new_note.description}")


# chose_action()


def update():
    update = input(
        "Please chose what you would like to update: \n category (print 1) \n note (print 2) \n if the note is still actual (print 3) \n")
    if update == "1":
        chose_category = input(
            "What category you would like to update: ")
        new_category = input("Please enter a new category: ")
        update_category = Notes.get(Notes.category == chose_category)
        # for category in update_category:
        #     update_category.category = new_category
        update_category.save()
        print(
            f"Successfully updated from from {chose_category} to {new_category}")
    elif update == "2":
        chose_description = input(
            "What note you would like to update: ")
        new_description = input("Please enter a new note: ")
        update_description = Notes.get(Notes.description == chose_description)
        update_description.description = new_description
        update_description.save()
        print(
            f"Successfully updated from from {chose_description} to {new_description}")


chose_action()


def go_out():
    print("See you next time!")
    return True


chose_action()
see_all()
delete()
create()
update()
go_out()


# for filtering using still_active true
# User.select().where(User.active == True)

# random line
# LotteryNumber.select().order_by(fn.Random()).limit(5)
