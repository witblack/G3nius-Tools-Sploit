# libs
from socket import gethostbyname_ex

# convert hostname to IP
#
# external:
# from socket import gethostbyname_ex
#
# version
# 1
def gpl_hostname_to_ip(Hostname):
    return gethostbyname_ex(Hostname)[2]