# NOTE:
# It's also a facade design pattern.

"""     libs        """
# core
from lib.core.Error_Handler import Handler
from lib.core.G3nius_Location import G3nius_Location
from lib.core.End_Plugin import End_Plugin
from lib.core.Check_Supported_OS import Check_Supported
from lib.core.Exit_Request import Exit_Request
from lib.core.OS_Detector import OS
from lib.core.Run_File import Run_File
# main
from lib.core.main.Restart_G3nius import Restart_G3nius
from lib.core.main.Plugin_Launcher import Plugin_Launcher
from lib.core.main.Statistics import Send_Statistics
from lib.core.main.Generate_Menu import Generate_Menu
from lib.core.main.Do_On_Startup import Startup
from lib.core.main.Clean_Temp_Dir import Clean_Temp_Dir
# installers
from lib.core.installers.check import Check_Installtion_G3nius
from lib.core.installers.installer_uninstaller import Install_G3nius, Uninstall_G3nius

"""     FACADE    """
import lib.config.Error_Levels as Error_Levels


"""     class       """
class core:
    # Core
    def OS():
        return OS

    def End_Plugin():
        return End_Plugin()

    def G3nius_Location():
        return G3nius_Location()

    def Handler(*args, **keywords):
        return Handler(*args, **keywords)

    def Run_File(*args, **keywords):
        return Run_File(*args, **keywords)

    def Exit_Request(*args, **keywords):
        return Exit_Request(*args, **keywords)

    def Check_Supported(*args, **keywords):
        return Check_Supported(*args, **keywords)

    # main
    class main:
        def Startup():
            return Startup()

        def Restart_G3nius():
            return Restart_G3nius()

        def Generate_Menu(*args, **keywords):
            return Generate_Menu(*args, **keywords)

        def Clean_Temp_Dir(*args, **keywords):
            return Clean_Temp_Dir(*args, **keywords)

        def Plugin_Launcher(*args, **keywords):
            return Plugin_Launcher(*args, **keywords)

        def Send_Statistics(*args, **keywords):
            return Send_Statistics(*args, **keywords)

    # installers
    class installers:
        def Check_Installtion_G3nius(*args, **keywords):
            return Check_Installtion_G3nius(*args, **keywords)

        def Install_G3nius(*args, **keywords):
            return Install_G3nius(*args, ** keywords)

        def Uninstall_G3nius(*args, **keywords):
            return Uninstall_G3nius(*args, **keywords)
