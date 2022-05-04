# libs
from scapy.all import srp, ARP, Ether

import lib.config.GPL as GPL_Config


# convert ip to mac
#
# external:
# from scapy.all import srp, ARP, Ether
#
# note:
# 1. don't manage CTRL+C CTRL+D
# 2. if return False = network connection lose
#
# version
# 1
def gpl_ip_to_mac(IP, timeout_by_sec=GPL_Config.ARP_Timeout):
    try:
        ANS, unANS = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=IP), timeout=timeout_by_sec, verbose=0)
        for s, r in ANS:
            MAC = r[Ether].src
    except (KeyboardInterrupt, EOFError):
        raise Exception(KeyboardInterrupt)
    except:
        return False
    else:
        if 'MAC' in locals() and len(MAC) == 17:
            return MAC
        else:
            return False