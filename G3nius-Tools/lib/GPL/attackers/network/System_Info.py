"""     libs        """
# external
from socket import gethostname, socket

# internal
from lib.GPL.HTTP_Managers import gpl_http_get

"""     GPL     """
# get ip
#
# external:
# from socket import gethostname, socket
#
# internal:
# gpl_http_get
#
# note:
# if return False, internet lose
#
# version
# 1
def gpl_get_local_system_ip():
    session = socket()
    try:
        session.connect(("8.8.8.8", 1))
        IP = session.getsockname()[0]
    except:
        return False
    else:
        return IP



# get remote ip
#
# internal:
# gpl_http_get
#
# note:
# if return None: connection lose.
# version
# 1
def gpl_get_remote_system_ip():
    IP = gpl_http_get('https://api.bugzone.ir/myIP.php', ok_http_codes=[200])
    return IP


# get hostname
#
# external:
# from socket import gethostname
#
# version
# 1
def gpl_get_system_hostname():
    try:
        return gethostname()
    except:
        return False