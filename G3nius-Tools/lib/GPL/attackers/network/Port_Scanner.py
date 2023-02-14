"""     libs        """
from nmap import PortScanner
from socket import socket

"""     GPL     """
# scan port status
#
# external:
# from nmap import PortScanner
#
# note:
# if return None, connection lose or unable to scan
#
# version
# 2
def gpl_port_scanner(IP, Port=None, UDP=False, Scan_Version=False, More_Nmap_Argument=''):
    Scanner = PortScanner()
    try:
        if Scan_Version:
            More_Nmap_Argument += ' -sV'
        if UDP:
            More_Nmap_Argument += ' -sU'
        if Port == None:
            Scan = Scanner.scan(IP, arguments=More_Nmap_Argument)
        else:
            Scan = Scanner.scan(IP, str(Port), arguments=More_Nmap_Argument)
        if UDP:
            Result = Scan['scan'][IP]['udp']
        else:
            Result = Scan['scan'][IP]['tcp']
        return Result
    except:
        return None



# is tcp open ?
#
# external:
# from socket import socket
#
# version
# 1
def gpl_is_TCP_open(IP, Port):
    Socket = socket()
    Result = Socket.connect_ex((IP, Port))
    if Result == 0:
        return True
    elif Result == 111:
        return False
    else:
        return None
