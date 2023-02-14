"""     libs    """
# external
from os import name,popen
from sys import version_info
# internal
from lib.packages.termcolor import colored
from lib.GPL.String_Workers import gpl_fix_spases
from lib.core.OS_Detector import OS

"""     Local variable      """
Banner_Version = None

"""     GPL     """

# Clear Page
#
# modules:
# import os
# from termcolor import colored
#
# version:
# 3
def gpl_clear(clear_on_unsuported_OS=True,on_unsuported_OS_text="New page is here:\n-----------------"):
    global OS
    if OS == 'Linux':
        print('\033c')
    elif OS == 'Windows':
        print(popen('cls').read())
    elif clear_on_unsuported_OS:
        print(colored(on_unsuported_OS_text, 'yellow'))
        print('\033c')



# Banner
#
# modules:
# from termcolor import colored
# import sys
# import os
#
# internal modules:
# gpl_fix_spases
# gpl_clear
#
# version:
# 1
def gpl_clear_and_banner(owners_text='WitBlack',field2_title='',field2_text='',field3_title='',field3_text='',license='FREE'): # Banner_Version shuild in globals
    global Banner_Version
    if not 'Banner_Version' in globals():
        raise Exception('Banner_Version not in globals. Run gpl_set_banner_verion first.')
    gpl_clear()
    Python_Version = str(version_info[0])
    if len(field3_title) > 31:
        field3_title = field3_title[:31]
    if len(field2_title) > 31:
        field3_title = field2_title[:31]
    print(colored(' _______________________________________________________________________', 'red'))
    print(colored('|', 'red') + colored(' ▒███▒ ▒████           █                ', 'magenta') + colored('  |','red') + colored(' Programmer info:          ', 'white') + colored('|', 'red'))
    print(colored('|', 'red') + colored('░█▒ ░█ █▒  ▓█          █                ', 'magenta') + colored('  |','red') + colored('---------------------------|', 'red'))
    print(colored('|', 'red') + colored('█▒          █ █▒██▒    █    █   █  ▒███▒', 'magenta') + colored('  |','red') + colored(' Programmed by WitBlack    ', 'green') + colored('|', 'red'))
    print(colored('|', 'red') + colored('█          ▒█ █▓ ▒█    █    █   █  █▒ ░█', 'magenta') + colored('  |','red') + colored(' Github ~>                 ', 'white') + colored('|', 'red'))
    print(colored('|', 'red') + colored('█   ██   ███░ █   █    █    █   █  █▒░  ', 'magenta') + colored('  |','red') + colored('Https://github.com/WitBlack', 'blue') + colored('|', 'red'))
    print(colored('|', 'red') + colored('█    █     ▓█ █   █    █    █   █  ░███▒', 'magenta') + colored('  |','red') + colored(' Website ~>                ', 'white') + colored('|', 'red'))
    print(colored('|', 'red') + colored('█▒   █      █ █   █         █   █     ▒█', 'magenta') + colored('  |','red') + colored('Https://BugZone.ir         ', 'blue') + colored('|', 'red'))
    print(colored('|', 'red') + colored('▒█░ ░█ █░  ▓█ █   █    █    █▒ ▓█  █░ ▒█', 'magenta') + colored('  |','red') + colored(' E-Mail ~>                 ', 'white') + colored('|', 'red'))
    print(colored('|', 'red') + colored(' ▒███▒ ▒████  █   █    █    ▒██▒█  ▒███▒', 'magenta') + colored('  |','red') + colored('admin@bugzone.ir           ', 'blue') + colored('|', 'red'))
    print(colored('|', 'red') + colored('                                 _________|___________________________|', 'red'))
    print(colored('|', 'red') + colored('________________________________|', 'red') + colored('                       ███           ', 'magenta') + colored('|', 'red'))
    print(colored('|', 'red') + colored(' Information :                  ', 'white') + colored('|', 'red') + colored(' ███████                 █           ', 'magenta') + colored('|', 'red'))
    print(colored('|', 'red') + colored('--------------------------------', 'red') + colored('|', 'red') + colored('    █                    █           ', 'magenta') + colored('|', 'red'))
    print(colored('|', 'red') + colored(' Python Version: ', 'blue') + colored(Python_Version + '              ', 'white') + colored('|','red') + colored('    █     ███    ███     █    ▒███▒  ', 'magenta') + colored('|', 'red'))
    print(colored('|', 'red') + colored(' LICENSE: ', 'blue') + colored(gpl_fix_spases(license, 22,overflow=False), 'white') + colored('|','red') + colored('    █    █▓ ▓█  █▓ ▓█    █    █▒ ░█  ', 'magenta') + colored('|', 'red'))
    print(colored('|', 'red') + colored(' VERSION: ', 'blue') + colored(gpl_fix_spases(Banner_Version, 22,overflow=False), 'white') + colored('|','red') + colored('    █    █   █  █   █    █    █▒░    ', 'magenta') + colored('|', 'red'))
    print(colored('|', 'red') + colored(' OS: ', 'blue') + colored(gpl_fix_spases(OS, 27,overflow=False), 'white') + colored('|','red') + colored('    █    █   █  █   █    █    ░███▒  ', 'magenta') + colored('|', 'red'))
    print(colored('|', 'red') + colored(' Owners: ', 'blue') + colored(gpl_fix_spases(owners_text,23,overflow=False),'white') + colored('|', 'red') + colored('    █    █   █  █   █    █       ▒█  ', 'magenta') + colored('|', 'red'))
    print(colored('| ', 'red') + colored(field2_title,'blue') + colored(gpl_fix_spases(field2_text,31 - len(field2_title),overflow=False),'white') + colored('|', 'red') + colored('    █    █▓ ▓█  █▓ ▓█    █░   █░ ▒█  ', 'magenta') + colored('|', 'red'))
    print(colored('| ', 'red') + colored(field3_title,'blue') + colored(gpl_fix_spases(field3_text,31 - len(field3_title),overflow=False),'white') + colored('|', 'red') + colored('    █     ███    ███     ▒██  ▒███▒  ', 'magenta') + colored('|', 'red'))
    print(colored('|________________________________|_____________________________________|', 'red'))
    print(colored('| Warning:', 'red') + colored(" Don't break or kill script while process runing.            ",'yellow') + colored('|', 'red'))
    print(colored('|______________________________________________________________________|\n', 'red'))



# Set Banner Version
#
# modules:
#
# internal modules:
#
# version:
# 1
def gpl_set_banner_verion(Version):
    global Banner_Version
    Banner_Version = Version