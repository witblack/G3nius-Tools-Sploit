# g3nius-tools power lib


# import libs
from termcolor import colored
import requests
from time import sleep
from sys import exit
import os
import sys






# input data safely
#
# modules:
# from sys import exit
# from termcolor import colored
#
# internal modules:
# gpl_sleep
#
# version:
# 1
def gpl_input(text='',forground_color='white',on_exit_request_text='Exit with user request.',on_exit_request_forground_color='yellow',on_exit_request_error_code=0,q_to_exit=True,get_int=False,get_float=False,on_invalid_number_text='Invalid number!',on_invalid_number_text_color='red',on_invalid_number_sleep_by_sec=1):
    while True:
        try:
            choose = input(colored(text,forground_color))
        except:
            print(colored(on_exit_request_text,on_exit_request_forground_color))
            exit(on_exit_request_error_code)
        else:
            if q_to_exit and (str.lower(choose) == 'q' or str.lower(choose) == 'exit'):
                print(colored(on_exit_request_text,on_exit_request_forground_color))
                exit(on_exit_request_error_code)
            else:
                if get_float:
                    try:
                        float(choose)
                    except:
                        print(colored(on_invalid_number_text,on_invalid_number_text_color))
                        gpl_sleep(on_invalid_number_sleep_by_sec)
                    else:
                        return float(choose)
                elif get_int:
                    try:
                        int(choose)
                    except:
                        print(colored(on_invalid_number_text,on_invalid_number_text_color))
                        gpl_sleep(on_invalid_number_sleep_by_sec)
                    else:
                        return int(choose)
                else:
                    return choose


# while get
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
def gpl_while_input(title='',list_of_chooses=[],text_color='magenta',number_color='green',title_color='white',input_text='Number of choose : ',input_color='blue',on_invalid_sleep_time=1,on_invalid_text='Invalid number!',on_invalid_forground_color='red',on_exit_request_error_code=0,on_exit_request_text='Exit with user request.',on_exit_request_forground_text_color='yellow',exit_option=True,exit_option_text='Exit (or "q").'):
    if exit_option:
        list_of_chooses.append(exit_option_text)
    while True:
        gpl_clear()
        print(colored(title,title_color))
        i = 0
        for option in list_of_chooses:
            i += 1
            print('\t\t' + colored(str(i),number_color) + ' ' + colored(option,text_color))
        choose = gpl_input(input_text,input_color)
        try:
            choose = int(choose)
        except:
            print(colored(on_invalid_text,on_invalid_forground_color))
            gpl_sleep(on_invalid_sleep_time)
            continue
        else:
            if choose <= 0 or choose > len(list_of_chooses):
                print(colored(on_invalid_text,on_invalid_forground_color))
                gpl_sleep(on_invalid_sleep_time)
                continue
        if exit_option and choose == len(list_of_chooses):
            print(colored(on_exit_request_text,on_exit_request_forground_text_color))
            exit(on_exit_request_error_code)
        else:
            return choose


# clear page
#
# modules:
# import os
# from termcolor import colored
#
# version:
# 1
def gpl_clear(clear_on_unsuported_OS=True,on_unsuported_OS_text="New page is here:\n-----------------",on_unsuported_OS_text_color='yellow'):
    if os.name == 'posix':
        print('\033c')
    elif os.name == 'nt':
        print(os.popen('cls').read())
    elif clear_on_unsuported_OS:
        print('\033c')
    else:
        print(colored(on_unsuported_OS_text,on_unsuported_OS_text_color))


# get request
#
# modules:
# import requests
# from termcolor import colored
#
# version:
# 1
def gpl_get(url,timeout_by_s=45,timeout_failed_times=None,on_timeout_failed_times_text='Failed to connect. Check your internet connection.',on_timeout_failed_times_text_color='red',on_timeout_failed_times_command='sys.exit(1)',ignores=[200],on_failed_to_connect_text='Failed to connect. Retry...',on_failed_to_connect_text_color='red',on_error_code_retry_text='Get error code: {ErrorCode} , retry to connect.',on_error_code_retry_text_color='yellow',verbos=True):
    failed_times = 0
    while True:
        try:
            data = requests.get(url,timeout=timeout_by_s)
        except:
            if verbos:
                print(colored(on_failed_to_connect_text,on_failed_to_connect_text_color))
            failed_times += 1
            if timeout_failed_times and failed_times >= timeout_failed_times:
                if verbos:
                    print(colored(on_timeout_failed_times_text,on_timeout_failed_times_text_color))
                exec(on_timeout_failed_times_command)
        else:
            if data.status_code in ignores:
                return data
            elif verbos:
                print(colored(on_error_code_retry_text.format(ErrorCode=data.status_code),on_error_code_retry_text_color))


# get request
#
# modules:
# import requests
# from termcolor import colored
#
# version:
# 1
def gpl_post(url,post_data={},timeout_by_s=45,timeout_failed_times=None,on_timeout_failed_times_text='Failed to connect. Check your internet connection.',on_timeout_failed_times_text_color='red',on_timeout_failed_times_command='sys.exit(1)',ignores=[200],on_failed_to_connect_text='Failed to connect. Retry...',on_failed_to_connect_text_color='red',on_error_code_retry_text='Get error code: {ErrorCode} , retry to connect.',on_error_code_retry_text_color='yellow',verbos=True):
    failed_times = 0
    while True:
        try:
            data = requests.post(url,data=post_data,timeout=timeout_by_s)
        except:
            if verbos:
                print(colored(on_failed_to_connect_text,on_failed_to_connect_text_color))
            failed_times += 1
            if timeout_failed_times and failed_times >= timeout_failed_times:
                if verbos:
                    print(colored(on_timeout_failed_times_text,on_timeout_failed_times_text_color))
                exec(on_timeout_failed_times_command)
        else:
            if data.status_code in ignores:
                return data
            elif verbos:
                print(colored(on_error_code_retry_text.format(ErrorCode=data.status_code),on_error_code_retry_text_color))


# ask load from file
#
# modules:
# import os
# from termcolor import colored
#
# internal modules:
# gpl_clear
# gpl_input
# gpl_sleep
#
# version:
# 1
def gpl_ask_load_from_file(just_ask=False,read_lines=False,read_content=False,read_bytes=False,ask_address_text='Enter address/name of file to load (q to exit): ',ask_address_text_color='white',on_file_not_exists_text='File not exists or not a file!',on_file_not_exists_text_color='red',on_file_not_exists_sleep_by_sec=1,on_file_not_have_enough_access_text='File not have enough access to read.',on_file_not_have_enough_access_text_color='red',on_file_not_have_enough_access_sleep_by_sec=1,on_file_is_dir_text="It's a directory. should be a file.",on_file_is_dir_text_color='red',on_file_is_dir_sleep_by_sec=1):
    while True:
        gpl_clear()
        address = gpl_input(ask_address_text,ask_address_text_color)
        if not os.path.exists(address):
            print(colored(on_file_not_exists_text,on_file_not_exists_text_color))
            gpl_sleep(on_file_not_exists_sleep_by_sec)
        elif os.path.isfile(address):
            if just_ask:
                return address
            elif read_content:
                try:
                    file = open(address,'r')
                    data = file.read()
                except:
                    print(colored(on_file_not_have_enough_access_text,on_file_not_have_enough_access_text_color))
                    gpl_sleep(on_file_not_have_enough_access_sleep_by_sec)
                else:
                    file.close()
                    return data
            elif read_lines:
                try:
                    file = open(address,'r')
                    data = file.readlines()
                except:
                    print(colored(on_file_not_have_enough_access_text,on_file_not_have_enough_access_text_color))
                    gpl_sleep(on_file_not_exists_sleep_by_sec)
                else:
                    file.close()
                    lst = []
                    for item in data:
                        if item[-1:] == "\n":
                            lst.append(item[:-1])
                        else:
                            lst.append(item)
                    return lst
            elif read_bytes:
                try:
                    file = open(address,'rb')
                    data = file.read()
                except:
                    print(colored(on_file_not_have_enough_access_text,on_file_not_have_enough_access_text_color))
                    gpl_sleep(on_file_not_exists_sleep_by_sec)
                else:
                    file.close()
                    return data
        elif os.path.isdir(address):
            print(colored(on_file_is_dir_text,on_file_is_dir_text_color))
            gpl_sleep(on_file_is_dir_sleep_by_sec)


# ask save to file
#
# modules:
# import os
#
# internal modules:
# gpl_input
# gpl_clear
# gpl_sleep
#
# version:
# 1
def gpl_ask_save_to_file(just_ask=False,bytes_to_write=b'',string_to_write='',is_string_to_write=True,ask_address_text='Enter address/name of file to load (q to exit): ',ask_address_text_color='white',on_ask_overwrite_text='This is a file, Overwrite [y/n/q] ? ',on_ask_overwrite_text_color='yellow',on_file_not_have_enough_access_text='File not have enough access to write.',on_file_not_have_enough_access_text_color='red',on_file_not_have_enough_access_sleep_by_sec=1,on_file_is_dir_text='This is a directory. Should be file.',on_file_is_dir_text_color='red',on_file_is_dir_sleep_by_sec=1):
    while True:
        gpl_clear()
        address = gpl_input(ask_address_text,ask_address_text_color)
        if not os.path.exists(address):
            if just_ask:
                return address
            elif is_string_to_write:
                try:
                    file = open(address,'w')
                    file.write(string_to_write)
                except:
                    print(colored(on_file_not_have_enough_access_text,on_file_not_have_enough_access_text_color))
                    gpl_sleep(on_file_not_have_enough_access_sleep_by_sec)
                else:
                    file.close()
                    return
            else:
                try:
                    file = open(address,'wb')
                    file.write(bytes_to_write)
                except:
                    print(colored(on_file_not_have_enough_access_text,on_file_not_have_enough_access_text_color))
                    gpl_sleep(on_file_not_have_enough_access_sleep_by_sec)
                else:
                    file.close()
                    return
        elif os.path.isdir(address):
            print(colored(on_file_is_dir_text,on_file_is_dir_text_color))
            gpl_sleep(on_file_is_dir_sleep_by_sec)
        elif os.path.isfile(address):
            gpl_clear()
            choose = gpl_input(on_ask_overwrite_text,on_ask_overwrite_text_color)
            if choose.lower() == 'y' or choose.lower() == 'yes':
                if just_ask:
                    return address
                elif is_string_to_write:
                    try:
                        file = open(address, 'w')
                        file.write(string_to_write)
                    except:
                        print(colored(on_file_not_have_enough_access_text,on_file_not_have_enough_access_text_color))
                        gpl_sleep(on_file_not_have_enough_access_sleep_by_sec)
                    else:
                        file.close()
                        return
                else:
                    try:
                        file = open(address, 'wb')
                        file.write(bytes_to_write)
                    except:
                        print(colored(on_file_not_have_enough_access_text, on_file_not_have_enough_access_text_color))
                        gpl_sleep(on_file_not_have_enough_access_sleep_by_sec)
                    else:
                        file.close()
                        return

# sleep
#
# modules:
# from time import sleep
# from sys import exit
#
# version:
# 1
def gpl_sleep(time_by_sec=1,on_exit_request_text='Exit with user request.',on_exit_request_forground_color='yellow',on_exit_request_exit_code=0):
    try:
        sleep(time_by_sec)
    except:
        print(colored(on_exit_request_text,on_exit_request_forground_color))
        exit(on_exit_request_exit_code)


# fix_spases
#
# modules:
#
# version:
# 1
def gpl_fix_spases(string,lenth,overflow=True,fill_with=' '): # lenth start from 1
    if len(string) < lenth:
        num = lenth - len(string)
        return (string + (fill_with * num))
    elif len(string) > lenth:
        if overflow:
            return string
        else:
            return string[:lenth]
    else:
        return string


# banner
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
def gpl_clear_and_banner(owners_text='WitBlack',field2_title='',field2_text='',field3_title='',field3_text='',license='FREE'): # plugin_version shuild in globals
    if not 'plugin_version' in globals():
        raise Exception('plugin_version not found in globals')
    gpl_clear()
    python_verson = str(sys.version_info[0])
    if os.name == 'posix':
        OS = 'Linux'
    elif os.name == 'nt':
        OS = 'Windows'
    else:
        OS = 'Unknown'
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
    print(colored('|', 'red') + colored(' Python Version: ', 'blue') + colored(python_verson + '              ', 'white') + colored('|','red') + colored('    █     ███    ███     █    ▒███▒  ', 'magenta') + colored('|', 'red'))
    print(colored('|', 'red') + colored(' LICENSE: ', 'blue') + colored(gpl_fix_spases(license, 22,overflow=False), 'white') + colored('|','red') + colored('    █    █▓ ▓█  █▓ ▓█    █    █▒ ░█  ', 'magenta') + colored('|', 'red'))
    print(colored('|', 'red') + colored(' PLUGIN VERSION: ', 'blue') + colored(gpl_fix_spases(plugin_version, 15,overflow=False), 'white') + colored('|','red') + colored('    █    █   █  █   █    █    █▒░    ', 'magenta') + colored('|', 'red'))
    print(colored('|', 'red') + colored(' OS: ', 'blue') + colored(gpl_fix_spases(OS, 27,overflow=False), 'white') + colored('|','red') + colored('    █    █   █  █   █    █    ░███▒  ', 'magenta') + colored('|', 'red'))
    print(colored('|', 'red') + colored(' Plugin Owners: ', 'blue') + colored(gpl_fix_spases(owners_text,16,overflow=False),'white') + colored('|', 'red') + colored('    █    █   █  █   █    █       ▒█  ', 'magenta') + colored('|', 'red'))
    print(colored('| ', 'red') + colored(field2_title,'blue') + colored(gpl_fix_spases(field2_text,31 - len(field2_title),overflow=False),'white') + colored('|', 'red') + colored('    █    █▓ ▓█  █▓ ▓█    █░   █░ ▒█  ', 'magenta') + colored('|', 'red'))
    print(colored('| ', 'red') + colored(field3_title,'blue') + colored(gpl_fix_spases(field3_text,31 - len(field3_title),overflow=False),'white') + colored('|', 'red') + colored('    █     ███    ███     ▒██  ▒███▒  ', 'magenta') + colored('|', 'red'))
    print(colored('|________________________________|_____________________________________|', 'red'))
    print(colored('| Warning:', 'red') + colored(" Don't break or kill script while process runing.            ",'yellow') + colored('|', 'red'))
    print(colored('|______________________________________________________________________|\n', 'red'))


# url encode
#
# version
# 1
def gpl_url_encode(string):
    return string.replace('#','%23').replace('&','%26').replace('/','%2f').replace("\\",'%5C').replace(':',)