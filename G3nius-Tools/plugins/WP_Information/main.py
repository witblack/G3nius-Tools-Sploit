# import G3nius-Tools
# coding: utf-8

"""     libs       """
# GPL
from lib.classes.gpl import gpl_set_banner_verion, gpl_clear_and_banner
from lib.classes.gpl import gpl_input, gpl_http_get
from lib.classes.gpl import Handler, Error_Levels
from lib.classes.gpl import End_Plugin
from lib.classes.gpl import gpl_wordpress_exists

# Configs
from lib.config.GPL import Wordpress_Theme_Path

"""     Version       """
gpl_set_banner_verion("2.0.0")

"""     Ask     """
gpl_clear_and_banner()
Handler(Error_Levels.Info, 'Use WP_UserFinder plugin for detect real user without Brute-Force.')
URL = gpl_input("Enter URL of wordpress website: ", get_URL=True, clear_before=False)


"""     Check wordpress exists       """
if not gpl_wordpress_exists(URL):
    Handler(Error_Levels.Failed_Job, "Can't detect wordpress installation!")
    End_Plugin()


"""     Attack      """
gpl_clear_and_banner()
Handler(Error_Levels.Star, "Please wait, Detecting...")

# Theme name
Request = gpl_http_get(URL)
Theme_Name = Request.text.split(Wordpress_Theme_Path)[1].split('/')[0]

# License
Request = gpl_http_get(URL + '/license.txt')
if Request.status_code == 200:
    License = True
else:
    License = False

# wp_login.php
Request = gpl_http_get(URL + '/wp-login.php')
if Request.status_code == 200:
    WP_Login = True
else:
    WP_Login = False

# xml-rpc.php
Request = gpl_http_get(URL + '/xml-rpc.php')
if Request.status_code == 200:
    XML_RPC = True
else:
    XML_RPC = False

# wp-cron.php
Request = gpl_http_get(URL + '/wp-cron.php')
if Request.status_code == 200:
    WP_Corn = True
else:
    WP_Corn = False

# wp-cron.php
Request = gpl_http_get(URL + '/wp-json/wp/v2/users/')
if Request.status_code == 200:
    JSON_Users = True
else:
    JSON_Users = False


"""     Report      """
gpl_clear_and_banner()

Handler(Error_Levels.Plus, f"Theme name:\t{Theme_Name}")

if License:
    Handler(Error_Levels.Plus, f"License:\t{URL}/license.txt")
else:
    Handler(Error_Levels.Minus, f"License:\tNot found!")

if WP_Login:
    Handler(Error_Levels.Plus, f"Login form:\t{URL}/wp-login.php")
else:
    Handler(Error_Levels.Minus, f"Login form:\tNot found!")

if XML_RPC:
    Handler(Error_Levels.Plus, f"XML RPC:\t{URL}/xml-rpc.php")
else:
    Handler(Error_Levels.Minus, f"XML RPC:\tNot found!")

if WP_Corn:
    Handler(Error_Levels.Plus, f"WP Corn:\t{URL}/wp-cron.php")
else:
    Handler(Error_Levels.Minus, f"WP Corn:\tNot found!")

if JSON_Users:
    Handler(Error_Levels.Plus, f"Users JSON:\t{URL}/wp-json/wp/v2/users/")
else:
    Handler(Error_Levels.Minus, f"Users JSON:\tNot found!")
