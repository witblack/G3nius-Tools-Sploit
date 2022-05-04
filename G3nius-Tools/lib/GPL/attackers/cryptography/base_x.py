# libs
from base64 import b16encode, b16decode, b32encode, b32decode, b64encode, b64decode, b85encode, b85decode
from lib.GPL.String_Workers import gpl_convert_to_bytes


# base16 encode
#
# external:
# from base64 import b16encode
#
# internal
# gpl_convert_to_bytes
#
# version
# 1
def gpl_base16_encode(data):
    data = gpl_convert_to_bytes(data)
    return str(b16encode(data))


# base16 decode
#
# external:
# from base64 import b16encode
#
# internal
# gpl_convert_to_bytes
#
# version
# 1
def gpl_base16_decode(data):
    data = gpl_convert_to_bytes(data)
    return b16decode(data)


# base32 encode
#
# external:
# from base64 import b32encode
#
# internal
# gpl_convert_to_bytes
#
# version
# 1
def gpl_base32_encode(data):
    data = gpl_convert_to_bytes(data)
    return str(b32encode(data))


# base32 decode
#
# external:
# from base64 import b32encode
#
# internal
# gpl_convert_to_bytes
#
# version
# 1
def gpl_base32_decode(data):
    data = gpl_convert_to_bytes(data)
    return b32decode(data)


# base64 encode
#
# external:
# from base64 import b64encode
#
# internal
# gpl_convert_to_bytes
#
# version
# 1
def gpl_base64_encode(data):
    data = gpl_convert_to_bytes(data)
    return str(b64encode(data))


# base64 decode
#
# external:
# from base64 import b64encode
#
# internal
# gpl_convert_to_bytes
#
# version
# 1
def gpl_base64_decode(data):
    data = gpl_convert_to_bytes(data)
    return b64decode(data)


# base85 encode
#
# external:
# from base64 import b85encode
#
# internal
# gpl_convert_to_bytes
#
# version
# 1
def gpl_base85_encode(data):
    data = gpl_convert_to_bytes(data)
    return str(b85encode(data))


# base85 decode
#
# external:
# from base64 import b85encode
#
# internal
# gpl_convert_to_bytes
#
# version
# 1
def gpl_base85_decode(data):
    data = gpl_convert_to_bytes(data)
    return b85decode(data)