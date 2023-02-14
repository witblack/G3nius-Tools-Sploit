"""     libs        """
# external
from Crypto.Cipher import AES
# internal
from lib.GPL.String_Workers import gpl_convert_to_bytes



"""

Simple usage:



from lib.GPL.attackers.cryptography.AES import *

key = '1' * 8  # should be 16, 32, 64 , ...
data = 'h' * 16  # should be 16, 32, 64 , ...

cipher, nonce = gpl_AES_new_cipher(key, EAX=True)
enc, digest = gpl_AES_encrypt(data, cipher, calculate_digest=True)
print('encrypted: ', enc)
cipher, nnoce = gpl_AES_new_cipher(key, nonce, EAX=True)
print('decrypted: ', gpl_AES_decrypt(enc, cipher))
print(gpl_AES_verify(digest, cipher))



"""



"""     GPL     """

# AES Encrypt
#
# external:
# from Crypto.Cipher import AES
#
# version
# 1
def gpl_AES_new_cipher(key, nonce=None, CBC=False, GCM=False, CCM=False, CFB=False, EAX=False, CTR=False, ECB=False, OCB=False, OFB=False, OpenPGP=False, SIV=False):    # block multiple mode
    Trues = [CBC, GCM, CCM, CFB, EAX, CTR, ECB, OCB, OFB, OpenPGP, SIV].count(True)
    if Trues != 1:
        raise Exception("AES Error! One mode should be True.")
    # detect mode
    if CBC:
        Mode = AES.MODE_CBC
    elif GCM:
        Mode = AES.MODE_GCM
    elif CCM:
        Mode = AES.MODE_CCM
    elif CFB:
        Mode = AES.MODE_CFB
    elif EAX:
        Mode = AES.MODE_EAX
    elif CTR:
        Mode = AES.MODE_CTR
    elif ECB:
        Mode = AES.MODE_ECB
    elif OCB:
        Mode = AES.MODE_OCB
    elif OFB:
        Mode = AES.MODE_OFB
    elif OpenPGP:
        Mode = AES.MODE_OPENPGP
    else:
        Mode = AES.MODE_SIV
    # check key be Bytes
    if type(key) != bytes:
        key = gpl_convert_to_bytes(key)
    # generate key
    if nonce:
        Cipher = AES.new(key, Mode, nonce=nonce)
    else:
        Cipher = AES.new(key, Mode)
    Nonce = Cipher.nonce
    return [Cipher, Nonce]



# AES Encrypt
#
# external:
# from Crypto.Cipher import AES
#
# version
# 1
def gpl_AES_encrypt(data, cipher, calculate_digest=False):
    # data most be byte
    data = gpl_convert_to_bytes(data)
    # encrypt
    if calculate_digest:
        return cipher.encrypt_and_digest(data)
    else:
        return cipher.encrypt(data)



# AES Decrypt
#
# external:
# from Crypto.Cipher import AES
#
# version
# 1
def gpl_AES_decrypt(data, cipher):
    return cipher.decrypt(data)



# AES verify en/de+cryptions
#
# external:
# from Crypto.Cipher import AES
#
# version
# 1
def gpl_AES_verify(tag, cipher):
    try:
        cipher.verify(tag)
    except:
        return False
    else:
        return True
