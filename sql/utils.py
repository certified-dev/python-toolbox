import sqlite3
from getpass import getpass

import bcrypt


def create_pwd(username, user_id):
    while True:
        password = getpass('Choose a password: ')
        password1 = getpass('Please confirm password: ')
        if password == password1:
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            with sqlite3.connect('db.sqlite') as db:
                cursor = db.cursor()
                data = (username, pw_hash, user_id[0])
                cursor.execute(
                    "UPDATE Users SET Username = ?, Password = ? WHERE Id = ? ", data)
                db.commit()
                cursor.close()
                break
        else:
            print('\nPasswords does not match\n')
