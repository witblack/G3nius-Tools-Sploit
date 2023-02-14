"""     libs    """
# Internal
from lib.GPL.IO import gpl_sleep

# External
from pynput.keyboard import Controller, Listener

# Configs
from lib.config.GPL import Macro_Apply_Time


"""     FACADE      """
from pynput.keyboard import Key


"""     Global       """
Keyboard = Controller()


"""     GPL     """
# set callback function for get keyboard events
#
# modules:
# from pynput.keyboard import Listener
#
# version:
# 1
def gpl_keyboard_callback(on_press=None, on_release=None):
    try:
        listener = Listener(on_press=on_press, on_release=on_release)
        listener.start()
        return listener
    except:
        return None
    else:
        return True




# wait for keyboard listener
#
# version:
# 1
def gpl_keyboard_join(listener):
    try:
        listener.join()
    except:
        return None
    else:
        return True



# type a text with keyboard
#
# modules:
# from pynput.keyboard import Controller
#
# NOTE:
# This function only support ANSI characters
# If this function can't type full string,
# Increase "Macro_Apply_Time" at config file
#
# version:
# 1
def gpl_keyboard_type(text:str):
    try:
        for character in text:
            Keyboard.type(character)
            gpl_sleep(Macro_Apply_Time)
    except:
        return None


# press hot key on keyboard
#
# version:
# 1
def gpl_keyboard_press(key:Key, hot_key:Key=None):
    try:
        if hot_key:
            with Keyboard.pressed(hot_key):
                Keyboard.press(key)
                Keyboard.release(key)
        else:
            Keyboard.press(key)
    except:
        return False
    else:
        return True


# release key on keyboard
#
# version:
# 1
def gpl_keyboard_release(key:Key):
    try:
        Keyboard.release(key)
    except:
        return False
    else:
        return True
