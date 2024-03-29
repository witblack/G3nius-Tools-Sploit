"""     libs    """
# External
from re import match
from time import sleep
from ipaddress import ip_address
from lib.packages.termcolor import colored

# Internal
from lib.GPL.HTTP_Managers import gpl_http_get
from lib.GPL.Page_Managers import gpl_clear_and_banner, gpl_clear
from lib.core.Error_Handler import Handler
from lib.core.Exit_Request import Exit_Request

# Configs
import lib.config.Exit_Codes as Exit_Codes
import lib.config.Error_Levels as Error_Levels
from lib.config.Main_Configs import Default_Sleep_Time

"""     GPL     """

# input data safely
#
# modules:
# from sys import exit
# from termcolor import colored
# from ipaddress import ip_address
#
# internal modules:
# gpl_sleep
# gpl_clear
# gpl_clear_and_banner
# gpl_get
#
# version:
# 2
def gpl_input(text: str, dont_style=False, clear_and_banner_before=True, on_invalid_after_clear_text=None, clear_before=False, q_to_exit=True, clear_and_banner_when_exit=True, clear_when_exit=False, get_int=False, get_URL=False, get_float=False, get_port=False, get_ip=False, get_MAC=False, get_plus_number=False, on_invalid_clear_and_banner=True):
    if clear_and_banner_before and (not clear_before):
        gpl_clear_and_banner()
    elif clear_before:
        gpl_clear()
    try:
        while True:
            if dont_style:
                choose = input(text)
            else:
                choose = input(colored(text, 'white'))
            if q_to_exit and (str.lower(choose) == 'q' or str.lower(choose) == 'exit'):
                if clear_when_exit:
                    gpl_clear()
                elif clear_and_banner_when_exit:
                    gpl_clear_and_banner()
                Exit_Request(Exit_Codes.Normal, text_after_clear=colored('Exit with user request.', 'yellow'))
            else:
                if get_float:
                    try:
                        choose = float(choose)
                    except:
                        Handler(Error_Levels.High, 'Invalid number!')
                        gpl_sleep()
                        if on_invalid_clear_and_banner:
                            gpl_clear_and_banner()
                        if on_invalid_after_clear_text:
                            print(on_invalid_after_clear_text)
                    else:
                        return choose
                elif get_int or get_port or get_plus_number:
                    try:
                        choose = int(choose)
                    except:
                        Handler(Error_Levels.High, 'Invalid number!')
                        gpl_sleep()
                        if on_invalid_clear_and_banner:
                            gpl_clear_and_banner()
                        if on_invalid_after_clear_text:
                            print(on_invalid_after_clear_text)
                    else:
                        if get_port:
                            if choose > 0 and choose <= 65535:
                                return choose
                            else:
                                Handler(Error_Levels.High, 'Invalid port number, can be range of 1-65535')
                        elif get_plus_number:
                            if choose > 0:
                                return choose
                            else:
                                Handler(Error_Levels.High, "Number can't be <= 0, Enter a plus number.")
                        else:
                            return choose
                elif get_ip:
                    try:
                        ip_address(choose)
                    except:
                        Handler(Error_Levels.High, "Invalid IP address!")
                        gpl_sleep()
                        if on_invalid_clear_and_banner:
                            gpl_clear_and_banner()
                        if on_invalid_after_clear_text:
                            print(on_invalid_after_clear_text)
                    else:
                        return choose
                elif get_MAC:
                    if match("^(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})$", choose):
                        return choose
                    else:
                        Handler(Error_Levels.High, "Invalid MAC address!")
                        gpl_sleep()
                        if on_invalid_clear_and_banner:
                            gpl_clear_and_banner()
                        if on_invalid_after_clear_text:
                            print(on_invalid_after_clear_text)
                elif get_URL:
                    if gpl_http_get(choose) != None:
                        return choose
                    else:
                        Handler(Error_Levels.Failed_Job, 'Invalid URL or problem to connection !')
                else:
                    return choose
    except (KeyboardInterrupt, EOFError):
        Exit_Request(Exit_Codes.CTRL_C, text_after_clear=colored('Exit with user request.', 'yellow'))



# while input
#
# modules:
# from sys import exit
# from termcolor import colored
#
# internal modules:
# gpl_clear
# gpl_input
# gpl_sleep
#
# notes:
#
# return value start from 1
# gpl_clear will be run before
#
# version:
# 2
def gpl_while_input(title: str, list_of_chooses: list, exit_option=True):
    if exit_option:
        list_of_chooses.append('Exit (or "q").')
    while True:
        gpl_clear_and_banner()
        print(colored(title, 'white'))
        i = 0
        for option in list_of_chooses:
            i += 1
            print("\t" + colored(str(i), 'green') + ' ' + colored(option, 'magenta'))
        choose = gpl_input("\nNumber of choose : ", clear_and_banner_before=False)
        try:
            choose = int(choose)
        except:
            Handler(Error_Levels.High, 'Invalid number!')
            gpl_sleep(1)
            continue
        else:
            if choose <= 0 or choose > len(list_of_chooses):
                Handler(Error_Levels.High, 'Invalid number!')
                gpl_sleep(1)
                continue
        if exit_option and choose == len(list_of_chooses):
            Exit_Request(Exit_Codes.Normal, text_after_clear='Exit with user request.')
        else:
            list_of_chooses.pop()
            return choose



# sleep
#
# modules:
# from time import sleep
# from sys import exit
#
# version:
# 2
def gpl_sleep(time_by_sec=Default_Sleep_Time):
    try:
        sleep(time_by_sec)
    except (KeyboardInterrupt, EOFError):
        Exit_Request(Exit_Codes.Normal, text_after_clear='Exit with user request.')


# confirm
#
# modules:
# gpl_sleep
#
# version:
# 1
def gpl_confirm(text: str, default_return_value=None, clear_and_banner_before=True):
    while True:
        Choose = str.lower(gpl_input(colored('[?] ', 'green') + text + ' [y/n/q] ? ', dont_style=True, clear_and_banner_before=clear_and_banner_before))
        if Choose == 'n' or Choose == 'no':
            return False
        elif Choose == 'y' or Choose == 'yes':
            return True
        else:
            if default_return_value != None and len(Choose) == 0:
                return default_return_value
            else:
                print(colored('[!] ', 'red') + colored('Invalid Choose! type once y/yes/n/no/q/exit', 'yellow'))
                gpl_sleep(1)
