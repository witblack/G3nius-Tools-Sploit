"""     libs       """
from lib.packages.termcolor import colored
from lib.GPL.String_Workers import gpl_fix_spases

"""     functions      """
def Generate_Menu(Plugin_List, Menu_Numebrs):
    ret = colored("|______________________________________________________________________|", 'red')
    ret += colored('\n|' + gpl_fix_spases('', 70) + '|\n|   ', 'red') + colored(gpl_fix_spases('Select Once:', 67), 'yellow') + colored('|', 'red')
    ret += colored("\n|______________________________________________________________________|", 'red')
    for Plugin in Plugin_List:
        ret += "\n" + gpl_fix_spases(colored(str(Plugin['ID']), 'green') + ' ' + colored(Plugin['Title'], 'white'), 87, False)
    ret += "\n" + colored(str(Menu_Numebrs + 1), 'green') + colored(', ', 'white') + colored('q', 'green') + colored(' Exit', 'white')
    return ret