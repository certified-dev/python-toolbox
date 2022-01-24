import time

from tools import txt_grabber, web_img_dwnlder, array_collector, lottery, currency_converter


def loader():
    print('\n\n\n                               ______________________________________________________ ')
    print('                              |__________________[TOOLBOX-V1.0]______________________|')
    print('                              |______________________________________________________| \n\n')
    time.sleep(3)
    print('\n\n\n                                            LOADING APP DATA........[35%]\n\n\n')
    time.sleep(2)
    print('\n\n\n                                           UPDATING LIBRARIES........[85%]\n\n\n')
    time.sleep(2)
    print('\n\n\n')


def activity():
    choice = int(input('''\n\n                          ____________[*] AVAILABLE TOOLS [*]_____________

                                         [1] Text Grabber

                                         [2] Web Image Scrapper 

                                         [3] Currency Converter 

                                         [4] Ticket Reservation 
                                         
                                         [5] Lottery

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
        currency_converter()
    elif choice == 4:
        array_collector()
    elif choice == 5:
        lottery()
    elif choice == 0:
        print('''\n\n\n\n\n\n\n\n\n     ---------Your Profile Details--------\n\n\n''')

        fr = open('com.karma.toolbox\profile.txt', 'r')
        print(fr.read())
        fr.close()

        print('         -----------------------------------------------------------------------')

        change_pword = input('  [*] Change Password (Y/N) to go back\n[*] Enter any other key to go back =>')
        if change_pword == 'y':

            check_pwd = open('com.karma.toolbox\pin.txt', 'r')
            read_pwd = check_pwd.read()
            check_pwd.close()

            curr_pwd = input('\nEnter Current Password: ')

            while read_pwd != curr_pwd:
                curr_pwd = input('\nincorrect password\n\n[*]Re-enter Current Password: ')
                if curr_pwd == read_pwd:
                    new_pwd = input('Enter New Password: ')
                    verify_pwd = input('Verify Password: ')
                    if new_pwd == verify_pwd:
                        open("com.karma.toolbox\pin.txt", 'w').write(verify_pwd)
                        time.sleep(2)
                        print('\nPassword Changed successfully\n')
                        time.sleep(2)
                        activity()
                    else:
                        print('\npassword mismatch\n')
            else:
                new_pwd = input('Enter New Password: ')
                verify_pwd = input('Verify Password: ')
                while new_pwd != verify_pwd:
                    print('\npassword mismatch')
                    new_pwd = input('\n[*]Re-enter New Password: ')
                    verify_pwd = input('[*]Verify Password: ')
                else:
                    open("com.karma.toolbox\pin.txt", 'w').write(verify_pwd)
                    time.sleep(2)
                    print('\nPassword Changed successfully\n')
                    time.sleep(2)
                    activity()
        else:
            activity()

    else:
        print('''\n\n\n\n

                                                          ---------LOGGING OUT--------  
        \n\n\n''')
        time.sleep(5)
        print('\n\n\n\n')


def about():
    print('about toolbox')
