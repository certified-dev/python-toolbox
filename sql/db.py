import sqlite3


def add_db():
    with sqlite3.connect('db.sqlite') as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE Users 
                         ( Id INTEGER PRIMARY KEY AUTOINCREMENT,
                           Name TEXT,
                           Email TEXT UNIQUE,
                           Dob  DATE,
                           Address TEXT,
                           Occupation TEXT,
                           Phone INTEGER,
                           Username TEXT UNIQUE,
                           Password TEXT
                         );
                      ''')
        db.commit()
        cursor.close()


def collect(name, email, dob, address, occupation, phone):
    while True:
        try:
            db = sqlite3.connect('db.sqlite')
            cursor = db.cursor()
            sqlite_insert_query = """INSERT INTO Users (name, email, dob, address, occupation, phone) 
                                     VALUES (?, ?, ?, ?, ?, ?);"""
            data = (name, email, dob, address, occupation, phone)
            cursor.execute(sqlite_insert_query, data)
            db.commit()
            cursor.close()
            db.close()
            break
        except sqlite3.Error as error:
            print(error)
