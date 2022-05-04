"""     GPL     """
def gpl_xor(Str1, Str2):
    Size = min(len(Str1), len(Str2))
    Result = ''
    for i in range(Size):
        Result = Result + '%c' % (ord(Str1[i]) ^ ord(Str2[i]))
    return Result