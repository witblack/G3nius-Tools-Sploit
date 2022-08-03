"""     libs      """
# internal
from lib.GPL.Command_Managers import gpl_run_OS_command, Without_Error
from lib.GPL.File_Workers import gpl_read_from_file, gpl_remove_file
from lib.GPL.String_Workers import gpl_fix_string_to_uri
from lib.core.G3nius_Location import G3nius_Location
from lib.GPL.Timeout import gpl_timeout
# external
from glob import glob
# config
from lib.config.GPL import AirCrack_More_Arguments_Scan, Default_WiFi_ScanTime

"""     gpl     """

# get APs & clients
#
# internal modules:
# gpl_run_OS_command
# gpl_remove_file
# gpl_fix_string_to_uri
# G3nius_Location
# gpl_timeout
#
# internal:
# from glob import glob
#
# Structure:
#   {
#   "BSSID1": {
#        'BSSID': 'AA:BB:CC:DD:EE:FF',
#        'First_Time_Seen': '2022-07-28 01:40:52',
#        'Last_Time_Seen': '2022-07-28 01:40:52',
#        'Channel': 13,
#        'Speed': 130,
#        'Privacy': 'WPA2',
#        'Cipher': 'CCMP TKIP',
#        'Authentication': 'PSK',
#        'Power': -33,
#        'Beacons': 3,
#        'IV': 0,
#        'LAN_IP': '0.0.0.0',
#        'ID_length': 12,
#        'ESSID': 'AP_ESSID',
#        'Key': None | 'Key',
#        "Clients": [
#               {
#                   'MAC': 'AA:BB:CC:DD:EE:FF',
#                   'First_Time_Seen': '2022-07-28 01:40:52',
#                   'Last_Time_Seen': '2022-07-28 01:40:52',
#                   'Power': -33,
#                   'Packets': 12,
#                   'Probed_ESSIDs': ['ESSID1', 'ESSID2', ...],
#                   'Connected_BSSID': None | 'AA:BB:CC:DD:EE:FF'
#               }
#        , ...]
#       },
#   ...
#   "Not_Associated": [
#       {
#           'MAC': 'AA:BB:CC:DD:EE:FF',
#           'First_Time_Seen': '2022-07-28 01:40:52',
#           'Last_Time_Seen': '2022-07-28 01:40:52',
#           'Power': -33,
#           'Packets': 12,
#           'Probed_ESSIDs': ['ESSID1', 'ESSID2', ...],
#           'Connected_BSSID': None | 'AA:BB:CC:DD:EE:FF'
#       }
#   ]
#
# version:
# 1
def gpl_wifi_scan_signals(Interface='wlan0', ScanTime=Default_WiFi_ScanTime):
    Temp_output_file = G3nius_Location() + '/tmp/AP_Scan'
    Result = {
        'Not_Associated': []
    }
    with gpl_timeout(ScanTime):
        try:
            # run airodump
            gpl_run_OS_command('airodump-ng ' + AirCrack_More_Arguments_Scan + ' --output-format csv -w ' + gpl_fix_string_to_uri(Temp_output_file, fix_for_without_double_quotation=True) + ' ' + Interface + Without_Error)
        except TimeoutError:
            # stop airodump-ng
            gpl_run_OS_command('killall -9 airodump-ng')
            # choose newest
            Temp_output_file = glob(Temp_output_file + '*')
            Temp_output_file.sort()
            # read out file
            OutPut = gpl_read_from_file(Temp_output_file[-1])
            # delete outfile
            for OutFile in Temp_output_file:
                gpl_remove_file(OutFile)
            # process on output
            IsClients = False
            # process line by line
            for AP in OutPut.split("\n"):
                # skip first line
                if AP[:5] == 'BSSID':
                    continue
                # delete empty lines
                elif len(AP) == 0:
                    continue
                # get columns
                AP = AP.split(', ')
                # check goes in client section
                if AP[0] == 'Station MAC':
                    IsClients = True
                    continue
                elif IsClients:
                    # is client
                    Probed_ESSIDs = AP[5:][0].split(' ,')
                    # fix probed list
                    if len(Probed_ESSIDs) == 1:
                        Probed_ESSIDs[0] = Probed_ESSIDs[0][:-1]
                    if '(not associated)' in Probed_ESSIDs:
                        Probed_ESSIDs.remove('(not associated)')
                    if len(Probed_ESSIDs[0]) == 17:
                        # is MAC (Connected)
                        Connected_BSSID = Probed_ESSIDs[0]
                        Probed_ESSIDs = Probed_ESSIDs[1:]
                    else:
                        # probed
                        Connected_BSSID = None
                    # set up
                    Client = {
                        'MAC': AP[0],
                        'First_Time_Seen': AP[1],
                        'Last_Time_Seen': AP[2],
                        'Power': int(AP[3]),
                        'Packets': int(AP[4]),
                        'Probed_ESSIDs': Probed_ESSIDs,
                        'Connected_BSSID': Connected_BSSID
                    }
                    # append to result
                    if Connected_BSSID:
                        Result[Connected_BSSID]['Clients'].append(Client)
                    else:
                        Result['Not_Associated'].append(Client)
                else:
                    # is AP
                    # strip (except ESSID)
                    for i in range(0,len(AP)):
                        AP[i] = AP[i].strip()
                    # get key
                    if len(AP[14]) > 1:
                        Key = AP[14]
                    else:
                        Key = None
                    # fix lan ip
                    AP[11] = AP[11].replace(' ', '')
                    # append to result
                    Result[AP[0]] = {
                        'BSSID': AP[0],
                        'First_Time_Seen': AP[1],
                        'Last_Time_Seen': AP[2],
                        'Channel': int(AP[3]),
                        'Speed': int(AP[4]),
                        'Privacy': AP[5],
                        'Cipher': AP[6],
                        'Authentication': AP[7],
                        'Power': int(AP[8]),
                        'Beacons': int(AP[9]),
                        'IV': int(AP[10]),
                        'LAN_IP': AP[11],
                        'ID_length': AP[12],
                        'ESSID': AP[13],
                        'Key': Key,
                        'Clients': []
                    }
            # return
            return Result
    return False