from user import *
from main import *
from getpass import getpass
import json

if os.path.exists('json/data.json'):
    print('\n')
    try:
        with open('json/data.json', 'r') as read_file:
            data = json.load(read_file)

        print('[*] Username:', data['username'])

        while True:
            password = getpass('[*] Password: ')

            if password == data['password']:
                session()
                break
            else:
                print('\nincorrect password!!!\n')
    except KeyError as error:
        print('                          You Are Not A Registered User!!!1 ')
        print(
            '\n           Enter Your details Correctly to Signup And Continue Using This Product\n')

else:
    print('\n                                 SIGN UP NOW!!! ')
    print('          Please Enter Your details Correctly to Continue Using This Product \n')
    register()
