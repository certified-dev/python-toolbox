import time
import sqlite3
from tools import *
import os
import datetime
from getpass import getpass


def session():
    time.sleep(5)
    print('\nInitializing Aplication [85%]')
    print('\nLoading Tools components [99%]')
    time.sleep(1)
    print('\n')
    check_birthday()
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

            with sqlite3.connect('db/db.sqlite') as db:
                if edit == '1':
                    cursor = db.cursor()

                    # cursor.execute(
                    #     "SELECT Occupation FROM Users where Username = ?", os.getlogin())
                    # former_occupation = cursor.fetchone()
                    # print(former_occupation[0])

                    new_edit = input('Occupation: ')
                    var_new_edit = [new_edit, username]
                    cursor.execute(
                        "UPDATE Users SET Occupation = ? where Username = ?", var_new_edit)
                    print('\nsaved')
                    db.commit()
                    cursor.close()

                elif edit == '2':
                    cursor0 = db.cursor()

                    # cursor0.execute(
                    #     "SELECT Telephone FROM Users where Username = ?", os.getlogin())
                    # former_no = cursor0.fetchone()
                    # print(former_no[0])

                    new_edit = input('Telephone: ')
                    var_new_edit = [new_edit, username]
                    cursor0.execute(
                        "UPDATE Users SET Phone = ? where Username = ?", var_new_edit)
                    print('\nsaved')
                    db.commit()
                    cursor0.close()

                elif edit == '3':
                    cursor1 = db.cursor()
                    cursor1.execute(
                        "SELECT Username FROM Users where Username = ?", username)
                    record = cursor1.fetchone()
                    username = record[0]
                    user_id = [username]
                    cursor1.close()

                    old_pwd = input('Current password: ')
                    cursor2 = db.cursor()
                    cursor2.execute(
                        "SELECT Password FROM Users WHERE Username = ?", username)
                    result = cursor2.fetchone()
                    db_pwd = result[0]
                    cursor2.close()

                    if old_pwd == db_pwd:
                        new_pwd = getpass('New password: ')
                        check_new_pwd = getpass('Verify new password: ')
                        if new_pwd == check_new_pwd:

                            var_set_pwd = [check_new_pwd, username]
                            cursor3 = db.cursor()
                            cursor3.execute(
                                "UPDATE Users SET Password = ? WHERE Username = ?", var_set_pwd)
                            db.commit()
                            cursor3.close()
                            print('\nPassword Changed successfully!!!\n')
                            time.sleep(2)
                            session()
                        else:
                            print('Passwords does not match!!!')
                    else:
                        print('Current password incorrect!!!')


def check_birthday():
    with sqlite3.connect('db/db.sqlite') as db:
        cursor = db.cursor()
        cursor.execute("SELECT Dob FROM Users where Username = ?", username)
        record = cursor.fetchone()
        saved_dob = record[0]
        cursor.close()

        mm_dd = saved_dob[5:]
        cur_date = datetime.date.today()
        new_date = str(cur_date)
        if mm_dd in new_date:
            birth_year = saved_dob[:4]
            age = int(cur_date.year - int(birth_year))
            new_age = str(age)

            cursor1 = db.cursor()
            cursor1.execute(
                "SELECT Name FROM Users where Username = ?", username)
            read_name = cursor1.fetchone()
            referred = read_name[0]
            cursor1.close()

            if new_age[1:] == '1':
                print('\nHappy', str(age) + 'st', 'Birthday, Dear',
                      referred, 'Wishing You Success\n')
                time.sleep(5)
            elif new_age[1:] == '2':
                print('\nHappy', str(age) + 'nd', 'Birthday, Dear',
                      referred, 'Wishing You Success\n')
                time.sleep(5)
            elif new_age[1:] == '3':
                print('\nHappy', str(age) + 'rd', 'Birthday, Dear',
                      referred, 'Wishing You Success\n')
                time.sleep(5)
            else:
                print('\nHappy', str(age) + 'th', 'Birthday, Dear',
                      referred, 'Wishing You Success\n')
                time.sleep(5)
        else:
            pass
