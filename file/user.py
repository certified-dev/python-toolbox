import datetime
import os
import time
from tools import *
from snippets import activity


def register():
    if not os.path.exists('com.karma.toolbox'):
        os.mkdir('com.karma.toolbox')
    full_name = input('Full Name: ')
    dob = input('Birth Date In (YYYY-MM-DD) Format : ')

    fw = open('com.karma.toolbox\profile.txt', 'x')
    fw.write('                    NAME        : ' + full_name)
    fw.write('\n                    D.O.B       : ' + str(dob))
    fw.write('\n                    RELIGION    : ' + input('Religion: '))
    fw.write('\n                    OCCUPATION  : ' + input('Occupation: '))
    fw.write('\n                    NATIONALITY : ' + input('Nationality: '))

    sex = input('Sex:     Enter  M for Male Or F for Female \n'
                '=> ')
    if sex == 'm':
        fw.write('\n                    SEX         : Male')
    elif sex == 'f':
        fw.write('\n                    SEX         : Female')
    else:
        fw.write('\n                    SEX         : Unknown')
    fw.write('\n                    ADDRESS     : ' + input('Home Address: '))
    fw.write('\n                    PHONE NO    : ' + input('Telephone No: '))
    fw.write('\n                    EMAIL       : ' + input('Email: '))
    fw.close()

    save_dob = open('com.karma.toolbox/dob.txt', 'x')
    save_dob.write(dob)
    save_dob.close()

    usr_no = random.randrange(1, 1000)
    username = str(full_name.split()[0]) + str(usr_no)
    open('com.karma.toolbox\moniker.txt', 'w').write(username)

    if os.path.exists('com.karma.toolbox\profile.txt'):
        file = open('com.karma.toolbox\moniker.txt', 'r')
        print('\n\n\n\n\n\n\n\n                      WELCOME!!! ', file.read(), '\n')
        file.close()

        choose_pin = open('com.karma.toolbox\pin.txt', 'x')
        print('[*] Choose Password to Continue: ')
        pin = input('=> ')
        choose_pin.write(pin)
        choose_pin.close()

        pin1 = input('Verify Your Password => ')
        if pin == pin1:
            choose_security_question = int(input('\nChoose Your Security Question And Input Your Answer\n'
                                                 '''        1: Best Friends Name '''
                                                 '''         2: Favorite Color'''
                                                 '''        3: Pet Name'''
                                                 '''=> '''))
            if choose_security_question == 1:
                open('com.karma.toolbox\seq_choice.txt', 'x').write('1')
                print("Best friend's name?")
            elif choose_security_question == 2:
                open('com.karma.toolbox\seq_choice.txt', 'x').write('2')
                print('Favorite color?')
            elif choose_security_question == 3:
                open('com.karma.toolbox\seq_choice.txt', 'x').write('3')
                print("Pet's name?")

            open('com.karma.toolbox\security.txt', 'x').write(input('\nAnswer=> '))

            print('\n\n\n\n\n          << User Account Created Successfully!!! >>>\n\n')
            time.sleep(3)
            log_time = time.ctime()
            print('\n\n\n\n\n     --------------------User logged in @ : ' + str(log_time) + '--------------------\n')
            open('com.karma.toolbox\log.txt', 'x').write(log_time + '\n')
            activity()


def incorrect_password(pin):
    print('[*] Forgotten Your Password????\n[*]Press Y to View Password or Re-enter Password:')
    passcode = input('=> ')

    if passcode == 'y':
        try:
            check_seq = open('com.karma.toolbox\seq_choice.txt', 'r')
            seq = int(check_seq.read())
            check_seq.close()

            check_new = open('com.karma.toolbox\security.txt', 'r')
            check_new1 = check_new.read()
            check_new.close()

            if seq == 1:
                seq_ans = input('Best Friend Name => ')
                while seq_ans != check_new1:
                    seq_ans = input('\nWrong answer\nBest Friend Name => ')
                    if seq_ans == check_new1:
                        view_pass = open('com.karma.toolbox\pin.txt', 'r')
                        print('\npassword => \n', view_pass.read(), '\n')
                        view_pass.close()
                        break
                else:
                    view_pass = open('com.karma.toolbox\pin.txt', 'r')
                    print('password => \n', view_pass.read(), '\n')
                    view_pass.close()

            elif seq == 2:
                seq_ans = input('Favorite Color => ')
                while seq_ans != check_new1:
                    seq_ans = input('\nWrong answer\nFavorite Color => ')
                    if seq_ans == check_new1:
                        view_pass = open('com.karma.toolbox\pin.txt', 'r')
                        print('\password => \n', view_pass.read(), '\n')
                        view_pass.close()
                        break
                else:
                    view_pass = open('com.karma.toolbox\pin.txt', 'r')
                    print('Here is your password\n', view_pass.read(), '\n')
                    view_pass.close()

            elif seq == 3:
                seq_ans = input("Pet's Name => ")
                while seq_ans != check_new1:
                    seq_ans = input("\nWrong answer\nPet's Name => ")
                    if seq_ans == check_new1:
                        view_pass = open('com.karma.toolbox\pin.txt', 'r')
                        print('\nHere is your password\n', view_pass.read(), '\n')
                        view_pass.close()
                        break
                else:
                    view_pass = open('com.karma.toolbox\pin.txt', 'r')
                    print('Here is your password\n', view_pass.read(), '\n')
                    view_pass.close()

            time.sleep(3)
            new_session()

        except FileNotFoundError:
            print('                           Sorry You Are Not A Registered User!!! ')
            print('          Please Enter Your details Correctly to Signup And Continue Using This Product \n')
            print('\n')
            register()

    elif passcode == pin:
        check_birthday()
        log_time = time.ctime()
        print('\n\n\n\n\n\n\n--------------------User logged in @ : ' + str(log_time) + '--------------------')
        open('com.karma.toolbox\log.txt', 'a').write(log_time + '\n')
        activity()


def new_session():
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
            print('Incorrect!!!\n')
            incorrect_password(pin)

    except FileNotFoundError as fnf:
        print('                           Sorry You Are Not A Registered User!!! ')
        print('          Please Enter Your details Correctly to Signup And Continue Using This Product\n\n')


def check_birthday():
    read_dob = open('com.karma.toolbox/dob.txt', 'r')
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
        birth_name = read_name.readline()[34:]
        read_name.close()
        if new_age[1:] == '1':
            print('\nHappy', str(age) + 'st', 'Birthday, Dear', birth_name, '      Wishing You Success\n')
            time.sleep(5)
        elif new_age[1:] == '2':
            print('\nHappy', str(age) + 'nd', 'Birthday, Dear', birth_name, '      Wishing You Success\n')
            time.sleep(5)
        elif new_age[1:] == '3':
            print('\nHappy', str(age) + 'rd', 'Birthday, Dear', birth_name, '      Wishing You Success\n')
            time.sleep(5)
        else:
            print('\nHappy', str(age) + 'th', 'Birthday, Dear', birth_name, '      Wishing You Success\n')
            time.sleep(5)
