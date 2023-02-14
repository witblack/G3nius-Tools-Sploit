"""     libs    """
from PIL import ImageGrab

"""     GPL     """
# get pixel RGB code from screen
#
# modules:
# from PIL import ImageGrab
#
# version:
# 1
def gpl_screen_pixel_color(x_pixel, y_pixel):
    try:
        Image = ImageGrab.grab()
        return Image.getpixel((x_pixel, y_pixel))
    except:
        return False

