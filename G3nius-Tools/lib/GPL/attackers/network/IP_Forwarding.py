"""     libs        """
# external
from os import popen

# internal
from lib.GPL.File_Workers import gpl_read_from_file, gpl_write_to_file
from lib.GPL.Access_Managers import gpl_check_is_root

"""     GPL     """
# set ip forwarding
#
# external:
# from os import popen
#
# internal:
# gpl_check_is_root
#
# version
# 1
def gpl_set_ipv4_forward_state(Active=False):
    if gpl_check_is_root():
        if Active:
            popen('sysctl -w net.ipv4.ip_forward=1')
            if gpl_get_ipv4_forward_state():
                return True
        else:
            popen('sysctl -w net.ipv4.ip_forward=0')
            if not gpl_get_ipv4_forward_state():
                return True
    else:
        return None


# get status of ip forward
#
# internal:
# gpl_read_from_file
#
# note:
# if return None, root access error or can't read file
#
# version
# 1
def gpl_get_ipv4_forward_state():
    if gpl_check_is_root():
        State = gpl_read_from_file('/proc/sys/net/ipv4/ip_forward', show_error=False)
        if State[0] == '1':
            return True
        elif State[0] == '0':
            return False
        else:
            return None
    else:
        return None