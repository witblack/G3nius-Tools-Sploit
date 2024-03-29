# import G3nius-Tools
# coding: utf-8


"""     libs       """
# external
from os import listdir
# internal
# GPL
from lib.GPL.IO import gpl_input, gpl_while_input, gpl_sleep
from lib.GPL.File_Workers import gpl_write_to_file, gpl_read_from_file
from lib.GPL.Page_Managers import gpl_set_banner_verion, gpl_clear_and_banner
# Core
from lib.core.Check_Supported_OS import Check_Supported
from lib.core.End_Plugin import End_Plugin
from lib.core.Error_Handler import Handler
# config
import lib.config.Error_Levels as Error_Levels


# EOF and Keyboard Interupt
try:
    # check OS
    if not Check_Supported(Linux=True):
        Handler(Error_Levels.High, "This plugin is only for Linux users.")
        End_Plugin()

    """     config      """
    Plugin_Version = '2.0.0'
    Status_Codes = {1: "0", 2: "1", 3: "255"}


    """     setup      """
    gpl_set_banner_verion(Plugin_Version)
    gpl_clear_and_banner()

    """     get LEDs"""
    LEDs = listdir('/sys/class/leds/')
    LEDs.sort()

    while True:
        # ask from user
        Choose = gpl_while_input("Select once LED on your system:", LEDs)
        Value = gpl_while_input("OFF or ON ? ", ['OFF', 'ON', 'Automatic (Maybe not work)', 'Show Status'])
        Address = '/sys/class/leds/' + LEDs[Choose - 1] + '/brightness'
        if Value == 4:
            # show status
            Status = gpl_read_from_file(Address, on_access_failed_text="Failed to read LED status.")
            if Status != None:
                if Status == "255\n":
                    Handler(Error_Levels.Alert, 'Is automatic.')
                elif Status == "1\n":
                    Handler(Error_Levels.Alert, 'Is on.')
                elif Status == "0\n":
                    Handler(Error_Levels.Alert, 'Is off.')
                else:
                    Handler(Error_Levels.Failed_Job, "Can't detect. Status Code: " + Status.replace("\n", ''))
            gpl_sleep()
        else:
            # set status
            Status = Status_Codes[Value]
            gpl_write_to_file(Address, Status + "\n", on_access_error_text="Failed to set status!")
            if Status != None:
                Handler(Error_Levels.Alert, 'LED status changed.')
            gpl_sleep()
except (EOFError, KeyboardInterrupt):
    Handler(Error_Levels.Failed_Job, "Exit with user request.")