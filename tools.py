import random
import urllib.request
from urllib import request


def array_collector():
    all_ticket_no = []
    gen_ticket_no = []
    total_ticket = 15
    n = 1
    while n <= total_ticket:
        numbers = random.randrange(1, 100)
        if numbers in gen_ticket_no:
            continue
        gen_ticket_no.append(numbers)
        n += 1

    while True:
        while True:
            try:
                user_ticket_no = int(input("\nChoose Any Number From 1 to 99 => "))
                if user_ticket_no in gen_ticket_no:
                    while True:
                        try:

                            for x in range(1, 100):
                                if x in gen_ticket_no:
                                    continue
                                all_ticket_no.append(x)
                            print('Ticket No', user_ticket_no, 'is not available\nHere are The available numbers\n',
                                  all_ticket_no)
                            break
                        except ValueError:
                            print('\n             WARNING:enter a valid number!!!\n')
                else:
                    gen_ticket_no.append(user_ticket_no)
                    print('You Have Selected Ticket No', user_ticket_no)
                break
            except ValueError:
                print('             WARNING:enter a valid number!!!\n')


def lottery():
    winning_no = []

    # for i in range(1, 7):
    while len(winning_no) < 6:
        n = random.randint(1, 100)
        if n not in winning_no:
            winning_no.append(n)

    print('enter 6 winning numbers: \n')
    user_numbers = []
    while len(user_numbers) < 6:
        k = (int(input('=> ')))
        if k not in user_numbers:
            user_numbers.append(n)
        else:
            print('number aleady chosen \n')

    j = 0
    for n in winning_no:
        if n in user_numbers:
            j += 1

    if j > 5:
        print('\nyou WIN!!!\n')
        print('WINNING-NUMBERS', winning_no)
        print('YOUR-NUMBERS', user_numbers)
    else:
        print('\nyou LOSE!!!\n')
        print('WINNING-NUMBERS', winning_no)
        print('YOUR-NUMBERS', user_numbers)


def web_img_dwnlder(url):
    name = random.randrange(1, 100)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)


def currency_converter():
    while True:
        dollar_price_in_naira = 375
        dollar_price_of_one_btc = 56908
        choice = int(input('''
                                            [1] US Dollar To Naira

                                            [2] Bitcoin to Naira

                                            [3] Satoshi to Naira

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


def txt_grabber(txt_url):
    response = request.urlopen(txt_url)
    txt = response.read
    txt_str = str(txt)
    lines = txt_str.split("\\n")
    saved_txt = r'text.txt'
    fw = open(saved_txt, 'w')
    for line in lines:
        fw.write(line + '\n')
        fw.close()
