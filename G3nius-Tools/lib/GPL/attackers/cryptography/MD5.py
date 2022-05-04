# libs
from hashlib import md5
from lib.GPL.String_Workers import gpl_convert_to_bytes

# string to MD5
#
# external:
# from hashlib import md5
#
# internal
# gpl_convert_to_bytes
#
# version
# 1
def gpl_MD5(data):
    data = gpl_convert_to_bytes(data)
    return md5(data).hexdigest()