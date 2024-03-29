# import G3nius-Tools
# coding: utf-8

"""     libs       """
# External
from threading import Thread

# GPL
from lib.classes.gpl import gpl_set_banner_verion, gpl_clear_and_banner
from lib.classes.gpl import gpl_input, gpl_while_input, gpl_confirm
from lib.classes.gpl import gpl_ask_load_from_file
from lib.classes.gpl import Handler, Error_Levels
from lib.classes.gpl import gpl_ask_save_to_file
from lib.classes.gpl import gpl_JSON_loads
from lib.classes.gpl import gpl_http_get
from lib.classes.gpl import End_Plugin
from lib.classes.gpl import gpl_sleep

# Brute-Force
from plugins.WP_UserFinder.BruteForce import Login_Brute_Force

# Configs
import plugins.WP_UserFinder.Configs as Configs

# Holders
import plugins.WP_UserFinder.Holders as Holders


"""     Version     """
gpl_set_banner_verion("2.0.0")


"""     Ask     """
# Website
Holders.URL = gpl_input("Enter URL of wordpress target: ", get_URL=True)

# Method
Methods = [
    'Users JSON method (Without Brute-Force + Information) (Recommended)',
    'Author method (Without Brute-Force)',
    'Brute-Force'
]
Method = gpl_while_input("Select once method to find users: ", Methods)



"""     Attack      """
gpl_clear_and_banner()
Handler(Error_Levels.Star, "Please wait, Extracting users...")

Holders.Users = []
if Method == 1:
    # Users JSON
    Request = gpl_http_get(Holders.URL + Configs.Users_JSON_URI, ok_http_codes=[200, 403, 404])
    if Request.status_code == 200:
        # Found
        Users = gpl_JSON_loads(Request.text)
        for User in Users:
            Handler(Error_Levels.Star, "\n\nNew user found:")
            Holders.Users.append(User['slug'])
            for Key in User:
                # Fix if empty
                if type(User[Key]) == str and len(User[Key]) == 0:
                    User[Key] = '""'
                # Show
                Handler(Error_Levels.Plus, f"\t{Key}\t~>\t{User[Key]}")
        gpl_confirm("Confirm to report page")
    elif Request.status_code == 403:
        Handler(Error_Levels.Minus, "Failed, This method blocked by WAF!", "Try another methods.")
    else:
        Handler(Error_Levels.Minus, "Failed, This method not work on this target.", "Try another websites.")
elif Method == 2:
    # Author ID
    i = 0
    Just_Count = False
    while True:
        i += 1
        Request = gpl_http_get(Holders.URL + Configs.Author_By_ID_URI + f"{i}")
        if Request.status_code == 200:
            Title = Request.text.split('<title>')[1].split('</title>')[0]
            if ' - ' in Title:
                Username = Title.split(' - ')[0]
                Holders.Users.append(Username)
                Handler(Error_Levels.Plus, f"User found:\t{Username}")
            elif not Just_Count:
                Confirm = gpl_confirm("Method worked, but can't detect username. Do you want count Users", True)
                if Confirm:
                  Just_Count = True
                else:
                    End_Plugin()
        elif Request.status_code == 404:
            if Just_Count:
                Handler(Error_Levels.Plus, f"This target have {i-1} admin accounts.")
                End_Plugin()
            break
        else:
            Handler(Error_Levels.Minus, "Method not work on this target! May be blocked by WAF.", f"HTTP status code: {Request.status_code}")
    if len(Holders.Users) == 0:
        Handler(Error_Levels.Minus, "Failed to detect username! Method not work on this target.")
else:
    # Brute-Force
    Usernames = gpl_ask_load_from_file("Enter usernames list file address: ", read_lines=True)
    Power = gpl_input("Enter attack power (Thread per sec): ", get_plus_number=True)
    Holders.Verbose = gpl_confirm("Run as verbose (Default no)", False, False)
    gpl_clear_and_banner()
    Handler(Error_Levels.Star, "Logs:\n")
    # Thread counter
    i = 0
    threads = []
    for Username in Usernames:
        # check if sleep need
        i += 1
        if i % Power == 0:
            gpl_sleep()
        # open brute-force thread
        thread = Thread(target=Login_Brute_Force, args=(Username,))
        thread.start()
        threads.append(thread)
        if Holders.HTTP_Error:
            End_Plugin()
    # wait to end
    for thread in threads:
        thread.join()



"""     Result      """
if len(Holders.Users) > 0:
    # Ask
    Options = [
        'Write result to file',
        'Show result'
    ]
    Choose = gpl_while_input("Select once:", Options)
    gpl_clear_and_banner()

    if Choose == 1:
        # Write to file
        Data = ''
        for Username in Holders.Users:
            Data += f"\n{Username}"
        gpl_ask_save_to_file("Enter filename address to write results: ", data=Data)
        Handler(Error_Levels.Plus, "File Wrote. Enjoy!")
    else:
        for Username in Holders.Users:
            Handler(Error_Levels.Plus, Username)
else:
    gpl_clear_and_banner()
    Handler(Error_Levels.Minus, "Method worked but no one users found!")
