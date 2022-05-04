#!/usr/bin/python3
# coding: utf-8
try:
    import requests
except:
    print(colored('requests module not installed."','red'))
    print(colored('Run "pip install requests" to install.','red'))
else:
    print(colored('[+] Checking internet...','green'))
    try:
        price = requests.get('https://api.bugzone.ir/G3nius/PremiumValue.txt').text
    except:
        print(colored('Check your internet connection and then retry.','red'))
    else:
        Clear()
        print(colored("It's only \x1b[6;32m" + price + "\x1b[0m per month!",'white'))
        print(colored("\n\nFor buy it send message with once of following liks:",'blue'))
        print(colored("\tWeb: https://bugzone.ir/",'magenta'))
        print(colored("\tE-Mail: admin@bugzone.ir",'magenta'))
        print(colored("\tInstagram: https://instagram.com/WitBlack80",'magenta'))
        print(colored("\tTelegram: https://t.me/WitBlack",'magenta'))
        print(colored("\tPhone: +98 9379446362\n\n",'magenta'))