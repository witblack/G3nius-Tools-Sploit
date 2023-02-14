# libs
from rsa import newkeys, encrypt, decrypt
from lib.GPL.String_Workers import gpl_convert_to_bytes


# generate new RSA keys
#
# external:
# from rsa import newkeys
#
# version
# 1
def gpl_RSA_new_key(Key_Size):
    Keys = newkeys(Key_Size)
    return Keys


# encrypt with RSA public key
#
# external:
# from rsa import encrypt
#
# internal
# gpl_convert_to_bytes
#
# version
# 1
def gpl_RSA_encrypt(Data, Public_Key):
    if type(Data) != bytes:
        Data = gpl_convert_to_bytes(Data)
    Encrypted = encrypt(Data, Public_Key)
    return Encrypted


# decrypt with RSA private key
#
# external:
# from rsa import decrypt
#
# internala
# gpl_convert_to_bytes
#
# version
# 1
def gpl_RSA_decrypt(Data, Private_Key):
    if type(Data) != bytes:
        Data = gpl_convert_to_bytes(Data)
    Encrypted = decrypt(Data, Private_Key)
    return Encrypted