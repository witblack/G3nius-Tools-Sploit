# import G3nius-Tools

"""     libs       """
from lib.GPL.IO import gpl_input
from lib.core.Error_Handler import Handler
import lib.config.Error_Levels as Error_Levels
from lib.GPL.Page_Managers import gpl_clear_and_banner, gpl_set_banner_verion
from lib.GPL.attackers.protocols.Service_Version_Name_Scanner import gpl_find_service_version_name


gpl_set_banner_verion('2.0.1')

"""     get info       """
IP = gpl_input("Target IP: ", get_ip=True)
Port = gpl_input("Target port: ", get_port=True)

"""     attack      """
gpl_clear_and_banner()
Handler(Error_Levels.Info, "Scanning...")
Details = gpl_find_service_version_name(IP, Port)
gpl_clear_and_banner()
if Details == None:
    Handler(Error_Levels.Failed_Job, "Port is off.")
elif Details[0] != None:
    Handler(Error_Levels.Info, "Attack done. Port Product: '" + Details[0] + "' Version: " + Details[1])
else:
    Handler(Error_Levels.Info, "Attack done. Port server Version: " + Details[1])
Handler(Error_Levels.NoStyle, "\n")