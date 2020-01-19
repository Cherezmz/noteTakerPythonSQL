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
    print("see all")


def search():
    category_search = input("Please enter the category: ")
    search_results = Notes.select().where(Notes.category == category_search)
    for note in search_results:
        print(note.category + note.description+note.still_actual)


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


chose_action()


def update():
    print("update")


def go_out():
    print("See you next time!")


chose_action()


# for filtering using still_active true
# User.select().where(User.active == True)

# random line
# LotteryNumber.select().order_by(fn.Random()).limit(5)
