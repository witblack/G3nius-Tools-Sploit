"""     libs        """
from nmap import PortScanner

"""     local   """
Scanner = PortScanner()

"""     GPL     """
# scan port status
#
# external:
# from socket import gethostbyname_ex
#
# note:
# if return None, connection lose or unable to scan
#
# version
# 1
def gpl_port_scanner(IP, Port=None, UDP=False, more_nmap_argument=''):
    global Scanner
    try:
        if UDP:
            more_nmap_argument += ' -sU'
        if Port == None:
            Scan = Scanner.scan(IP, arguments=more_nmap_argument)
        else:
            Scan = Scanner.scan(IP, str(Port), arguments=more_nmap_argument)
        if UDP:
            Result = Scan['scan'][IP]['udp']
        else:
            Result = Scan['scan'][IP]['tcp']
        return Result
    except:
        return None