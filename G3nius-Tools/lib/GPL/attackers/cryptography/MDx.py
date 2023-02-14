# libs
from Crypto.Hash import MD2, MD4, MD5
from lib.GPL.String_Workers import gpl_convert_to_bytes

# convert to MD5
#
# external:
# from Crypto.Hash import MD5
#
# internal
# gpl_convert_to_bytes
#
# version
# 1
def gpl_MD5(data):
    if type(data) != bytes:
        data = gpl_convert_to_bytes(data)
    md5 = MD5.new()
    md5.update(data)
    return md5.hexdigest()


# convert to MD4
#
# external:
# from Crypto.Hash import MD4
#
# internal
# gpl_convert_to_bytes
#
# version
# 1
def gpl_MD4(data):
    if type(data) != bytes:
        data = gpl_convert_to_bytes(data)
    md4 = MD4.new()
    md4.update(data)
    return md4.hexdigest()


# convert to MD4
#
# external:
# from Crypto.Hash import MD4
#
# internal
# gpl_convert_to_bytes
#
# version
# 1
def gpl_MD2(data):
    if type(data) != bytes:
        data = gpl_convert_to_bytes(data)
    md2 = MD2.new()
    md2.update(data)
    return md2.hexdigest()