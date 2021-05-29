#!/usr/bin/python
# coding: utf-8
try:
    import os
    import sys
except:
    print('\x1b[0;31m[!] Some deepends not installed.')
    print('Run "pip install -r requires.txt"\x1b[0m')
else:
    if '-h' in sys.argv or '--help' in sys.argv or len(sys.argv) == 1:
        print('\x1b[0;29mHelp Page for installer/uninstaler:\x1b[0m\n')
        print('     \x1b[0;32m-h\x1b[0m\x1b[0;35m , \x1b[0m\x1b[0;32m--help\x1b[0m\x1b[0;34m       ~>  \x1b[0m\x1b[0;3mShow help page.')
        print('     \x1b[0;32m-c\x1b[0m\x1b[0;35m , \x1b[0m\x1b[0;32m--check\x1b[0m\x1b[0;34m      ~>  \x1b[0m\x1b[0;3mCheck status of installion.')
        print('     \x1b[0;32m-r\x1b[0m\x1b[0;35m , \x1b[0m\x1b[0;32m--reinstall\x1b[0m\x1b[0;34m  ~>  \x1b[0m\x1b[0;3mReinstall.')
        print('     \x1b[0;32m-u\x1b[0m\x1b[0;35m , \x1b[0m\x1b[0;32m--uninstall\x1b[0m\x1b[0;34m  ~>  \x1b[0m\x1b[0;3mUninstall.')
        print('     \x1b[0;32m-i\x1b[0m\x1b[0;35m , \x1b[0m\x1b[0;32m--install\x1b[0m\x1b[0;34m  ~>  \x1b[0m\x1b[0;3mInstall.\n')
    elif '-r' in sys.argv or '--reinstall' in sys.argv:
        if os.path.isfile('/bin/g3nius-tools'):
            if os.path.isdir('/bin/g3nius-tools'):
                print('\x1b[0;33mERROR:')
                print(" Can't install. This directory exists:")
                print("     /bin/g3nius-tools")
                print('See more information at ./install-uninstall.py -h')
                sys.exit(1)
            try:
                file = open('/bin/g3nius-tools', 'w')
                file.write("#!/bin/sh\npython '" + os.getcwd().replace("'","\\'") + "/launcher.py' $1 $2 $3 $4 $5 $6 $7 $8 $9 $10 $11 $12 $13 $14 $15 $16 $17 $18 $19 $20 $21 $22 $23 $24 $25")
                file.close()
                os.system('chmod 0755 /bin/g3nius-tools')
            except:
                print('\x1b[0;31mError:')
                print(" Can't install, Please run this file with root permission.\x1b[0m")
            else:
                print('\x1b[0;32m[+] \x1b[0m\x1b[0;38mInstalled successfully. Reopen your terminal.\x1b[0m')
                print('\n\x1b[0;33mNOTE:\x1b[0m')
                print("\x1b[0;34m   Installion files don't should be delete or move.")
                print("   \x1b[0m\x1b[0;35mg3nius-tools\x1b[0m\x1b[0;34m command will be called here.\x1b[0m\n")
                print("   run ./install-uninstall.py -h to see more information.\n")
        else:
            print('\x1b[0;33mG3nius-tools not installed, So not reinstall.\x1b[0m')
            print('See more information at ./install-uninstall.py -h')
    elif '-c' in sys.argv or '--check' in sys.argv:
        if os.path.isfile('/bin/g3nius-tools'):
            print('\x1b[0;32mG3nius-tools already installed.\x1b[0m')
        else:
            print('\x1b[0;33mG3nius-tools not installed.\x1b[0m')
    elif '-u' in sys.argv or '--uninstall' in sys.argv:
        if os.path.isfile('/bin/g3nius-tools'):
            try:
                os.remove('/bin/g3nius-tools')
            except:
                print('\x1b[0;31mError:')
                print(" Can't uninstall, Please run this file with root permission.\x1b[0m")
            else:
                print('\x1b[0;32mG3nius-tools uninstalled successfully!\x1b[0m')
                print("\n\x1b[0;33mWe're sorry we could not keep you satisfied :(")
                print('If you can, say us why uninstall G3nius-tools with E-Mail at:\x1b[0m')
                print("\x1b[0;34m     admin@BugZone.ir\x1b[0m\n")
        else:
            print('\x1b[0;31mG3nius-tools not installed, So not uninstall.\x1b[0m')
    elif '-i' in sys.argv or '--install' in sys.argv:
        if os.path.isfile('/bin/g3nius-tools'):
            print('\x1b[0;32mG3nius-tools already installed.')
            print('See more information at ./install-uninstall.py -h')
            print('run with command\x1b[0m:\x1b[0;34m g3nius-tools\x1b[0m')
            sys.exit(0)
        elif os.path.isdir('/bin/g3nius-tools'):
            print('\x1b[0;33mERROR:')
            print(" Can't install. This directory exists:")
            print("     /bin/g3nius-tools")
            print('See more information at ./install-uninstall.py -h')
            sys.exit(1)
        try:
            file = open('/bin/g3nius-tools','w')
            file.write("#!/bin/sh\npython '" + os.getcwd().replace("'","\\'") + "/launcher.py' $1 $2 $3 $4 $5 $6 $7 $8 $9 $10 $11 $12 $13 $14 $15 $16 $17 $18 $19 $20 $21 $22 $23 $24 $25")
            file.close()
            os.system('chmod 0755 /bin/g3nius-tools')
        except:
            print('\x1b[0;31mError:')
            print(" Can't install, Please run this file with root permission.\x1b[0m")
        else:
            print('\x1b[0;32m[+] \x1b[0m\x1b[0;38mInstalled successfully. Reopen your terminal.\x1b[0m')
            print('\n\x1b[0;33mNOTE:\x1b[0m')
            print("\x1b[0;34m   Installion files don't should be delete or move.")
            print("   \x1b[0m\x1b[0;35mg3nius-tools\x1b[0m\x1b[0;34m command will be called here.\x1b[0m\n")
            print("   run ./install-uninstall.py -h to see more information.\n")
    else:
        print('\x1b[0;31m[!] Invalid parameter.\x1b[0m')