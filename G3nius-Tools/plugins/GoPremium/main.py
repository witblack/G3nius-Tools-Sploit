# import G3nius-Tools
# coding: utf-8

"""     libs       """
from lib.GPL.HTTP_Managers import gpl_http_get
from lib.core.Error_Handler import Handler
import lib.config.Error_Levels as Error_Levels

"""     show price      """
# get price
Price = gpl_http_get('https://api.bugzone.ir/G3nius/PremiumValue.txt', ok_http_codes=[200])
# no internet
if Price == None:
    Handler(Error_Levels.Critical, "Failed to connect server for get price. Check your internet connection.",)
else:
    # show
    Handler(Error_Levels.Alert, "It's only \x1b[6;32m" + Price + "\x1b[0m per month!")
    Handler(Error_Levels.Alert, "\n\nFor buy it send message with once of following liks:")
    Handler(Error_Levels.Alert, "\tWeb: https://bugzone.ir/")
    Handler(Error_Levels.Alert, "\tE-Mail: admin@bugzone.ir")
    Handler(Error_Levels.Alert, "\tInstagram: https://instagram.com/WitBlack80")
    Handler(Error_Levels.Alert, "\tTelegram: https://t.me/WitBlack")
    Handler(Error_Levels.Alert, "\tPhone: +98 9379446362\n\n")