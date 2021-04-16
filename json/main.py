import time
import json
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
            with open('json/data.json', 'r') as read_file:
                data = json.load(read_file)

            if edit == 1:
                pass
            elif edit == 2:
                pass
            elif edit == 3:
                pass
            elif edit == 4:
                pass


def check_birthday():
    with open('json/data.json', 'r') as read_file:
        data = json.load(read_file)

    referred = data['name']
    mm_dd = data['birthdate'][5:]
    new_date = str(datetime.date.today())

    if mm_dd in new_date:
        birth_year = data['birthdate'][:4]
        age = int(cur_date.year - int(birth_year))
        new_age = str(age)

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
