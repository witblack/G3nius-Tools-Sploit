"""     libs    """
# internal
from lib.GPL.attackers.network.Port_Scanner import gpl_port_scanner


"""     GPL     """
# find http webserver version
#
# internal:
# gpl_port_scanner
#
# note:
# if return None, connection lose or unable to scan
#
# version
# 1
def gpl_get_server_service_version(IP, Port, more_nmap_argument=''):
    Version = gpl_port_scanner(IP, Port=Port, more_nmap_argument='-sV' + more_nmap_argument)
    if Version == None:
        return None
    # [Product_Name , Version]
    try:
        return [ Version[Port]['product'] , Version[Port]['version'] ]
    except:
        try:
            return [ None , Version[Port]['version'] ]
        except:
                return False