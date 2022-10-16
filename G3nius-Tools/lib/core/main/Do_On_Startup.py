"""     libs       """
# internal
from lib.core.OS_Detector import OS
from lib.config.Main_Configs import Block_Windows_CMD
# extrenal
from os import getppid
from psutil import Process

"""     functions      """
def Startup():
    # Get process parent name & block CMD
    if Block_Windows_CMD and OS == 'Windows' and Process(getppid()).name() == 'cmd.exe':
        print("Cmd not allowed because Windows CMD can't show colored texts.")
        print("Please run it under Windows Powershell.")
        print('You can set this option to "False" (Off) at "lib/config/Main_Configs.py"')