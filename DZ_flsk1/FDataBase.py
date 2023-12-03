import sqlite3
import time
import math


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []

    def add_course(self, title, text, url):
        try:
            self.__cur.execute("SELECT COUNT() as 'count' FROM cours WHERE url LIKE ?", (url,))
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('Такой курс уже существует')
                return False

            tm = math.floor(time.time())
            self.__cur.execute('INSERT INTO cours VALUES(NULL, ?, ?, ?, ?)', (title, text, url, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления курса' + str(e))
            return False
        return True

    def get_course(self, course_id):
        try:
            self.__cur.execute(f'SELECT title, text FROM cours WHERE id={course_id}')
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка получения курса из БД' + str(e))
        return False, False

    def get_course_anonce(self):
        try:
            self.__cur.execute(f'SELECT id, title, text FROM cours')
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка получения курсов в БД' + str(e))

        return []


