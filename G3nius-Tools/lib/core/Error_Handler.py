# import libs
import lib.config.Error_Levels as Error_Levels
import lib.config.Exit_Codes as Exit_Codes
from lib.packages.termcolor import colored
from lib.core.Exit_Request import Exit_Request

"""     error handler       """
def Handler(Error_Level, Title, Description=None, Clear_Page=True, Print_Before=None, Without_Newline=False):
    End = "\n"
    if Print_Before:
        print(Print_Before, end='')
    if Without_Newline:
        End = ''
    if Error_Level == Error_Levels.Critical:
        print(colored('[!] ', 'red') + colored(Title, 'yellow'), end=End)
        if Clear_Page:
            Exit_Request(Exit_Codes.Crash)
        else:
            Exit_Request(Exit_Codes.Crash, clear_and_banner=False)
    elif Error_Level == Error_Levels.High:
        print(colored('[!] ', 'red') + colored(Title, 'yellow'), end=End)
    elif Error_Level == Error_Levels.Confirm:
        print(colored('[?] ', 'yellow') + colored(Title, 'white'), end=End)
    elif Error_Level == Error_Levels.Failed_Job:
        print(colored('[-] ', 'yellow') + colored(Title, 'red'), end=End)
    elif Error_Level == Error_Levels.Alert:
        print(colored('[+] ', 'green') + colored(Title, 'white'), end=End)
    elif Error_Level == Error_Levels.Info:
        print(colored('[*] ', 'magenta') + colored(Title, 'white'), end=End)
    else:
        print(Title, end=End)

    # show description
    if Description != None:
        if Error_Level == None:
            print(Description)
        else:
            print(colored("Description:\t", 'blue') + colored(Description, 'white'))
