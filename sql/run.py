import os
import time
from getpass import getpass

import bcrypt

from db import *
from main import session
from utils import create_pwd


def register():
    if not os.path.exists('db.sqlite'):
        add_db()

    collect(
        input('Full Name: '),
        input('Email: '),
        input('Birth Date (YYYY-MM-DD): '),
        input('Home Address: '),
        input('Occupation: '),
        input('Telephone: '),
    )
    print('\n')
    time.sleep(2)

    # check if username is available
    db = sqlite3.connect('db.sqlite')
    cursor = db.cursor()
    cursor.execute("SELECT username FROM Users")
    records = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM Users")
    count = cursor.fetchone()
    cursor.close()
    db.close()

    taken = []

    for n in records:
        for i in n:
            taken.append(i)

    while True:
        new_username = str(input('Enter Preferred Username: '))
        if new_username not in taken:
            create_pwd(new_username, count)
            break
        else:
            print('\nUsername not available\n')

    print('\n\nRegistering User [20%]')
    print('\nSetting Up Database [40%]')
    print('\nSaving User Instance [60%]')
    print('\nLaunching Application [80%]')
    session(new_username)


class Main:

    def main(self):
        if not os.path.exists('db.sqlite'):
            register()
        else:
            while True:
                try:
                    choice = int(input('''
                                                                            [1] Login
    
                                                                            [2] Sign Up
                                            = > '''))
                    if choice == 1:
                        try:
                            while True:
                                login = input('Enter username: ')
                                with sqlite3.connect('db.sqlite') as db:
                                    cursor = db.cursor()
                                    cursor.execute(
                                        "SELECT Password FROM Users WHERE Username = ?", [login])
                                    password = cursor.fetchone()[0]
                                    cursor.close()

                                    if not password:
                                        print('\nIncorrect username\n')
                                    else:
                                        break

                            while True:
                                password1 = getpass('[*] Password: ')
                                if bcrypt.checkpw(password1.encode(), password):
                                    session(login)
                                    break
                                else:
                                    print('\n    Wrong password!!!\n')

                        except sqlite3.Error as error:
                            print(error)
                            print('      You Are Not A Registered User!!!\n           press enter to continue\n')
                            register()
                    elif choice == 2:
                        register()
                except ValueError:
                    print('enter a valid number')


if __name__ == "__main__":
    run = Main()
    run.main()
