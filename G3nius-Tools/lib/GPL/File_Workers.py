"""     libs    """
# internal
from os.path import exists, isfile, isdir
from lib.GPL.IO import gpl_clear, gpl_input, gpl_sleep
from lib.packages.termcolor import colored
import lib.config.Error_Levels as Error_Levels
from lib.core.Error_Handler import Handler
from lib.core.Exit_Request import Exit_Request
import lib.config.Exit_Codes as Exit_Codes
# external
from os import remove, mkdir

"""     GPL     """

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
        if not exists(address):
            print(colored(on_file_not_exists_text,on_file_not_exists_text_color))
            gpl_sleep(on_file_not_exists_sleep_by_sec)
        elif isfile(address):
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
        elif isdir(address):
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
        if not exists(address):
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
        elif isdir(address):
            print(colored(on_file_is_dir_text,on_file_is_dir_text_color))
            gpl_sleep(on_file_is_dir_sleep_by_sec)
        elif isfile(address):
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

# Read from file
#
# internal modules (core)
# Handler
# Exit_Request
#
# configs
# Error_Levels
# Exit_Codes
#
# version
# 1
def gpl_read_from_file(File_Name, read_bytes=False, encoding='UTF-8', show_error=True, on_access_failed_text="Can't read file.", on_access_failed_description_text=None, on_access_failed_return_value=None, on_access_failed_exit_code=None, on_CTRL_C_return_value=None, on_CTRL_C_exit_code=None):
    try:
        if read_bytes:
            file = open(File_Name, 'rb')
        else:
            file = open(File_Name, 'r', encoding=encoding)
        Content = file.read()
        file.close()
    except KeyboardInterrupt:
        if on_CTRL_C_exit_code:
            Exit_Request(Exit_Codes.CTRL_C)
        return on_CTRL_C_return_value
    except:
        if show_error:
            Handler(Error_Levels.High, on_access_failed_text, on_access_failed_description_text)
        if on_access_failed_exit_code:
            Exit_Request(on_access_failed_exit_code)
        return on_access_failed_return_value
    return Content


# write to file
#
# version
# 1
def gpl_write_to_file(File_Name: str, Data, Mode='w', on_access_error_text="Can't write to file!", on_accesss_error_text_description=None):
    try:
        File = open(File_Name, Mode)
        File.write(Data)
        File.close()
    except (KeyboardInterrupt, EOFError):
        return None
    except:
        if on_access_error_text:
            Handler(Error_Levels.High, on_access_error_text, on_accesss_error_text_description)
        return False
    else:
        return True


# remove file
#
# External:
# from os import remove
#
# version
# 1
def gpl_remove_file(FileName):
    try:
        remove(FileName)
    except:
        return False
    else:
        return True

# make directory
#
# External:
# from os import mkdir
#
# version
# 1
def gpl_mkdir(Address):
    try:
        mkdir(Address)
    except:
        return False
    else:
        return True