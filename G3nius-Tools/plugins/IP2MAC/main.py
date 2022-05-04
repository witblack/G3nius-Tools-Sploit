# import G3nius-Tools
#!/bin/python3
# coding: utf-8

"""     libs      """
from lib.GPL.attackers.network.IP_To_MAC import gpl_ip_to_mac
from lib.GPL.IO import gpl_input
from lib.GPL.Page_Managers import gpl_clear_and_banner, gpl_set_banner_verion
from lib.core.Error_Handler import Handler
import lib.config.Error_Levels as Error_Levels

"""     configs     """
Version = '2.0.1'


"""     proccess      """
# clear page
gpl_set_banner_verion(Version)
gpl_clear_and_banner()

# find mac
IP = gpl_input('Enter IP address: ', get_ip=True)
MAC = gpl_ip_to_mac(IP)
gpl_clear_and_banner()
if MAC:
    Handler(Error_Levels.Alert, 'Found:\t' + MAC)
else:
    Handler(Error_Levels.Failed_Job, 'MAC not found!', 'May be ARP (as broadcast) filtered by firewall.')