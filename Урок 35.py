import sqlite3

# con = sqlite3.connect("profile.db")
# cur = con.cursor()
#
# cur.execute("""""")
# con.close()

# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()
# cur.execute("""CREATE TABLE IF NOT EXIST users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     summa REAL,
#     date BLOB
# )""")
# cur.execute("DROP TABLE users")

# with sqlite3.connect("user.db") as con:
#     cur = con.cursor()
# cur.execute("""
# CREATE TABLE IF NOT EXISTS person(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# phone BLOB NOT NULL DEFAULT "+790900000000",
# age INTEGER CHECK(age > 0 AND age < 100),
# email TEXT UNIQUE
# )""")
# cur.execute("""
# ALTER TABLE person
# RENAME TO person_table;
# """)

# cur.execute("""
# ALTER TABLE person_table
# ADD COLUMN address TEXT;
# """)

# cur.execute("""
# ALTER TABLE person_table
# RENAME COLUMN address TO home_address;
# """)

# cur.execute("""
# ALTER TABLE person_table
# DROP COLUMN home_address;
# """)

# cur.execute("""
# DROP TABLE person_table;
# """)

# with sqlite3.connect("db_3.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     SELECT *
#     FROM T1
#     ORDER BY FNAME
#     LIMIT 2, 5
#     """)
#
#     # res = cur.fetchall() # получили список в виде картежей
#     # print(res)
#
#     # for res in cur:
#     #     print(res)
#
#     res = cur.fetchone()
#     print(res)
#
#     res2 = cur.fetchmany(2)
#     print(res2)
#
#     res3 = cur.fetchall()  # получили список в виде картежей
#     print(res3)

cars = [
    ("BMW", 54000),
    ("Chevrolet", 46000),
    ("Daewoo", 38000),
    ("Citroen", 29000),
    ("Honda", 33000)
]

with sqlite3.connect("car.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS car(
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    )""")

    # cur.execute("INSERT INTO car VALUES(1,'Renault', 22000)")
    # cur.execute("INSERT INTO car VALUES(2,'Volvo', 29000)")
    # cur.execute("INSERT INTO car VALUES(3,'Mercedes', 57000)")
    # cur.execute("INSERT INTO car VALUES(4,'Bentley', 35000)")
    # cur.execute("INSERT INTO car VALUES(5,'Audi', 52000)")

    # for car in cars:
    #     cur.execute("INSERT INTO car VALUES(NULL, ?, ?)", car)

    # cur.executemany("INSERT INTO car VALUES(NULL, ?, ?)", cars)

    # cur.execute("UPDATE car SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})
    # cur.executescript("""
    # DELETE FROM car WHERE model LIKE 'B%';
    # UPDATE car SET price = price + 100
    # """)
