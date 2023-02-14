"""     libs    """
# internal
from lib.GPL.IO import gpl_input, gpl_sleep, gpl_confirm
import lib.config.Error_Levels as Error_Levels
from lib.core.Error_Handler import Handler
from lib.core.Exit_Request import Exit_Request
from lib.GPL.Page_Managers import gpl_clear_and_banner

# external
from os import remove, mkdir
from os.path import exists, isfile, isdir
from shutil import rmtree

# Configs
import lib.config.Exit_Codes as Exit_Codes

"""     GPL     """

# ask load from file
#
# internal modules:
# gpl_clear_and_banner
# gpl_input
# gpl_sleep
#
# version:
# 2
def gpl_ask_load_from_file(ask_address_text='Enter address/name of file to load (q to exit): ', just_ask=False, read_lines=False, read_content=False, read_bytes=False):
    while True:
        # Get URI from user
        gpl_clear_and_banner()
        FileName = gpl_input(ask_address_text)
        if not exists(FileName):
            # file not exists
            Handler(Error_Levels.Failed_Job, 'File not exists or not a file!')
            gpl_sleep()
        elif isfile(FileName):
            if just_ask:
                return FileName
            elif read_content:
                return gpl_read_from_file(FileName)
            elif read_lines:
                return gpl_read_from_file(FileName, read_lines=True)
            elif read_bytes:
                return gpl_read_from_file(FileName, read_bytes=True)
        else:
            # Selected URI is directory
            Handler(Error_Levels.Failed_Job, "It's a directory. should be a file.")
            gpl_sleep()



# ask save to file
#
# internal modules:
# gpl_input
# gpl_clear
# gpl_sleep
#
# version:
# 2
def gpl_ask_save_to_file(ask_address_text='Enter address/name of file to save (q to exit): ', just_ask=False, data=''):
    while True:
        gpl_clear_and_banner()
        FileName = gpl_input(ask_address_text)
        if not exists(FileName):
            if just_ask:
                return FileName
            else:
                gpl_write_to_file(FileName, data)
        elif isdir(FileName):
            # FileName is a directory
            Handler(Error_Levels.Failed_Job, 'This is a directory. Should be file.')
            gpl_sleep()
        elif isfile(FileName):
            # FileName already exists
            gpl_clear_and_banner()
            choose = gpl_confirm('This is a file, Overwrite [y/n/q] ? ', default_return_value=False)
            if choose:
                if just_ask:
                    return FileName
                else:
                    gpl_write_to_file(FileName, data)




# Read from file
#
# internal modules (core)
# Handler
# Exit_Request
#
# configs
# Error_Levels
#
# version
# 2
def gpl_read_from_file(FileName, read_bytes=False, read_lines=False, remove_newlines=True, encoding='UTF-8', on_access_failed_text=None, on_access_failed_description_text=None, show_error=True):
    try:
        if read_bytes:
            File = open(FileName, 'rb')
        else:
            File = open(FileName, 'r', encoding=encoding)
        if read_lines:
            Lines = File.readlines()
            if remove_newlines:
                # remove \n end of lines
                for i in range(0, len(Lines)):
                    if Lines[i][-1] == "\n":
                        Lines[i] = Lines[i][:-1]
            Content = Lines
            del Lines, i
        else:
            Content = File.read()
        File.close()
        return Content
    except (KeyboardInterrupt, EOFError):
        if show_error:
            Handler(Error_Levels.Failed_Job, 'Cant read file. Check file permissions.')
        Exit_Request(Exit_Codes.CTRL_C, 'Exit with user request.')
    except:
        if on_access_failed_text != None:
            Handler(Error_Levels.Failed_Job, on_access_failed_text, on_access_failed_description_text)
        return False



# write to file
#
# version
# 2
def gpl_write_to_file(FileName: str, data, on_access_error_text='File not have enough access to write.', on_accesss_error_text_description=None):
    if type(data) == str:
        # Write string
        try:
            File = open(FileName, 'w')
            File.write(data)
        except:
            Handler(Error_Levels.Failed_Job, on_access_error_text, on_accesss_error_text_description)
            gpl_sleep()
        else:
            File.close()
            return True
    elif type(data) == bytes:
        # Write bytes
        try:
            File = open(FileName, 'wb')
            File.write(data)
        except:
            Handler(Error_Levels.Failed_Job, on_access_error_text, on_accesss_error_text_description)
            gpl_sleep()
        else:
            File.close()
            return True
    else:
        raise Exception('Argument called "data" must be string or bytes!')



# remove file
#
# External:
# from os import remove
#
# version
# 2
def gpl_remove_file(FileName):
    try:
        remove(FileName)
    except:
        return False
    else:
        return True



# create directory
#
# External:
# from os import mkdir
#
# version
# 2
def gpl_make_directory(Address):
    try:
        mkdir(Address)
    except:
        return False
    else:
        return True



# remove directory
#
# External:
# from shutil import rmtree
#
# Note:
# Directory and all of data will be removed
#
# version
# 2
def gpl_remove_directory(DirName):
    try:
        rmtree(DirName)
    except:
        return False
    else:
        return True