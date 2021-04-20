import datetime
import os
import time
from tools import *


def register():
    if not os.path.exists('com.karma.toolbox'):
        os.mkdir('com.karma.toolbox')
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    all_name = '%s, %s' % (last_name, first_name)
    fw = open('com.karma.toolbox\profile.txt', 'x')
    full_name = fw.write('                    NAME        : ' + all_name)
    dob = input('Birth Date In (YYYY-MM-DD) Format : ')
    open('com.karma.toolbox\seq.txt', 'w').write(dob)
    dob = fw.write('\n                    D.O.B       : ' + str(dob))
    religion = fw.write('\n                    RELIGION    : ' + input('Religion: '))
    occupation = fw.write('\n                    OCCUPATION  : ' + input('Occupation: '))
    nationality = fw.write('\n                    NATIONALITY : ' + input('Nationality: '))
    sex = input('Sex:     Enter  M for Male Or F for Female \n'
                '=> ')
    if sex == 'm':
        fw.write('\n                    SEX         : Male')
    elif sex == 'f':
        fw.write('\n                    SEX         : Female')
    else:
        fw.write('\n                    SEX         : Unknown')
    addr = fw.write('\n                    ADDRESS     : ' + input('Home Address: '))
    tel_no = fw.write('\n                    PHONE NO    : ' + input('Telephone No: '))
    email = fw.write('\n                    EMAIL       : ' + input('Email: '))
    fw.close()

    usr_no = random.randrange(1, 999)
    username = first_name + str(usr_no)
    open('com.karma.toolbox\moniker.txt', 'w').write(username)

    if os.path.exists('com.karma.toolbox\profile.txt'):
        file = open('com.karma.toolbox\moniker.txt', 'r')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n                      WELCOME!!! ', file.read())
        print('\n')
        file.close()

        choose_pin = open('com.karma.toolbox\pin.txt', 'x')
        print('[*] Choose Password to Continue: ')
        choose_pin.write(input('=> '))
        choose_pin.close()

        compare = open('com.karma.toolbox\pin.txt', 'r')
        pin1 = compare.read()
        compare.close()

        pin2 = input('Verify Your Password => ')
        print('\n')
        choose_security_question = int(input('Choose Your Security Question And Input Your Answer\n'
                                             '''        1: Best Friends Name?
        2: Favorite Color?
        3: Pet Name?
    => '''))
        if choose_security_question == 1:
            open('com.karma.toolbox\seq.txt', 'x').write('1')

        elif choose_security_question == 2:
            open('com.karma.toolbox\seq.txt', 'x').write('2')

        elif choose_security_question == 3:
            open('com.karma.toolbox\seq.txt', 'x').write('3')

        open('com.karma.toolbox\security.txt', 'x').write(input('=> '))

        if pin1 == pin2:
            print('''





            ''')
            print('\n          << User Account Created Successfully!!! >>>')
            print('\n')
            print('\n')
            time.sleep(4)
            log_time = time.ctime()
            print('''











                            ''')
            print('     --------------------User logged in @ : ' + str(log_time) + '--------------------\n')
            open('com.karma.toolbox\log.txt', 'x').write(log_time + '\n')
            choice = int(input('''                              ____________[*] AVAILABLE TOOLS [*]_____________

                                      [1] Text Grabber

                                      [2] Web Image Scrapper 

                                      [3] Currency To Naira Converter 

                                      [4] Ticket Reservation 

                                      [*] Enter 0 to view profile details 

    ----------------------------Enter Any Other Key to Logout-------------------------- 
  => '''))
            if choice == 1:
                txt_grabber(input('''

  Enter text full url path:
  => '''))
            elif choice == 2:
                print('')
                web_img_dwnlder(str('https://') + input('''
  Enter web address:
  => '''))
            elif choice == 3:
                print('')
                btc_choice = int(input('''
                                                        [1] USD To Naira 

                                                        [2] BTC to Naira 
  => '''))
                if btc_choice == 1:
                    usd_to_naira(int(input('enter amount in dollar: ')))
                elif btc_choice == 2:
                    btc_to_naira(input('enter bitcoin amount: '))
            elif choice == 4:
                array_collector()
            elif choice == 0:
                print('''












                  -----------------------------Your Profile Details----------------------------
                                       ''')

                fr = open('com.karma.toolbox\profile.txt', 'r')
                print(fr.read())
                fr.close()

                print('             -------------------------------------------------------------------')
                change_pword = input('Change Password (Y/N)')
                if change_pword is 'y':
                    curr_pwd = input('Enter Current Password')
                    check_pwd = open('com.karma.toolbox\pin.txt', 'r')
                    curr_pword = check_pwd.read()
                    check_pwd.close()

                    if curr_pwd == curr_pword:
                        new_pwd = input('Enter New Password: ')
                        verify_pwd = input('Verify Password: ')
                        if new_pwd == verify_pwd:
                            open('com.karma.toolbox\pin.txt', 'w').write(verify_pwd)
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
                print('\n'
                      '\n')
        else:
            print('Password Does Not Match!!!\n'
                  '\n')
            if os.path.exists('toolbox'):
                os.remove('com.karma.toolbox\moniker.txt')
                os.remove('com.karma.toolbox\pin.txt')
                os.remove('com.karma.toolbox\profile.txt')
                os.remove('com.karma.toolbox\security.txt')
                os.remove('com.karma.toolbox\log.txt')
                os.remove('com.karma.toolbox\seq.txt')
                os.rmdir('com.karma.toolbox')
                register()
            else:
                print('''




                                            ---------LOGGING OUT--------  




                ''')
                time.sleep(5)
                print('\n')
                print('\n')
                print('\n')
                print('\n')
                incorrect_password()
    else:
        print('                                   !!!SIGN-UP NOW!!!')
        print('                            You Are Not A Registered User!!! ')
        print('          Please Enter Your details Correctly to Signup And Continue Using Our Services \n')
        print('\n')
        print('\n')
        register()


def incorrect_password():
    global pin1
    try:
        check_pin = open('com.karma.toolbox\pin.txt', 'r')
        pin1 = check_pin.read()
        check_pin.close()

    except FileNotFoundError:
        print('                           Sorry You Are Not A Registered User!!! ')
        print('          Please Enter Your details Correctly to Signup And Continue Using This Product \n')
        print('\n')
        register()

    print('[*] Forgotten Your Password????\n   Press Y to View Password\n')
    print('[*] Re-enter Password:')
    passcode = input('=> ')

    if passcode is 'y':
        try:
            check_seq = open('com.karma.toolbox\seq.txt', 'r')
            seq = int(check_seq.read())
            check_seq.close()

            if seq == 1:
                check_new = open('com.karma.toolbox\security.txt', 'r')
                check_new1 = check_new.read()
                check_new.close()
                seq_ans = input('Best Friend Name =>')
                if seq_ans == check_new1:
                    view_pass = open('com.karma.toolbox\pin.txt', 'r')
                    print('Here is your password\n')
                    print(view_pass.read(), '\n')
                    view_pass.close()
                    new_session()
                else:
                    print('you didnt choose this security question')

            elif seq == 2:
                check_new = open('com.karma.toolbox\security.txt', 'r')
                check_new1 = check_new.read()
                check_new.close()
                seq_ans = input('Favorite Color =>')
                if seq_ans == check_new1:
                    view_pass = open('com.karma.toolbox\pin.txt', 'r')
                    print('Here is your password\n')
                    print(view_pass.read(), '\n')
                    view_pass.close()
                    new_session()
                else:
                    print('you didnt choose this security question')

            elif seq == 3:
                check_new = open('com.karma.toolbox\security.txt', 'r')
                check_new1 = check_new.read()
                check_new.close()
                seq_ans = input('Pet Name =>')
                if seq_ans == check_new1:
                    view_pass = open('com.karma.toolbox\pin.txt', 'r')
                    print('Here is your password\n')
                    print(view_pass.read(), '\n')
                    view_pass.close()
                    new_session()
                else:
                    print('you didnt choose this security question')

        except FileNotFoundError:
            print('                           Sorry You Are Not A Registered User!!! ')
            print('          Please Enter Your details Correctly to Signup And Continue Using This Product \n')
            print('\n')
            register()

    elif passcode == pin1:
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
                usd_to_naira(int(input('enter amount in dollar: ')))
            elif btc_choice == 2:
                btc_to_naira(input('enter bitcoin amount: '))
        elif choice == 4:
            array_collector()
        elif choice == 0:
            print('''














      ----------------------------Your Profile Details--------------------------''')

            fr = open('com.karma.toolbox\profile.txt', 'r')
            print(fr.read())
            fr.close()

            print('         -----------------------------------------------------------------------')
            change_pword = input('Change Password (Y/N)')
            if change_pword is 'y':
                curr_pwd = input('Enter Current Password')
                check_pwd = open('com.karma.toolbox\pin.txt', 'r')
                curr_pword = check_pwd.read()
                check_pwd.close()

                if curr_pwd == curr_pword:
                    new_pwd = input('Enter New Password: ')
                    verify_pwd = input('Verify Password: ')
                    if new_pwd == verify_pwd:
                        open('com.karma.toolbox\pin.txt', 'w').write(verify_pwd)
                        time.sleep(2)
                        print('''




                                                                        Password Changed successfully  




                                                ''')
                        time.sleep(2)
                        new_session()
                    else:
                        print('Password does not match')
                else:
                    print('Incorrect Password')
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


def new_session():
    try:
        check_pin = open('com.karma.toolbox\pin.txt', 'r')
        pin1 = check_pin.read()
        check_pin.close()
        print('[*] Re-enter Password:')
        passcode = input('=> ')
    except FileNotFoundError:
        print('                           Sorry You Are Not A Registered User!!! ')
        print('          Please Enter Your details Correctly to Signup And Continue Using This Product \n')
        print('\n')
        register()

    if passcode == pin1:
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
                usd_to_naira(int(input('enter amount in dollar: ')))
            elif btc_choice == 2:
                btc_to_naira(input('enter bitcoin amount: '))
        elif choice == 4:
            array_collector()
        elif choice == 0:
            print('''














      ----------------------------Your Profile Details--------------------------''')

            fr = open('com.karma.toolbox\profile.txt', 'r')
            print(fr.read())
            fr.close()

            print('         -----------------------------------------------------------------------')
            change_pword = input('Change Password (Y/N)')
            if change_pword is 'y':
                curr_pwd = input('Enter Current Password')
                check_pwd = open('com.karma.toolbox\pin.txt', 'r')
                curr_pword = check_pwd.read()
                check_pwd.close()

                if curr_pwd is curr_pword:
                    new_pwd = input('Enter New Password: ')
                    verify_pwd = input('Verify Password: ')
                    if new_pwd is verify_pwd:
                        open('com.karma.toolbox\pin.txt', 'w').write(verify_pwd)
                        time.sleep(2)
                        print('''




                                                                        Password Changed successfully  




                                                ''')
                        time.sleep(2)
                        new_session()
                    else:
                        print('Passwords does not Match')
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


def check_birthday():
    read_dob = open('com.karma.toolbox\seq.txt', 'r')
    saved_dob = read_dob.read()
    read_dob.close()
    mm_dd = saved_dob[5:]
    cur_date = datetime.date.today()
    new_date = str(cur_date)
    if mm_dd in new_date:
        birth_year = saved_dob[:4]
        age = int(cur_date.year - int(birth_year))
        new_age = str(age)
        read_name = open('com.karma.toolbox\profile.txt', 'r')
        birth_name = read_name.readline()
        read_name.close()
        referred = birth_name[34:]
        if new_age[1:] is '1':
            print('\nHappy', str(age) + 'st', 'Birthday, Dear', referred, '      Wishing You Success\n')
            time.sleep(5)
        elif new_age[1:] is '2':
            print('\nHappy', str(age) + 'nd', 'Birthday, Dear', referred, '      Wishing You Success\n')
            time.sleep(5)
        elif new_age[1:] is '3':
            print('\nHappy', str(age) + 'rd', 'Birthday, Dear', referred, '      Wishing You Success\n')
            time.sleep(5)
        else:
            print('\nHappy', str(age) + 'th', 'Birthday, Dear', referred, '      Wishing You Success\n')
            time.sleep(5)
    else:
        pass
