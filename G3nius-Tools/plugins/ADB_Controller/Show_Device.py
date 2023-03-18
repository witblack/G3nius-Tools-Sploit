"""     libs      """
from lib.classes.gpl import gpl_adb_device_information
from lib.classes.gpl import Handler, Error_Levels

"""     process     """
def Show_Device(Device):
    Info = gpl_adb_device_information(Device)
    # Title
    Handler(Error_Levels.Plus, f"Serials: {Info['Serial']}", Print_Before="\n\n")
    # Description
    Handler(Error_Levels.Star, f"Model:\t{Info['Model']}", Print_Before="\t")
    Handler(Error_Levels.Star, f"Name:\t{Info['Name']}", Print_Before="\t")
    Handler(Error_Levels.Star, f"Widow Size:\t{Info['Widow_Size']}", Print_Before="\t")
    Handler(Error_Levels.Star, f"Rotation:\t{Info['Rotation']}", Print_Before="\t")
    Handler(Error_Levels.Star, f"IP:\t\t{Info['IP']}", Print_Before="\t")
    Handler(Error_Levels.Star, f"Path:\t{Info['Path']}", Print_Before="\t")
