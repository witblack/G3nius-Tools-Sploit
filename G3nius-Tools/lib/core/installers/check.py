"""     libs    """
# external
from os.path import isfile, isdir
from lib.core.Error_Handler import Handler
import lib.config.Error_Levels as Error_Levels



"""     check      """
# version:
# 1
def Check_Installtion_G3nius(Verbose=True):
    if (isdir('/usr/share/G3nius-Tools') and isfile('/bin/g3nius-tools')):
        if (Verbose):
            Handler(Error_Levels.Alert, "G3nius-Tools already Installed.")
        return True
    else:
        if (Verbose):
            Handler(Error_Levels.Failed_Job, "G3nius-Tools not installed.")
        return False