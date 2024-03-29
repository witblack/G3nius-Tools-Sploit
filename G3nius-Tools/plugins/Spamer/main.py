# import G3nius-Tools
# coding: utf-8

"""     libs       """
# Core
from lib.core.Error_Handler import Handler
# Config
import lib.config.Error_Levels as Error_Levels
# GPL
from lib.GPL.IO import gpl_input, gpl_sleep, gpl_confirm
from lib.GPL.Page_Managers import gpl_set_banner_verion, gpl_clear_and_banner
from lib.GPL.attackers.macro.Keyboard import gpl_keyboard_callback, gpl_keyboard_type, gpl_keyboard_release, gpl_keyboard_press, Key
# External
from time import sleep

"""     attacker    """
# Local vars
State = False
def Controller(key):
    global State
    if key == Key.end:
        State = False
        Handler(Error_Levels.Failed_Job, 'Attack stoped.')
    elif key == Key.ctrl_l or key == Key.ctrl_r:
        State = True
        Handler(Error_Levels.Alert, 'Attack started.')


"""     version     """
gpl_set_banner_verion("2.0.0")
gpl_clear_and_banner()


"""     ask     """
Attack_Text = gpl_input('Enter attack text with ANSI characters: ')
Sleep_Time = gpl_input("Enter sleep time between attacks (By sec): ", get_int=True)
Enter = gpl_confirm('Press enter key after type text [y/n] ? ', default_return_value=True)

"""     set up controller     """
Handler(Error_Levels.Info, "Use CTRL key to start attack, End key to stop.")
Handler(Error_Levels.Info, "Use CTRL+D to exit from plugin.")
Listener = gpl_keyboard_callback(on_press=Controller)


"""     attack      """
while True:
    # Do attack if on
    while State:
        gpl_keyboard_type(Attack_Text)
        if Enter:
            gpl_keyboard_press(Key.enter)
            gpl_keyboard_release(Key.enter)
        gpl_sleep(Sleep_Time)
    # timeout
    try:
        sleep(1)
    except (KeyboardInterrupt, EOFError):
        Listener.stop()
        break
