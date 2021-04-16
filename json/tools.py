import random
import urllib.request
from urllib import request


def array_collector():
    gen_ticket_no = []
    while True:
        try:
            total_ticket = int(
                input('\nEnter Total Number of Booked Numbers:=>'))
            break
        except ValueError:
            print('             WARNING:enter a valid number!!!\\\n'
                  )
    n = 1
    while n <= total_ticket:
        numbers = random.randrange(1, 99)
        if numbers in gen_ticket_no:
            continue
        gen_ticket_no.append(numbers)
        n += 1
    print(gen_ticket_no)

    while True:
        try:
            user_ticket_no = int(
                input("\nChoose Any Number From 1 to 99 =>"))
            if user_ticket_no in gen_ticket_no:
                while True:
                    try:
                        print('Ticket No', user_ticket_no,
                              'Is Not Available\n')
                        print(
                            '        ----------Here Are The Available Numbers---------')

                        # list available ticket numbers
                        unavailable = []
                        for x in range(1, 99):
                            if x in gen_ticket_no:
                                continue
                            unavailable.append(x)
                        print(unavailable)

                        break
                    except ValueError:
                        print('\n             WARNING:enter a valid number!!!\n')
            elif len(str(user_ticket_no)) > 2:
                print('      WARNING:enter a valid selection!!!\n')
            else:
                gen_ticket_no.append(user_ticket_no)
                print('You Have Selected Ticket No', user_ticket_no)

        except ValueError:
            print('      WARNING:enter a valid number!!!\n')


def web_img_dwnlder(url):
    while True:
        try:
            name = random.randrange(1, 100)
            full_name = str(name) + '.jpg'
            urllib.request.urlretrieve(url, full_name)
        except urllib.error.URLError as error:
            print(error)
            break


def naira_converter():
    while True:
        dollar_price_in_naira = 375
        dollar_price_of_one_btc = 56908
        choice = int(input('''
                                            [1] US Dollar To Naira

                                            [2] Bitcoin Core to Naira

                                            [3] Satoshi Core to Naira

                                            [*] Any Other Number To Quit 
            => '''))
        if choice == 1:
            amount = int(input('enter amount of usd => '))
            total = amount * dollar_price_in_naira
            print('\n$', amount, ' = ', '#', total)
            print('\n')
            input('press enter to continue')

        elif choice == 2:
            amount = int(input('enter amount of btc => '))
            total = amount * dollar_price_of_one_btc * \
                dollar_price_in_naira
            print('\n')
            print(amount, 'btc', ' = ', '#', total)
            print('\n')
            input('press enter to continue')
        elif choice == 3:
            pass
        else:
            break


def txt_grabber(txt_url):
    while True:
        response = request.urlopen(txt_url)
        txt = str(response.read)
        lines = txt.split("\\n")
        saved_txt = r'text.txt'
        fw = open(saved_txt, 'w')
        for line in lines:
            fw.write(line + '\n')
            fw.close()
