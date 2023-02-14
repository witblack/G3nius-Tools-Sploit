"""     libs    """
from pynput.mouse import Controller, Listener

"""     FACADE      """
from pynput.mouse import Button


"""     Global       """
Mouse_Controller = Controller()
Mouse_Listener = Listener()

"""     GPL     """
# click on a position
#
# modules:
# from pynput.mouse import Controller
# from pynput.mouse import Button
#
# version:
# 1
def gpl_mouse_click(left_click=True, right_click=False, middle_click=False):
    if left_click:
        Mouse_Controller.click(Button.left)
    elif right_click:
        Mouse_Controller.click(Button.right)
    elif middle_click:
        Mouse_Controller.click(Button.middle)
    else:
        return False
    return True



# click on a position
#
# modules:
# from pynput.mouse import Controller
# from pynput.mouse import Button
#
# version:
# 1
def gpl_mouse_move(x_pixel, y_pixel):
    try:
        Mouse_Controller.move(x_pixel, y_pixel)
    except:
        return False
    else:
        return True



# click on a position
#
# modules:
# from pynput.mouse import Controller
# from pynput.mouse import Button
#
# version:
# 1
def gpl_mouse_set_position(x_pixel, y_pixel):
    try:
        Mouse_Controller.position = (x_pixel, y_pixel)
    except:
        return False
    else:
        return True



# click on a position
#
# modules:
# from pynput.mouse import Controller
# from pynput.mouse import Button
#
# version:
# 1
def gpl_mouse_set_callback(on_move=None ,on_click=None ,on_scroll=None):
    try:
        return Listener(on_click=on_click, on_move=on_move, on_scroll=on_scroll)
    except:
        return False
    else:
        return True
