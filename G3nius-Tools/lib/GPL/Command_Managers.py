"""     libs        """
from os import popen

# configs, add to end command
NoOutPut = ' 1> /dev/null 2>&1'
return_ERROR_if_error = " || echo 'ERROR'"
Under_NoHup = 'nohup '
Without_Error = ' 2> /dev/null'

# Run list of OS commands
#
# modules:
# from os import popen
#
# version:
# 1
def gpl_run_OS_command(Commands):
    if type(Commands) == str:
        OutPut = popen(Commands).read()
        if len(OutPut) > 1 and OutPut[-1] == "\n":
            OutPut = OutPut[:-1]
        return OutPut
    elif type(Commands) == list:
        OutPuts = []
        for Command in Commands:
            OutPut = popen(Command).read()
            if len(OutPut) > 1 and OutPut[-1] == "\n":
                OutPut = OutPut[:-1]
            OutPuts.append(OutPut)
        return OutPuts


# check existing command
#
# internal modules:
# gpl_run_OS_command
#
# version:
# 1
def gpl_check_command_exists(Commands, Custom_PATH=None):
    if type(Commands) == str:
        Commands = [Commands]
    for Command in Commands:
        if Custom_PATH != None:
            OutPut = gpl_run_OS_command('PATH=' + Custom_PATH + NoOutPut + ' && whereis ' + Command)
        else:
            OutPut = gpl_run_OS_command('whereis ' + Command)
        if len(OutPut) == len(Command) + 1:
            return False
        return True