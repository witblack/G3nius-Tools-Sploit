# libs
from lib.core.OS_Detector import OS
from lib.core.Error_Handler import Handler
import lib.config.Error_Levels as Error_Levels

"""     check supported     """
# don't exit or end plugin
def Check_Supported(Windows=False, Linux=False, Unknown=False, on_unsupported_OS_text=None):
    if OS == 'Windows':
        if Windows:
            return True
        else:
            return False
    elif OS == 'Linux':
        if Linux:
            return True
        else:
            return False
    else:
        # unknown OS
        if Unknown:
            if on_unsupported_OS_text:
                Handler(Error_Levels.Alert, on_unsupported_OS_text)
            return True
        else:
            return False