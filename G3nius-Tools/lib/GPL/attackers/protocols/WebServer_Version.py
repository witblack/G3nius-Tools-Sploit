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
def gpl_get_http_webserver_version(IP, Port=80):
    HTTP_Version = gpl_port_scanner(IP, Port=Port ,more_nmap_argument='-sV')
    if HTTP_Version == None:
        return None
    # [Product_Name , Version]
    return [ HTTP_Version[80]['product'] , HTTP_Version[80]['version'] ]