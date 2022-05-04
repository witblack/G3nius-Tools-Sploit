"""     libs    """
# external
from os import execv
from sys import argv, executable
# internal
from lib.core.main.Clean_Temp_Dir import Clean_Temp_Dir


# restart
def Restart_G3nius():
    Clean_Temp_Dir()
    execv(argv[0], argv)