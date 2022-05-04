"""     libs        """
# internal
from lib.GPL.attackers.network.ICMP import gpl_icmp
import lib.config.GPL as GPL_Config

"""     gpl     """
# check ip exists
#
# internal:
# gpl_icmp
#
# note:
# if return None: connection lose
#
# version
# 1
def gpl_ipv4_icmp_exists_check(ip, timeout=GPL_Config.ICMP_Timeout, TTL=GPL_Config.Default_TTL):
    Response = gpl_icmp(ip, timeout, TTL)
    if Response == None:
        return None
    if len(Response[0].res) > 0:
        # online
        return True
    elif len(Response[1].res) > 0:
        # offline
        return False
    else:
        # unknown
        return None