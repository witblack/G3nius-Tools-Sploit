# libs
from subprocess import call
from sys import modules, exc_info
from lib.core.End_Plugin import EndScript_Class

# if crashed at import mode, return linenumber
def Run_File(file_address, subprocess_call=True):
    if subprocess_call:
        # call
        call(file_address)
    else:
        # run with g3nius-tools libs
        try:
            __import__(file_address)
            #exec('import ' + file_address)
        except EndScript_Class:
            # Ended with End_Plugin
            del modules[file_address]
            return None
        except Exception as Ex:
            # finders functions
            def Find_Error_Line(exc_tb):
                while True:
                    if hasattr(exc_tb, 'tb_next') and exc_tb.tb_next != None:
                        # go to deeper layer
                        exc_tb = exc_tb.tb_next
                    else:
                        # return line number
                        return exc_tb.tb_lineno

            def Find_Error_File(exc_tb):
                return exc_tb.tb_frame.f_locals['file_address'].replace('.', '/') + '.py'
            # create pointers
            exc_type, exc_obj, exc_tb = exc_info()
            # crash, return line number
            FileName = Find_Error_File(exc_tb)
            Line_Number = Find_Error_Line(exc_tb)
            del exc_type, exc_obj, exc_tb
            return [FileName, Line_Number, Ex]
        else:
            # exit without error
            del modules[file_address]
            return None