#!/usr/bin/python3
# coding: utf-8

"""     libs       """
try:
    # external
    from os import system, remove, getcwd
    from os.path import isdir, isfile
    from sys import argv, exit

    # internal
    from lib.packages.termcolor import colored

    # core
    from lib.core.Check_Supported_OS import Check_Supported
    from lib.core.G3nius_Location import G3nius_Location
    from lib.core.Error_Handler import Handler

    # GPL
    from lib.GPL.Access_Managers import gpl_check_root_needed_with_error

    # configs
    import lib.config.Error_Levels as Error_Levels
    import lib.config.Exit_Codes as Exit_Codes

    # installers
    from lib.core.installers.installer_uninstaller import Install_G3nius, Uninstall_G3nius, Reinstall_G3nius
    from lib.core.installers.check import Check_Installtion_G3nius
except ModuleNotFoundError:
    print('\x1b[0;31m[!] Some depends not installed.')
    print('Run "pip install -r requires.txt"\x1b[0m')
else:
    Check_Supported(Linux=True)
    gpl_check_root_needed_with_error(Exit_Codes.CanNotExecute)
    if '-h' in argv or '--help' in argv or len(argv) == 1:
        # help page
        print('\x1b[0;29mHelp Page for installer/uninstaler:\x1b[0m\n\n')
        print(colored('-h', 'green') + colored(' , ', 'green') + colored('--help', 'green') + '\t~>\t' + colored('Show help page.', 'white'))
        print(colored('-c', 'green') + colored(' , ', 'green') + colored('--check', 'green') + '\t~>\t' + colored('Check status of installion.', 'white'))
        print(colored('-i', 'green') + colored(' , ', 'green') + colored('--install', 'green') + '\t~>\t' + colored('Install G3nius-Tools.', 'white'))
        print(colored('-un', 'green') + colored(' , ', 'green') + colored('--uninstall', 'green') + '\t~>\t' + colored('Uninstall G3nius-Tools.', 'white'))
        print(colored('\n\nDefault installion path:', 'green'))
        print(colored('\t/usr/share/G3nius-Tools', 'blue'))
    elif '-c' in argv or '--check' in argv:
        # check installion
        Check_Installtion_G3nius()
    elif '-i' in argv or '--install' in argv:
        # install
        Install_G3nius()
    elif '-un' in argv or '--uninstall' in argv:
        # uninstall
        Uninstall_G3nius()
    else:
        Handler(Error_Levels.Failed_Job, "Invalid parameters!")
        exit(Exit_Codes.InvalidArgument)
    exit(Exit_Codes.Normal)