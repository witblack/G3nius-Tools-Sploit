# import G3nius-Tools
# coding: utf-8

"""     libs      """
from lib.GPL.IO import gpl_input, gpl_confirm
from lib.GPL.File_Workers import gpl_ask_load_from_file, gpl_read_from_file
from lib.core.G3nius_Location import G3nius_Location
from lib.GPL.HTTP_Managers import gpl_http_get
from lib.core.Error_Handler import Handler
import lib.config.Error_Levels as Error_Levels

"""    Configs   """
import plugins.PageAdmin_Finder.Config as Config

try:
    """     ask     """
    # URL
    Target_URL = gpl_input('Enter URL of your target: ', get_URL=True)
    # fix '/' character
    if Target_URL[-1] != '/':
        Target_URL += '/'
    # Custom wordlist
    Use_Default = gpl_confirm('Do you want use default wordlist ? ', default_return_value=True)
    if Use_Default:
        # use cumstom wordlist
        Records = gpl_ask_load_from_file(read_lines=True)
    else:
        # use default wordlist
        Location = G3nius_Location()
        Records = gpl_read_from_file(Location + Config.Default_Wrodlist, read_lines=True)
    # verbose
    Verbose = gpl_confirm('Run as verbose mode [y/n] ? ', default_return_value=True)


    """     process     """
    # attack
    for Record in Records:
        # request page
        URL = Target_URL + Record
        if Verbose:
            Handler(Error_Levels.Info, 'Testing "' + URL + '" ...')
        Response = gpl_http_get(URL)
        # user used CTRL+C
        if Response == None:
            break
        # processing on response
        if Response.status_code == 200:
            Handler(Error_Levels.Alert, 'Admin page found : ' + URL)
        elif Response.status_code == 404 and Verbose:
            Handler(Error_Levels.Failed_Job, 'Testing "' + URL + " was failed (404).")
        else:
            Handler(Error_Levels.Info, 'Unable to detect ' + str(Response.status_code) + ' detect page : ' + URL)
except (EOFError, KeyboardInterrupt):
    Handler(Error_Levels.Failed_Job, 'Exit with user request.')
