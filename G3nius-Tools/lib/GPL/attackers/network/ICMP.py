"""     libs     """
# external
from scapy.all import IP, ICMP, sr, conf

# internal
import lib.config.GPL as GPL_Config

# disabe verbose
conf.verb = 0

# send and recv icmp
#
# external:
# from scapy.all import IP, ICMP, sr
#
# note:
# if return None: connection lose
#
# version
# 1
def gpl_icmp(ip, timeout=GPL_Config.ICMP_Timeout, TTL=GPL_Config.Default_TTL, payload=None):
    try:
        if payload != None:
            Answer, Unanswer = sr(IP(dst=ip, ttl=TTL) / ICMP() / payload, timeout=timeout)
        else:
            Answer, Unanswer = sr(IP(dst=ip, ttl=TTL) / ICMP(), timeout=timeout)
        return [Answer, Unanswer]
    except:
        return None