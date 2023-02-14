"""     libs        """
from nmap import PortScanner

"""     GPL     """
# detect OS and version
#
# external:
# from nmap import PortScanner
#
# note:
# If return None, connection lose or unable to scan
# REMEMBER: it make scan all ports on target
#
# version
# 1
def gpl_OS_detector(IP):
    Scanner = PortScanner()
    try:
        Result = Scanner.scan(IP, arguments='-O')
        return Result['scan'][IP]['osmatch'][0]
    except:
        return None