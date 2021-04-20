import datetime
import sqlite3
import time
from getpass import getpass

from tools import *


def session(user):
    time.sleep(5)
    print('\nInitializing Aplication [85%]')
    print('\nLoading Tools components [99%]')
    time.sleep(1)
    print('\n')
    log_time = time.ctime()

    print('''

                                            ''')
    print('     --------------------User logged in @ : ' +
          str(log_time) + '--------------------\n')

    while True:
        choice = int(input('''                              ____________[*] AVAILABLE TOOLS [*]_____________

                                            [1] Text Grabber

                                            [2] Web Image Scrapper 

                                            [3] Currency To Naira Converter 

                                            [4] Ticket Reservation 

                                            [*] Enter 0 to Edit Your Details 

                        
                    => '''))
        if choice == 1:
            txt_grabber(input('''
        Enter text full url path:
        => '''))
        elif choice == 2:
            web_img_dwnlder(str('https://') + input('''
        Enter web address:
        => '''))
        elif choice == 3:
            naira_converter()

        elif choice == 4:
            array_collector()
        elif choice == 0:
            edit = input('''            What would you like to edit?
            
                            [1] Occupation
                            [2] Phone Number
                            [3] Password
                = > : ''')

            with sqlite3.connect('db.sqlite') as db:
                cursor = db.cursor()
                if edit == '1':
                    new_edit = input('Occupation: ')
                    data = [new_edit, user]
                    cursor.execute(
                        "UPDATE Users SET Occupation = ? where Username = ?", data)
                    print('\nsaved')

                elif edit == '2':
                    new_edit = input('Telephone: ')
                    data = [new_edit, user]
                    cursor.execute(
                        "UPDATE Users SET Phone = ? where Username = ?", data)
                    print('\nsaved')

                elif edit == '3':
                    old_pwd = input('Current password: ')
                    cursor.execute(
                        "SELECT Password FROM Users WHERE Username = ?", data)
                    db_pwd = cursor.fetchone()
                    print('\nsaved')

                db.commit()
                cursor.close()

                while True:

                    if old_pwd == db_pwd:
                        new_pwd = getpass('New password: ')
                        check_new_pwd = getpass('Verify new password: ')

                        if new_pwd == check_new_pwd:
                            data = [new_pwd, user]
                            cursor0 = db.cursor()
                            cursor0.execute(
                                "UPDATE Users SET Password = ? WHERE Username = ?", data)
                            db.commit()
                            cursor0.close()
                            db.close()
                            print('\nPassword Changed successfully!!!\n')
                            time.sleep(2)
                            break
                        else:
                            print('Passwords does not match!!!')
                    else:
                        print('Current password incorrect!!!')
