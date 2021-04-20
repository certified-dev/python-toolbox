import sqlite3
import time
from getpass import getpass


def create_pwd(username, user_id):
    while True:
        password = getpass('Choose a password: ')
        password1 = getpass('Please confirm password: ')
        if password == password1:
            with sqlite3.connect('db.sqlite') as db:
                cursor = db.cursor()
                data = (username, password, user_id[0])
                cursor.execute(
                    "UPDATE Users SET Username = ?, Password = ? WHERE Id = ? ", data)
                db.commit()
                cursor.close()
                break
        else:
            print('\nPasswords does not match\n')
