"""     libs    """
from random import choice
from json import loads, dumps
from urllib.parse import unquote, urlencode

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
def gpl_url_encode(str_or_params):
    if type(str_or_params) == dict:
        return urlencode(str_or_params)
    elif type(str_or_params) == str:
        return urlencode({'': str_or_params})[1:]
    else:
        raise Exception("URL encode input should be str or dict.")


# URL Encode
#
# version
# 1
def gpl_url_decode(string):
    return unquote(string)


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
    URI = URI.replace("\\", "\\\\")
    Charecters = ['"', '!', '$', '`']
    for Charecter in Charecters:
        URI = URI.replace(Charecter, '\\' + Charecter)
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



# JSON Loader
#
# modules:
# from json import loads
#
# version:
# 2
def gpl_JSON_loads(JSON_String):
    try:
        return loads(JSON_String)
    except:
        return None


# JSON Dumper
#
# modules:
# from json import dumps
#
# version:
# 2
def gpl_JSON_dumps(JSON_String):
    try:
        return dumps(JSON_String)
    except:
        return None
