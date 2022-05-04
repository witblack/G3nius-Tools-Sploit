"""     libs    """
from random import choice

"""     GPL     """

# fix_spases
#
# version
# 1
def gpl_fix_spases(string,lenth,overflow=True,fill_with=' '): # lenth start from 1
    if len(string) < lenth:
        num = lenth - len(string)
        return (string + (fill_with * num))
    elif len(string) > lenth:
        if overflow:
            return string
        else:
            return string[:lenth]
    else:
        return string



# URL Encode
#
# version
# 1
def gpl_url_encode(string):
    return string.replace('#', '%23').replace('&', '%26').replace('/', '%2f').replace("\\", '%5C').replace(':', '%3A')



# Random String
#
# version
# 1
def gpl_random_string(Size,Chars=['0','1','2','3','4','5','6','7','8','9','A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z','`','~','!','@','#','$','%','^','&','*','(',')','-','=',"\\",'/','.',',',';',':',"'",'"','[',']','{','}','|','+','_','<','>','?']):
    String = ''
    for i in range(0,Size):
        String += choice(Chars)
    return String


# fix string to uri
#
# version
# 1
#
# note:
# use that's like:
# "yours/uri"
def gpl_fix_string_to_uri(URI, fix_for_without_double_quotation=False):
    URI = URI.replace('\\', '\\\\')
    Charecters = ['"', '!']
    for Charecter in Charecters:
        URI = URI.replace(Charecter, "\\" + Charecter)
    if fix_for_without_double_quotation:
        Charecters = ["'", '&', ';', '|', '(', ')', '%', '$', '*', '?', '>', '[', ']', '`']
        for Charecter in Charecters:
            URI = URI.replace(Charecter, "\\" + Charecter)
    return URI

# convert everything to byte
#
# version
# 1
def gpl_convert_to_bytes(data):
    typ = type(data)
    if typ == str:
        data = data.encode()
    elif typ == int:
        data = str(data).encode()
    elif typ != bytes:
        data = bytes(data)
    del typ
    return data