# libs
from subprocess import call
from sys import modules
from sys import exc_info
from os.path import split

# if crashed at import mode, return linenumber
def Run_File(file_address, subprocess_call=True):
    if subprocess_call:
        # call
        call(file_address)
    else:
        # run with g3nius-tools libs
        try:
            exec('import ' + file_address)
        except:
            # crash, return line number
            exc_type, exc_obj, exc_tb = exc_info()
            FileName = split(exc_tb.tb_frame.f_code.co_filename)[1]
            Line_Number = exc_tb.tb_next.tb_next.tb_lineno
            del exc_type, exc_obj, exc_tb
            return [FileName, Line_Number]
        else:
            del modules[file_address]