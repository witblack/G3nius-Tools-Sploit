#!/usr/bin/python3
# coding: utf-8

"""     libs      """
# External
import hashlib

# GPL
from lib.GPL.IO import gpl_while_input, gpl_confirm, gpl_input
from lib.GPL.Page_Managers import gpl_clear_and_banner, gpl_set_banner_verion
from lib.GPL.File_Workers import gpl_ask_load_from_file
from lib.GPL.attackers.cryptography.XOR import gpl_xor

# Core
from lib.core.Error_Handler import Handler

# configs
import lib.config.Error_Levels as Error_Levels


# Set plugin version
gpl_set_banner_verion('2.0.1')

# Show menu
Options = ['MD5', 'SHA-1', 'SHA-224', 'SHA3-224', 'SHA-256', 'SHA3-256', 'SHA-384', 'SHA3-384', 'SHA-512', 'SHA3-512', 'XOR (Without Brute Force)']
Choose = gpl_while_input('Select a algorithm to decode: ', Options)


# Verbose ?
Verbose = gpl_confirm('Run as Verbose', True)
if Verbose.lower() == 'y' or Verbose.lower() == 'yes':
    Verbose = True
else:
    Verbose = False

# if be type of hash
if Choose <= 10:
    Hash = gpl_input('Enter hash to find: ')
    Password_List = gpl_ask_load_from_file(ask_address_text='Enter address/name of Password list : ', read_lines=True)
    gpl_clear_and_banner()
    Handler(Error_Levels.Info, 'Attack started')
    Found = False
    # Brute Force
    if Choose == 1:
        # MD5
        for Password in Password_List:
            if hashlib.md5(bytes(Password.encode())).hexdigest() == hash:
                Handler(Error_Levels.Alert, "MD5 hash found !", "Value: " + Password)
                Found = True
                break
            elif Verbose:
                Handler(Error_Levels.Failed_Job, 'Testing "' + Password + '" ...')
    elif Choose == 2:
        # SHA-1
        for Password in Password_List:
            if hashlib.sha1(bytes(Password.encode())).hexdigest() == hash:
                Handler(Error_Levels.Alert, "SHA1 hash found !", "Value: " + Password)
                Found = True
                break
            elif Verbose:
                Handler(Error_Levels.Failed_Job, 'Testing "' + Password + '" ...')
    elif Choose == 3:
        # SHA-224
        for Password in Password_List:
            if hashlib.sha224(bytes(Password.encode())).hexdigest() == hash:
                Handler(Error_Levels.Alert, "SHA224 hash found !", "Value: " + Password)
                Found = True
                break
            elif Verbose:
                Handler(Error_Levels.Failed_Job, 'Testing "' + Password + '" ...')
    elif Choose == 4:
        # SHA3-224
        for Password in Password_List:
            if hashlib.sha3_224(bytes(Password.encode())).hexdigest() == hash:
                Handler(Error_Levels.Alert, "SHA3-224 hash found !", "Value: " + Password)
                Found = True
                break
            elif Verbose:
                Handler(Error_Levels.Failed_Job, 'Testing "' + Password + '" ...')
    elif Choose == 5:
        # SHA-256
        for Password in Password_List:
            if hashlib.sha256(bytes(Password.encode())).hexdigest() == hash:
                Handler(Error_Levels.Alert, "SHA256 hash found !", "Value: " + Password)
                Found = True
                break
            elif Verbose:
                Handler(Error_Levels.Failed_Job, 'Testing "' + Password + '" ...')
    elif Choose == 6:
        # SHA3-256
        for Password in Password_List:
            if hashlib.sha3_256(bytes(Password.encode())).hexdigest() == hash:
                Handler(Error_Levels.Alert, "SHA3_256 hash found !", "Value: " + Password)
                Found = True
                break
            elif Verbose:
                Handler(Error_Levels.Failed_Job, 'Testing "' + Password + '" ...')
    elif Choose == 7:
        # SHA-384
        for Password in Password_List:
            if hashlib.sha384(bytes(Password.encode())).hexdigest() == hash:
                Handler(Error_Levels.Alert, "SHA384 hash found !", "Value: " + Password)
                Found = True
                break
            elif Verbose:
                Handler(Error_Levels.Failed_Job, 'Testing "' + Password + '" ...')
    elif Choose == 8:
        # SHA3-384
        for Password in Password_List:
            if hashlib.sha3_384(bytes(Password.encode())).hexdigest() == hash:
                Handler(Error_Levels.Alert, "SHA3_384 hash found !", "Value: " + Password)
                Found = True
                break
            elif Verbose:
                Handler(Error_Levels.Failed_Job, 'Testing "' + Password + '" ...')
    elif Choose == 9:
        # SHA-512
        for Password in Password_List:
            if hashlib.sha512(bytes(Password.encode())).hexdigest() == hash:
                Handler(Error_Levels.Alert, "SHA512 hash found !", "Value: " + Password)
                Found = True
                break
            elif Verbose:
                Handler(Error_Levels.Failed_Job, 'Testing "' + Password + '" ...')
    elif Choose == 10:
        # SHA3-512
        for Password in Password_List:
            if hashlib.sha3_512(bytes(Password.encode())).hexdigest() == hash:
                Handler(Error_Levels.Alert, "SHA3-512 hash found !", "Value: " + Password)
                Found = True
                break
            elif Verbose:
                Handler(Error_Levels.Failed_Job, 'Testing "' + Password + '" ...')
    # If not found
    if not Found:
        gpl_clear_and_banner()
        Handler(Error_Levels.Failed_Job, 'Sorry. this hash not in Password list.')
elif Choose == 11:
    Options = ['Enter key and value to get encoded value.', 'Enter encoded value and key to get decoded value.', 'Enter value and encoded to get key.']
    Choose = gpl_while_input('Select Once:', Options)
    if Choose == 1:
        # encoded = XOR of value & key
        Key = gpl_input('Enter key: ')
        Value = gpl_input('Enter value to encode: ')
        Handler(Error_Levels.Alert, 'Encoded value with XOR:', 'Value: ' + gpl_xor(Key, Value))
    elif Choose == 2:
        # decoded = XOR of key & encoded
        Key = gpl_input('Enter key: ')
        Encoded = gpl_input('Enter encoded value: ')
        Handler(Error_Levels.Alert, 'Decoded value with XOR:', 'Value: ' + gpl_xor(Key, Encoded))
    else:
        # key = XOR of encoded & value
        Value = gpl_input('Enter value: ')
        Encoded = gpl_input('Enter encoded value: ')
        Handler(Error_Levels.Alert, 'Decoded value with XOR:', 'Value: ' + gpl_xor(Value, Encoded))
