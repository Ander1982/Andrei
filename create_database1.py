# from models1.database import create_db, Session
# from models1.lesson import Lesson
# from models1.student import Student
# from models1.group import Group
#
#
# def create_database(load_fake_data=True):
#     create_db()
#     if load_fake_data:
#         _load_fake_data(Session())
#
#
# def _load_fake_data(session):
#     ...


from models1.database import create_db, Session
from models1.lesson import Lesson
from models1.student import Student
from models1.group import Group


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    ...

