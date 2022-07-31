"""     libs        """
# external
from ipaddress import IPv4Address, IPv6Address

"""     GPL     """
# return list of IPs (V4)
#
# external:
# from ipaddress import IPv4Address
#
# version
# 1
def gpl_IPv4_range(start_IP: str, end_IP: str):
    # list of IPs
    IPs = []
    # Create range
    start_IP = IPv4Address(start_IP)
    end_IP = IPv4Address(end_IP)
    for IP_int in range(int(start_IP), int(end_IP)):
        IPs.append(str(IPv4Address(IP_int)))
    # return list of IPs
    return IPs



# return list of IPs (V4)
#
# external:
# from ipaddress import IPv6Address
#
# version
# 1
def gpl_IPv6_range(start_IP: str, end_IP: str):
    # list of IPs
    IPs = []
    # Create range
    start_IP = IPv6Address(start_IP)
    end_IP = IPv6Address(end_IP)
    for IP_int in range(int(start_IP), int(end_IP)):
        IPs.append(str(IPv6Address(IP_int)))
    # return list of IPs
    return IPs