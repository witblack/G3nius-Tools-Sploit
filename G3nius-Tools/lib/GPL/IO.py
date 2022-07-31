"""     libs    """
from re import match
from time import sleep
from ipaddress import ip_address
from lib.packages.termcolor import colored
from lib.GPL.Page_Managers import gpl_clear
import lib.config.Exit_Codes as Exit_Codes
from lib.GPL.Page_Managers import gpl_clear_and_banner, gpl_clear
from lib.core.Exit_Request import Exit_Request
from lib.core.Error_Handler import Handler
import lib.config.Error_Levels as Error_Levels

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
#
# version:
# 1
def gpl_input(text: str, dont_style=False, forground_color='white', clear_and_banner_before=True, on_invalid_after_clear_text=None, clear_before=False, on_exit_request_text='\nExit with user request.', on_exit_request_forground_color='yellow', q_to_exit=True, clear_and_banner_when_exit=True, clear_when_exit=False, get_int=False, get_float=False, get_ip=False, get_MAC=False, on_invalid_number_text='Invalid number!', on_invalid_sleep_by_sec=1, on_invalid_clear_and_banner=True, on_invalid_ip_text="Invalid IP!", on_invalid_mac_text="Invalid MAC!"):
    if clear_and_banner_before and (not clear_before):
        gpl_clear_and_banner()
    elif clear_before:
        gpl_clear()
    try:
        while True:
            if dont_style:
                choose = input(text)
            else:
                choose = input(colored(text, forground_color))
            if q_to_exit and (str.lower(choose) == 'q' or str.lower(choose) == 'exit'):
                if clear_when_exit:
                    gpl_clear()
                elif clear_and_banner_when_exit:
                    gpl_clear_and_banner()
                print(colored(on_exit_request_text, on_exit_request_forground_color))
                Exit_Request(Exit_Codes.Normal)
            else:
                if get_float:
                    try:
                        choose = float(choose)
                    except:
                        Handler(Error_Levels.High, on_invalid_number_text)
                        gpl_sleep(on_invalid_sleep_by_sec)
                        if on_invalid_clear_and_banner:
                            gpl_clear_and_banner()
                        if on_invalid_after_clear_text:
                            print(on_invalid_after_clear_text)
                    else:
                        return choose
                elif get_int:
                    try:
                        choose = int(choose)
                    except:
                        Handler(Error_Levels.High, on_invalid_number_text)
                        gpl_sleep(on_invalid_sleep_by_sec)
                        if on_invalid_clear_and_banner:
                            gpl_clear_and_banner()
                        if on_invalid_after_clear_text:
                            print(on_invalid_after_clear_text)
                    else:
                        return choose
                elif get_ip:
                    try:
                        ip_address(choose)
                    except:
                        Handler(Error_Levels.High, on_invalid_ip_text)
                        gpl_sleep(on_invalid_sleep_by_sec)
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
                        Handler(Error_Levels.High, on_invalid_mac_text)
                        gpl_sleep(on_invalid_sleep_by_sec)
                        if on_invalid_clear_and_banner:
                            gpl_clear_and_banner()
                        if on_invalid_after_clear_text:
                            print(on_invalid_after_clear_text)
                else:
                    return choose
    except (KeyboardInterrupt, EOFError):
        print(colored("\n" + on_exit_request_text, on_exit_request_forground_color))
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
def gpl_while_input(title: str, list_of_chooses=[], text_color='magenta', number_color='green', title_color='white', input_text='Number of choose : ', input_color='blue', on_invalid_sleep_time=1, on_invalid_text='Invalid number!', on_exit_request_text='Exit with user request.', on_exit_request_forground_text_color='yellow', exit_option=True, exit_option_text='Exit (or "q").'):
    if exit_option:
        list_of_chooses.append(exit_option_text)
    while True:
        gpl_clear_and_banner()
        print(colored(title, title_color))
        i = 0
        for option in list_of_chooses:
            i += 1
            print("\t" + colored(str(i), number_color) + ' ' + colored(option, text_color))
        choose = gpl_input("\n" + input_text, input_color, clear_and_banner_before=False)
        try:
            choose = int(choose)
        except:
            Handler(Error_Levels.High, on_invalid_text)
            gpl_sleep(on_invalid_sleep_time)
            continue
        else:
            if choose <= 0 or choose > len(list_of_chooses):
                Handler(Error_Levels.High, on_invalid_text)
                gpl_sleep(on_invalid_sleep_time)
                continue
        if exit_option and choose == len(list_of_chooses):
            print(colored(on_exit_request_text, on_exit_request_forground_text_color))
            Exit_Request(Exit_Codes.Normal)
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
# 1
def gpl_sleep(time_by_sec=1, on_exit_request_text='Exit with user request.', on_exit_request_forground_color='yellow', manage_ctrl_C_and_exit=True):
    try:
        sleep(time_by_sec)
    except (KeyboardInterrupt, EOFError):
        if manage_ctrl_C_and_exit:
            print(colored(on_exit_request_text, on_exit_request_forground_color))
            exit(Exit_Codes.CTRL_C)
        else:
            raise KeyboardInterrupt


# confirm
#
# modules:
# gpl_sleep
#
# version:
# 1
def gpl_confirm(text: str, default_return_value=None, clear_and_banner_before=True):
    Choose = str.lower(gpl_input(colored('[?] ', 'green') + text + ' [y/n/q] ? ', dont_style=True, clear_and_banner_before=clear_and_banner_before))
    if Choose == 'n' or Choose == 'no':
        return False
    elif Choose == 'y' or Choose == 'yes':
        return True
    else:
        if default_return_value != None:
            return default_return_value
        else:
            print(colored('[!] ', 'red') + colored('Invalid Choose! type once y/yes/n/no/q/exit', 'yellow'))
            gpl_sleep(1)