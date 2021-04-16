import os
import time
import sys
from getpass import getpass

from db import *


class Main:
    def register(self):
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
        new_username = str(input('Enter Preferred Username: '))

        # check if username is available
        db = sqlite3.connect('sql/db.sqlite3')
        cursor = db.cursor()
        cursor.execute("SELECT username FROM Users")
        records = cursor.fetchall()
        record = str(records)
        cursor.close()
        db.close()
        if new_username in record:
            # -------------username is not available-------------------
            print('Username not available')
        pwd()
        print('\n')
        print('\nRegistering User [20%]')
        print('\nSetting Up Database [40%]')
        print('\nSaving User Instanse [60%]')
        print('\nLaunching Application [80%]')
        session()

    def incorrect_pwd(self):
        with sqlite3.connect('db/db.sqlite') as db:
            # -------------get username from db via win_name---------------------------
            cursor = db.cursor()
            cursor.execute(
                "SELECT Username FROM Users Where Username = ?", username)
            record = cursor.fetchone()
            username = record[0]
            user_id = [username]

            password = getpass('[*] Password: ')
            # ---------------fetch password from db via username---------------------------
            cursor.execute(
                "SELECT Password FROM Users WHERE Username = ?", username)
            result = cursor.fetchone()
            password1 = result[0]
            cursor.close()
            if password == password1:
                session()
            else:
                print('\n    Wrong password!!!\n')
                password = getpass('[*] Password: ')
                cursor = db.cursor()
                # ---------------fetch password from db via username--------------------------
                cursor.execute(
                    "SELECT Password FROM Users WHERE Username = ?", username)
                result = cursor.fetchone()
                password2 = result[0]
                if password == password2:
                    session()
                else:
                    print('\n     Wrong password!!!\n')
                    asked = input('Forgotten Password? (y/n): \n')
                    if asked == 'y':
                        print(
                            '[*] contact us on toolbox_team@dev_org.com to retrieve password')
                        time.sleep(5)
                    elif asked == 'n':
                        incorrect_pwd()
                    else:
                        print('enter a valid option!!!!\n')
                        incorrect_pwd()

    def main(self):
        choice = int(input('''
                                                    [1] Login

                                                    [2] Sign Up
                    = > '''))
        if choice == 1:
            try:
                username = input('Enter username')
                password = getpass('[*] Password: ')
                with sqlite3.connect('db.sqlite') as db:
                    cursor = db.cursor()
                    cursor.execute(
                        "SELECT Password FROM Users WHERE Username = ?", username)
                    result = cursor.fetchone()
                    password1 = result[0]
                    if password == password1:
                        session()
                    else:
                        print('')
                        print('    Wrong password!!!\n')
                        self.incorrect_pwd()
            except sqlite3.Error as error:
                print(error)
                print('                          You Are Not A Registered User!!! ')
                print(
                    '\n           press enter to continue\n')
                self.register()
        elif choice == 2:
            self.register()


if __name__ == "__main__":
    run = Main()
    run.main()
