"""     libs        """
from lib.GPL.Command_Managers import gpl_run_OS_command, NoOutPut, return_ERROR_if_error
import lib.config.Error_Levels as Error_Levels
from lib.core.Error_Handler import Handler

"""     def         """

# IEEE 802.11 Wifi - monning on
#
# internal modules:
# gpl_run_OS_command
#
# NOTE:
# don't change interface name
#
# version:
# 1
def gpl_wifi_monning_on():
    OutPut = []
    Commands = [
        # stop services using Wireless
        'service wpa_supplicant stop' + NoOutPut,
        'service network-manager stop' + NoOutPut,
        'service NetworkManager stop' + NoOutPut,
        'service avahi-daemon stop' + NoOutPut,
        # change mode & name
        'ifconfig wlan0 down' + NoOutPut + return_ERROR_if_error,
        'ip link set wlan0 name wlan0mon' + NoOutPut,
        'iwconfig wlan0mon mode monitor' + NoOutPut + return_ERROR_if_error,
        'ifconfig wlan0mon up' + NoOutPut + return_ERROR_if_error
    ]
    for Command in Commands:
        while True:
            try:
                OutPut.append(gpl_run_OS_command(Command))
            except (EOFError, KeyboardInterrupt):
                Handler(Error_Levels.Failed_Job, "Can't use keyboard interrupts when Script working on hardware", "It's dangerous and maybe damage to your hardware, So blocked.")
                pass
            else:
                break
    if 'ERROR' in NoOutPut[-3:]:
        return False
    return True


# IEEE 802.11 Wifi - monning off
#
# internal modules:
# gpl_run_OS_command
#
# NOTE:
# don't change interface name
#
# version:
# 1
def gpl_wifi_monning_off():
    OutPut = []
    Commands = [
        # Change name & mode
        'ifconfig wlan0mon down' + NoOutPut + return_ERROR_if_error,
        'iwconfig wlan0mon mode managed' + NoOutPut + return_ERROR_if_error,
        'ip link set wlan0mon name wlan0' + NoOutPut,
        'ifconfig wlan0 up' + NoOutPut + return_ERROR_if_error,
        # start services using Wireless
        'service wpa_supplicant start' + NoOutPut,
        'service network-manager start' + NoOutPut,
        'service NetworkManager start' + NoOutPut,
        'service avahi-daemon start' + NoOutPut,
        'nmcli networking off' + NoOutPut,
        'nmcli networking on' + NoOutPut,
        'service NetworkManager restart' + NoOutPut
    ]
    for Command in Commands:
        while True:
            try:
                OutPut.append(gpl_run_OS_command(Command))
            except (EOFError, KeyboardInterrupt):
                Handler(Error_Levels.Failed_Job, "Can't use keyboard interrupts when Script working on hardware", "It's dangerous and maybe damage to your hardware, So blocked.")
                pass
            else:
                break
    if 'ERROR' in NoOutPut[:3]:
        return False
    return True
