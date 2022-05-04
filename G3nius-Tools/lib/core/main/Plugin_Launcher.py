"""     libs        """
from os import chmod
from lib.core.Run_File import Run_File
from lib.core.End_Plugin import End_Plugin, EndScript_Class
from lib.core.Error_Handler import Handler
import lib.config.Error_Levels as Error_Levels
from lib.core.G3nius_Location import G3nius_Location

"""     Launch      """
# Stractrue:
# {'ID': 1, 'Name': 'ddos', 'Title': 'do ddos', 'File_Address': '/path/to/main.py', 'Import_G3nius': False}
def Plugin_Launcher(Plugin):
    # check open source
    if Plugin['Import_G3nius']:
        # run source with g3nius-tools libs
        try:
            Crash_Details = Run_File('plugins.' + Plugin['Name'] + '.main', subprocess_call=False)
        except EndScript_Class:
            return
        except (KeyboardInterrupt, EOFError):
            Handler(Error_Levels.Failed_Job, 'Plugin ended with user request.')
        except Exception as EX:
            Handler(Error_Levels.Failed_Job, "Plugin crashed! Can't find & say line number to you :(", str(EX))
        else:
            if Crash_Details != None:
                Handler(Error_Levels.Failed_Job, "Plugin crashed at: '" + G3nius_Location() + '/' + Crash_Details[0] + "' Line: " + str(Crash_Details[1]))
    else:
        # close source
        try:
            Run_File(Plugin['File_Address'])
        except PermissionError:
            try:
                chmod(Plugin['File_Address'], 0o771)
            except:
                Handler(Error_Levels.Failed_Job, 'File address "' + Plugin['File_Address'] + '" not have execute access!')
            else:
                Plugin_Launcher(Plugin)
        except Exception as EX:
            if str(EX)[0:28] == '[Errno 8] Exec format error:':
                Handler(Error_Levels.Failed_Job, "This plugin isn't for your CPU (ARM or AMD) or not have SheBang.", "SheBang is first line at file, should thats like: #!/bin/python3")
            else:
                Handler(Error_Levels.Failed_Job, "Plugin crashed!", "Exception:\t" + str(EX))
        except:
            Handler(Error_Levels.Failed_Job, "Plugin crashed!")