# external
from os.path import isdir, isfile
from os import remove, mkdir
from shutil import rmtree

# internal
from lib.core.G3nius_Location import G3nius_Location
from lib.config.Error_Levels import Critical, High

# clean
def Clean_Temp_Dir(Exit_If_Error=True):
    Location = G3nius_Location()
    try:
        if isdir(Location + '/tmp'):
            rmtree(Location + '/tmp')
        elif isfile(Location + '/tmp'):
            remove(Location + '/tmp')
        mkdir(Location + '/tmp')
    except:
        # import here to block loop
        from lib.core.Error_Handler import Handler
        if Exit_If_Error:
            Handler(Critical, "'tmp' folder can't be delete or create! Manage access.")
        else:
            Handler(High, "'tmp' folder can't be delete or create! Manage access.")