# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#


# print('hello git!!!')
# print('Hello GitHab!!!')


# print('строка в новом репозитории')


import os

from models.database import DATABASE_NAME, Session
import create_database1 as db_creator
from models.lesson import Lesson, association_table
from models.student import Student
from models.group import Group
from sqlalchemy import and_, or_, not_, desc

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()
    # print(session.query(Lesson).all())
    # print("*" * 60)
    #
    # for it in session.query(Lesson):
    #     print(it)
    # print("*" * 60)
    #
    # for it in session.query(Lesson):
    #     print(it.lesson_title)
    # print("*" * 60)
    #
    # print(session.query(Lesson).count())
    # print("*" * 60)
    #
    # print(session.query(Lesson).first())
    # print("*" * 60)
    #
    # for it in session.query(Lesson).filter(Lesson.id > 3):
    #     print(it)
    # print("*" * 60)
    #
    # for it in session.query(Lesson).filter(and_(Lesson.id > 3, Lesson.lesson_title.like('Ф%'))):
    #     print(it)
    # print("*" * 60)
    #
    # for it in session.query(Lesson).filter(or_(Lesson.id > 3, Lesson.lesson_title.like('Ф%'))):
    #     print(it)
    # print("*" * 60)
    #
    # for it in session.query(Lesson).filter(not_(Lesson.id > 3), not_(Lesson.lesson_title.like('Ф%'))):
    #     print(it)
    # print("*" * 60)
    #
    # for it, gr in session.query(Lesson.lesson_title, Group.group_name).filter(
    #         and_(association_table.c.lesson_id == Lesson.id,
    #              association_table.c.group_id == Group.id,
    #              Group.group_name == "MDA-7")):
    #     print(it, gr)
    #     print("*" * 60)
    #
    #     print(session.query(Lesson).filter(Lesson.lesson_title is not None).all())
    #     print("*" * 60)
    #
    #     print(session.query(Lesson).filter(Lesson.lesson_title.in_(["Математика", "Линейная алгебра"])).all())
    #     print("*" * 60)
    #
    #     print(session.query(Lesson).filter(Lesson.lesson_title.notin_(["Математика", "Линейная алгебра"])).all())
    #     print("*" * 60)
    #
    #     print(session.query(Student).filter(Student.age.between(16, 17)).all())
    #     print("*" * 60)
    #
    #     print(session.query(Student).filter(not_(Student.age.between(16, 17))).all())
    #     print("*" * 60)
    #
    #     for it in session.query(Student).filter(Student.age.like("1%")).limit(4).offset(3):
    #         print(it)
    #     print("*" * 60)
    #
    #     for it in session.query(Student).order_by(Student.surname):
    #         print(it)
    #     print("*" * 60)
    #
    #     for it in session.query(Student).order_by(desc(Student.surname)):
    #         print(it)
    #     print("*" * 60)
    #
    #     for it in session.query(Student).join(Group).filter(Group.group_name == "MDA-7"):
    #         print(it)
    #     print("*" * 60)
    # for it in session.query(Lesson):
    #     print(it.lesson_title)
    # print("*" * 60)
    #
    # i = session.query(Lesson).first()
    # i.lesson_title = "Информатика"
    # session.add(i)
    # session.commit()

    # for it in session.query(Lesson):
    #     print(it.lesson_title)
    # print("*" * 60)
    #
    # session.query(Lesson).filter(Lesson.lesson_title.like("%м%")).update(
    #     {'lesson_title': "M"}, synchronize_session="fetch")
    # session.commit()

    # for it in session.query(Lesson):
    #     print(it.lesson_title)
    # print("*" * 60)
    #
    # session.add(Lesson(lesson_title="Математика"))
    # session.commit()

    for it in session.query(Lesson):
        print(it.lesson_title)
    print("*" * 60)

    i = session.query(Lesson).filter(Lesson.lesson_title == "М").first()
    session.delete(i)
    session.commit()

    for it in session.query(Lesson):
        print(it.lesson_title)
    print("*" * 60)

