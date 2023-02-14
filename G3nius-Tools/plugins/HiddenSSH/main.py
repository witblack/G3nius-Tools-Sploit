# import G3nius-Tools
# coding: utf-8

"""     libs       """
# GPL
from lib.GPL.attackers.protocols.SSH import gpl_disconnect_SSH, gpl_connect_to_ssh, gpl_run_command_on_SSH
from lib.GPL.IO import gpl_input
from lib.GPL.Page_Managers import gpl_clear_and_banner, gpl_set_banner_verion

# Core
from lib.core.Error_Handler import Handler

# Configs
import lib.config.Exit_Codes as Exit_Codes
import lib.config.Error_Levels as Error_Levels
gpl_set_banner_verion('2.0.0')

"""     ask     """
IP = gpl_input('Enter target server IP: ', get_ip=True)
Port = gpl_input('Enter port: (Default: 22): ', get_port=True)
Username = gpl_input('Enter username: ')
Password = gpl_input('Enter password: ')

"""     connect     """
SSH_Controller = gpl_connect_to_ssh(IP, Username, Password, Port)
if not SSH_Controller:
    Handler(Error_Levels.Failed_Job, "Failed to Connect SSH. Please Check IP/Port/Username/Password.")
else:
    """     Connected, handler     """
    # Finishing connection
    gpl_clear_and_banner()
    Handler(Error_Levels.Alert, f"Connected, Talking to server...")
    # Detect first banner
    Result = gpl_run_command_on_SSH(SSH_Controller, 'echo -n ""')
    Banner_Stdout_lenth = len(Result['Stdout'])
    Banner_Stderr_lenth = len(Result['Stderr'])
    # Process PS1
    PS1 = gpl_run_command_on_SSH(SSH_Controller, 'echo -e $PS1')
    # Show .bashrc errors if exists
    if PS1['Stderr'] != b'':
        print(PS1['Stderr'])
    # Fix PS1
    PS1 = PS1['Stdout'][Banner_Stdout_lenth:]
    if PS1[-1] == "\n":
        PS1 = PS1[:-1]
    # Show connected
    Handler(Error_Levels.Alert, f"Successfully connected to {IP}:{Port}")
    del IP, Port, Username, Password
    # Ask command
    while True:
        Command = gpl_input(PS1, q_to_exit=False, clear_when_exit=False, clear_and_banner_before=False)
        if Command == 'exit' or Command == 'logout':
            break
        # Run command
        Result = gpl_run_command_on_SSH(SSH_Controller, Command)
        # Check if command not found
        if Result['ExitCode'] == Exit_Codes.CommandNotFound:
            Handler(Error_Levels.Failed_Job, 'Command not found !')
        elif Result['ExitCode'] != Exit_Codes.Normal:
            # Unknown error
            Handler(Error_Levels.Failed_Job, f"Exit Code: {Result['ExitCode']}")
        else:
            print(Result['Stdout'][Banner_Stdout_lenth:])
            print(Result['Stderr'][Banner_Stderr_lenth + Banner_Stdout_lenth:].decode())
    Handler(Error_Levels.Alert, 'Logged out successfully.')
    gpl_disconnect_SSH(SSH_Controller)
