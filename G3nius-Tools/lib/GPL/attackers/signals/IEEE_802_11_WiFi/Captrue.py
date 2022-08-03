"""     libs       """
# internal
from lib.GPL.Command_Managers import gpl_run_OS_command, Without_Error
from lib.core.G3nius_Location import G3nius_Location
from lib.GPL.String_Workers import gpl_fix_string_to_uri
from lib.GPL.Timeout import gpl_timeout
# external
from glob import glob
from os.path import isdir
# config
from lib.config.GPL import AirCrack_More_Arguments_Capture, Default_WiFi_ScanTime
"""     gpl     """
# capture wifi signals in file
#
# internal modules:
# gpl_run_OS_command
#
# external:
# from os.path import isdir
#
# NOTE:
# (ESSID, BSSID, Channel) are filter options.
# You can use everyone together.
# You can't run it under thread
#
# version:
# 1
def gpl_wifi_capture_signals(Destination, ScanTime=Default_WiFi_ScanTime, Interface='wlan0', Channel=None, ESSID=None, BSSID=None):
    # save in directory if is
    if isdir(Destination) and Destination[-1] != '/':
        Destination += '/'
    # Filter options
    More_Args = ''
    if Channel:
        More_Args += ' -c ' + str(Channel)
    if BSSID:
        More_Args += ' --bssid ' + BSSID
    if ESSID:
        More_Args += ' --essid "' + gpl_fix_string_to_uri(ESSID) + '"'
    # capture
    with gpl_timeout(ScanTime):
        try:
            gpl_run_OS_command('airodump-ng ' + AirCrack_More_Arguments_Capture + More_Args + ' -w ' + gpl_fix_string_to_uri(Destination, fix_for_without_double_quotation=True) + ' ' + Interface + Without_Error)
        except TimeoutError:
            # stop airodump-ng
            gpl_run_OS_command('killall -9 airodump-ng')
            # Find newest files
            if isdir(Destination) and Destination[-1] != '/':
                Destination += '/'
            Cap_Files = glob(Destination + '*.cap')
            CSV_Files = glob(Destination + '*.csv')
            Kismet_CSV_Files = glob(Destination + '*.kismet.csv')
            Kismet_Netxml_Files = glob(Destination + '*.kismet.netxml')
            LogFiles = glob(Destination + '*.log.csv')
            Cap_Files.sort()
            CSV_Files.sort()
            Kismet_CSV_Files.sort()
            Kismet_Netxml_Files.sort()
            LogFiles.sort()
            # return
            return {
                'Cap_Address': Cap_Files[-1],
                'CSV_Address': CSV_Files[-1],
                'Kismet_CSV_Address': Kismet_CSV_Files[-1],
                'Kismet_Netxml_Address': Kismet_Netxml_Files[-1],
                'LogFile_Address': LogFiles[-1]
            }
        else:
            return False