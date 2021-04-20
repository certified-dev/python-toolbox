import os
import time
from getpass import getpass

from db import *
from main import session
from utils import create_pwd


class Main:

    def register(self):
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

        print('\n')
        print('\nRegistering User [20%]')
        print('\nSetting Up Database [40%]')
        print('\nSaving User Instance [60%]')
        print('\nLaunching Application [80%]')
        session(new_username)

    def main(self):
        if not os.path.exists('db.sqlite'):
            self.register()
        else:
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
                            password = cursor.fetchone()
                            cursor.close()

                            if password:
                                break
                            else:
                                print('\nIncorrect username\n')

                    while True:
                        password1 = getpass('[*] Password: ')
                        if password[0] == password1:
                            session(login)
                            break
                        else:
                            print('\n    Wrong password!!!\n')

                except sqlite3.Error as error:
                    print(error)
                    print('                          You Are Not A Registered User!!! ')
                    print('\n           press enter to continue\n')
                    self.register()
            elif choice == 2:
                self.register()


if __name__ == "__main__":
    run = Main()
    run.main()
