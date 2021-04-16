from tools import txt_grabber, web_img_dwnlder, usd_to_naira, btc_to_naira, array_collector
from user import *
import time
import os
from snippets import loader as init

init()
if os.path.exists('com.karma.toolbox\profile.txt'):
    try:
        file = open('com.karma.toolbox\moniker.txt', 'r')
        print('                      Welcome ', file.read())
        file.close()
        print('\n'
              '\n'
              '\n'
              '\n')
    except FileNotFoundError:
        print('                           Sorry You Are Not A Registered User!!! ')
        print('          Please Enter Your details Correctly to Signup And Continue Using This Product\n')
        print('\n')
        register()

    try:
        check_pin = open('com.karma.toolbox\pin.txt', 'r')
        pin = check_pin.read()
        check_pin.close()
        print('[*] Enter Password To Login:')
        passcode = input('=> ')
    except FileNotFoundError as fnf:
        print('                           Sorry You Are Not A Registered User!!! ')
        print('          Please Enter Your details Correctly to Signup And Continue Using This Product\n')
        print('\n')

    if passcode == pin:
        check_birthday()
        log_time = time.ctime()
        print('''










        ''')
        print('--------------------User logged in @ : ' + str(log_time) + '--------------------')
        open('com.karma.toolbox\log.txt', 'a').write(log_time + '\n')
        choice = int(input('''                     ____________[*] AVAILABLE TOOLS [*]_____________

                       [1] Text Grabber

                       [2] Web Image Scrapper 

                       [3] Usd/Btc To Naira Converter 

                       [4] Ticket Reservation 

                       [*] Enter 0 to view profile details 

         ----------------------------Enter Any Other Key to Logout-------------------------- 
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
            btc_choice = int(input('''
                                    [1] US Dollar To Naira 

                                    [2] Bitcoin Core to Naira 
 => '''))
            if btc_choice == 1:
                usd_to_naira(int(input('enter amount in dollar:$ ')))
            elif btc_choice == 2:
                btc_to_naira(input('enter bitcoin amount: '))
        elif choice == 4:
            array_collector()
        elif choice == 0:
            print('''














        -----------------------------Your Profile Details--------------------------
                   ''')

            fr = open('com.karma.toolbox\profile.txt', 'r')
            print(fr.read())
            fr.close()

            print('         -----------------------------------------------------------------------')

            change_pword = input('  [*] Change Password (Y/N)'
                                 '  =>')
            if change_pword is 'y':
                curr_pwd = input('Enter Current Password: ')
                check_pwd = open('com.karma.toolbox\pin.txt', 'r')
                curr_pword = check_pwd.read()
                check_pwd.close()

                if curr_pwd == curr_pword:
                    new_pwd = input('Enter New Password: ')
                    verify_pwd = input('Verify Password: ')
                    if new_pwd == verify_pwd:
                        open("com.karma.toolbox\pin.txt", 'w').write(verify_pwd)
                        time.sleep(2)
                        print('\nPassword Changed successfully\n')
                        time.sleep(2)
                        new_session()
                    else:
                        print('password does not match!!!')
                else:
                    print('incorrect password')
            else:
                pass
        else:
            print('''




                                        ---------LOGGING OUT--------  




            ''')
            time.sleep(5)
            print('\n')
            print('\n')
            print('\n')
            print('\n')
            new_session()

    else:
        print('Incorrect!!!\n')
        incorrect_password()
else:
    print('                                 SIGN UP NOW!!! ')
    print('          Please Enter Your details Correctly to Continue Using This Product \n')
    print('\n')
    register()
