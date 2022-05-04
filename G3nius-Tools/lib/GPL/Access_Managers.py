"""     libs        """
# external
from os import getuid

# internal
from lib.core.Error_Handler import Handler
import lib.config.Error_Levels as Error_Levels
from lib.core.End_Plugin import End_Plugin
from lib.core.Exit_Request import Exit_Request

"""     GPL     """
def gpl_check_is_root():
    if getuid() == 0:
        return True
    else:
        return False

def gpl_check_root_needed_with_error(text='Access denie! Run again as Root.', description=None, end_plugin=False, exit_code=None, before_exit_text=None):
    if not gpl_check_is_root():
        Handler(Error_Levels.High, text, description)
        if end_plugin:
            End_Plugin()
        elif exit_code != None:
            Exit_Request(exit_code, text_after_clear=before_exit_text)