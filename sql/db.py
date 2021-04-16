import sqlite3

def add_db():
    with sqlite3.connect('sql/db.sqlite3') as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE Users 
                         ( Name TEXT,
                           Email TEXT UNIQUE,
                           Dob  DATE,
                           Address TEXT,
                           Occupation TEXT,
                           Phone INTEGER UNIQUE,
                           Username TEXT,
                           Password TEXT
                         );
                      ''')
        db.commit()
        cursor.close()


def collect(name, email, dob, address, occupation, phone):
    db = sqlite3.connect('sql/db.sqlite3')
    cursor = db.cursor()
    sqlite_insert_query = """INSERT INTO Users (name, email, dob, address, occupation, phone) 
                             VALUES (?, ?, ?, ?, ?, ?);"""
    data = (name, email, dob, address, occupation, phone)
    cursor.execute(sqlite_insert_query, data)
    db.commit()
    cursor.close()
    db.close()
