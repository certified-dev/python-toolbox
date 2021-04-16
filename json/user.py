from main import *
import os
import time
import sys
from getpass import getpass
import json


def register():
    global os_id

    def linux_test():
        assert ('linux' in sys.platform)

    try:
        linux_test()
    except AssertionError:
        print('windows detected\n')
        var = []
        new = sys.getwindowsversion()
        for x in new:
            var.append(x)
        a = str(var.pop())
        b = str(var.pop())
        c = str(var.pop())
        d = str(var.pop())
        e = str(var.pop())
        os_id = e + '.' + d + '.' + c + '.' + b + '.' + a
    else:
        os_id = os.getlogin()

    data = {}

    input(' Please enter your info correctly\n press any key to continue\n')

    data['UserID'] = os_id
    data['name'], data['email'] = input('Full Name: '), input('Email: ')
    data['address'], data['birthdate'] = input(
        'Home Address: '), input('Birth Date (YYYY-MM-DD): ')
    data['occupation'], data['telephone'] = input(
        'Occupation: '), input('Telephone: ')
    time.sleep(2)
    data['occupation'] = input('Enter A Username: ')

    time.sleep(2)
    password = str(getpass('Choose a password: '))
    password1 = str(getpass('Please confirm password: '))
    # -------------check if both entries match-----------------------
    while True:
        if password == password1:
            # -------------match-----------------------------
            data['password'] = password
            break
        else:
            # -------------no match-----------------------
            print('Passwords does not match')

    with open('json/data.json', 'w') as output:
        json.dump(data, output, indent=2)
    time.sleep(2)

    print('\n')
    print('\nRegistering User [20%]')
    print('\nSetting Up Database [40%]')
    print('\nSaving User Instanse [60%]')
    print('\nLaunching Application [80%]')
    session()
