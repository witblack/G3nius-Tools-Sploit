"""     libs    """
# Internal
from lib.GPL.String_Workers import gpl_convert_to_bytes
# External
from binascii import hexlify, unhexlify

"""     gpl     """
# convert to HEX
#
# internal
# gpl_convert_to_bytes
#
# Note:
# 1. Input data can be string or bytes
# 2. Result not started with 0x
#
# version
# 1
def gpl_HEXlify(data):
    data = gpl_convert_to_bytes(data)
    return hexlify(data)


# convert from HEX
#
# internal
# gpl_convert_to_bytes
#
# Note:
# 1. Input should not started with 0x
#
# version
# 1
def gpl_unHEXlify(data):
    data = gpl_convert_to_bytes(data)
    return unhexlify(data)
