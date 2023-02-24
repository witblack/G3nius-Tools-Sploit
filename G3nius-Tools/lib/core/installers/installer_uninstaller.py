"""     libs    """
# external
from os import symlink, unlink
from shutil import move, rmtree

# core
from lib.core.G3nius_Location import G3nius_Location
from lib.core.Error_Handler import Handler
from lib.core.installers.check import Check_Installtion_G3nius

# configs
import lib.config.Error_Levels as Error_Levels


"""     installers      """

# bootstrap
Location = G3nius_Location()

# version:
# 1
def Install_G3nius(Verbose=True):
    if not Check_Installtion_G3nius(False):
        if Verbose:
            Handler(Error_Levels.Alert, "Installing G3nius-Tools...")
        try:
            move(Location, '/usr/share/G3nius-Tools')
            symlink('/usr/share/G3nius-Tools/launcher.py', '/bin/g3nius-tools')
        except:
            if Verbose:
                Handler(Error_Levels.Failed_Job, "Can't write on G3nius folder or '/usr/share/' or '/bin/'.", "Manage your access and make sure run as root or administrator.")
            return False
        else:
            if Verbose:
                Handler(Error_Levels.Alert, "G3nius-Tools installed successfully.", "Command is 'g3nius-tools'")
                Handler(Error_Levels.Alert, "Current directory is moved to '/usr/share/G3nius-Tools/',\nUse 'cd ..' before.")
            return True
    else:
        if Verbose:
            Handler(Error_Levels.Alert, "G3nius-Tools already installed.")
        return None


# version:
# 1
def Uninstall_G3nius(Verbose=True):
    if Check_Installtion_G3nius(False):
        if Verbose:
            Handler(Error_Levels.Alert, "Uninstalling G3nius-Tools...")
        try:
            rmtree('/usr/share/G3nius-Tools')
            unlink('/bin/g3nius-tools')
        except:
            if Verbose:
                Handler(Error_Levels.Failed_Job, "Can't delete from '/usr/share/' or '/bin/'.", "Manage your access and make sure run as root or administrator.")
            return False
        else:
            if Verbose:
                Handler(Error_Levels.Alert, "G3nius-Tools uninstalled successfully.")
            return True
    else:
        if Verbose:
            Handler(Error_Levels.Alert, "G3nius-Tools already not installed.")
        return False
