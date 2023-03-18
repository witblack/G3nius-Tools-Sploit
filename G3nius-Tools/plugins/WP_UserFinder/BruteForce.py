"""     libs       """
# GPL
from lib.classes.gpl import gpl_http_get, Handler, Error_Levels

# configs
from plugins.WP_UserFinder.Configs import Author_BruteForce_URI

# holders
import plugins.WP_UserFinder.Holders as Holders



"""     Attack      """
def Login_Brute_Force(Username):
    # Attack
    Request = gpl_http_get(Holders.URL + Author_BruteForce_URI + Username)
    if Request.status_code == 200:
        Holders.Users.append(Username)
        Handler(Error_Levels.Plus, f"Username Found:\t{Username}")
    elif Request.status_code == 404 and Holders.Verbose:
        Handler(Error_Levels.Minus, f"Username '{Username}' not exists.")
    elif Request.status_code != 404:
        Handler(Error_Levels.Minus, "Brute-Force failed, May be blocked by WAF.", f"HTTP status code:\t{Request.status_code}")
        Holders.HTTP_Error = True
