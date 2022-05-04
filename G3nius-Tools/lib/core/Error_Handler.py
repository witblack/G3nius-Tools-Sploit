# import libs
import lib.config.Error_Levels as Error_Levels
import lib.config.Exit_Codes as Exit_Codes
from lib.packages.termcolor import colored
from lib.core.Exit_Request import Exit_Request

"""     error handler       """
def Handler(Error_Level, Title, Description=None, Clear_Page=True):
    if Error_Level == Error_Levels.Critical:
        print(colored('[!] ', 'red') + colored(Title, 'yellow'))
        if Clear_Page:
            Exit_Request(Exit_Codes.Crash)
        else:
            Exit_Request(Exit_Codes.Crash, clear_and_banner=False)
    elif Error_Level == Error_Levels.High:
        print(colored('[!] ', 'red') + colored(Title, 'yellow'))
    elif Error_Level == Error_Levels.Confirm:
        print(colored('[?] ', 'yellow') + colored(Title, 'white'))
    elif Error_Level == Error_Levels.Failed_Job:
        print(colored('[-] ', 'yellow') + colored(Title, 'red'))
    elif Error_Level == Error_Levels.Alert:
        print(colored('[+] ', 'green') + colored(Title, 'white'))
    elif Error_Level == Error_Levels.Info:
        print(colored('[*] ', 'magenta') + colored(Title, 'white'))
    else:
        print(Title)

    # show description
    if Description != None:
        if Error_Level == None:
            print(Description)
        else:
            print(colored("Description:\t", 'blue') + colored(Description, 'white'))