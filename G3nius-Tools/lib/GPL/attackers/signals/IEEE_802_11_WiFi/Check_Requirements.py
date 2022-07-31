"""     libs      """
from lib.GPL.Command_Managers import gpl_check_command_exists

"""     gpl     """
# check Wi-Fi attackers requirements
#
# internal modules:
# gpl_run_OS_command
#
# version:
# 1
def gpl_wifi_check_requirements(Commands = ['aircrack-ng', 'airodump-ng', 'aireplay-ng', 'ifconfig', 'iwconfig', 'iwlist']):
    for Command in Commands:
        if not gpl_check_command_exists(Command):
            return False
    return True