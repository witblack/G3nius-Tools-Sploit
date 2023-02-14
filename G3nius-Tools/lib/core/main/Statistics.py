"""     libs       """
from lib.GPL.HTTP_Managers import gpl_http_get
from lib.config.Main_Configs import Statistics_Reports

"""     defs       """
def Send_Statistics(Type="Usage"):
    if Statistics_Reports:
        if Type == 'Usage':
            gpl_http_get("https://api.bugzone.ir/G3nius/Statistics.php?Type=Usage", ok_http_codes=[200])
        else:
            raise("Invalid type given.")
