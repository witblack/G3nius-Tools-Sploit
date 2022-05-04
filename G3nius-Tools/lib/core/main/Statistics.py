"""     libs       """
from lib.GPL.HTTP_Managers import gpl_http_get

"""     defs       """
def Send_Statistics(Report, Type="Usage"):
    if Report:
        if Type == 'Usage':
            gpl_http_get("https://api.bugzone.ir/G3nius/Statistics.php?Type=Usage", ok_http_codes=[200])
        else:
            raise("Invalid type given.")