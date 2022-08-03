"""     libs       """
from lib.config.GPL import Check_WiFi_Channel_Changed_In_Change, Change_Channel_Try_Times
from lib.GPL.Command_Managers import gpl_run_OS_command
from lib.GPL.IO import gpl_sleep

"""     gpl     """
# set new channel
#
# internal modules:
# gpl_run_OS_command
#
# version:
# 1
def gpl_wifi_set_channel(Channel, Interface="wlan0"):
    Result = gpl_run_OS_command('iwconfig ' + Interface + ' channel ' + str(Channel))
    for i in range(0, Change_Channel_Try_Times):
        Current = gpl_wifi_channel(Interface)
        if Current == Channel:
            if len(Result) > 0:
                return False
            else:
                return True
        elif Current == None:
            return False
        gpl_sleep(Check_WiFi_Channel_Changed_In_Change)
    return False


# get channel
#
# internal modules:
# gpl_run_OS_command
#
# version:
# 1
def gpl_wifi_channel(Interface="wlan0"):
    Result = gpl_run_OS_command('iwlist ' + Interface + ' channel')
    Result = Result.split("\n")[-2]
    Result = Result.split(' ')[-1][:-1]
    try:
        return int(Result)
    except:
        return False