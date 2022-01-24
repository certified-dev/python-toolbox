from snippets import loader as init
from user import *

init()
if os.path.exists('com.karma.toolbox\profile.txt'):
    try:
        file = open('com.karma.toolbox\moniker.txt', 'r')
        print('                      Welcome ', file.read(), '\n')
        file.close()

        try:
            check_pin = open('com.karma.toolbox\pin.txt', 'r')
            pin = check_pin.read()
            check_pin.close()
            print('[*] Enter Password To Login:')
            passcode = input('=> ')

            if passcode == pin:
                check_birthday()
                log_time = time.ctime()
                print('\n\n\n\n\n\n--------------------User logged in @ : ' + str(log_time) + '--------------------')
                open('com.karma.toolbox\log.txt', 'a').write(log_time + '\n')
                activity()
            else:
                print('\nIncorrect password\n')
                incorrect_password(pin)

        except FileNotFoundError as fnf:
            print('                           Sorry You Are Not A Registered User!!! ')
            print('          Please Enter Your details Correctly to Signup And Continue Using This Product\n\n')

    except FileNotFoundError:
        print('                           Sorry You Are Not A Registered User!!! ')
        print('          Please Enter Your details Correctly to Signup And Continue Using This Product\n\n')
        register()
else:
    print('                           Sorry You Are Not A Registered User!!! ')
    print('          Please Enter Your details Correctly to Signup And Continue Using This Product\n\n')
    register()
