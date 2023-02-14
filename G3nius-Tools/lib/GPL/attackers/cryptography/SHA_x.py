# libs
from Crypto.Hash import SHA1, SHA224, SHA256, SHA384, SHA512
from lib.GPL.String_Workers import gpl_convert_to_bytes


# convert to SHA1
#
# external:
# from Crypto.Hash import SHA1
#
# internal
# gpl_convert_to_bytes
#
# version
# 1
def gpl_SHA1(data):
    if type(data) != bytes:
        data = gpl_convert_to_bytes(data)
    sha1 = SHA1.new(data)
    sha1.update(data)
    return sha1.hexdigest()



# convert to SHA224
#
# external:
# from Crypto.Hash import SHA224
#
# internal
# gpl_convert_to_bytes
#
# version
# 1
def gpl_SHA224(data):
    if type(data) != bytes:
        data = gpl_convert_to_bytes(data)
    sha224 = SHA224.new(data)
    sha224.update(data)
    return sha224.hexdigest()



# convert to SHA256
#
# external:
# from Crypto.Hash import SHA256
#
# internal
# gpl_convert_to_bytes
#
# version
# 1
def gpl_SHA256(data):
    if type(data) != bytes:
        data = gpl_convert_to_bytes(data)
    sha256 = SHA256.new(data)
    sha256.update(data)
    return sha256.hexdigest()



# convert to SHA384
#
# external:
# from Crypto.Hash import SHA384
#
# internal
# gpl_convert_to_bytes
#
# version
# 1
def gpl_SHA384(data):
    if type(data) != bytes:
        data = gpl_convert_to_bytes(data)
    sha384 = SHA384.new(data)
    sha384.update(data)
    return sha384.hexdigest()



# convert to SHA512
#
# external:
# from Crypto.Hash import SHA512
#
# internal
# gpl_convert_to_bytes
#
# version
# 1
def gpl_SHA512(data):
    if type(data) != bytes:
        data = gpl_convert_to_bytes(data)
    sha512 = SHA512.new(data)
    sha512.update(data)
    return sha512.hexdigest()