#!/usr/bin/python
# coding: utf-8
try:
	import sys
	import os
	import subprocess
	from colorama import Fore,Back,init
except:
	print("Some libs not installed. run 'pip install -r requires.txt' to install.")
else:
	init()
	if str(sys.version_info[0]) == '3':
		try:
			theproc = subprocess.Popen([sys.executable, sys.path[0] + "\\main_py3.py"])
			theproc.communicate()
		except Exception as EX:
			if '[Errno 13] Permission denied: ' in str(EX):
				print(Fore.YELLOW + "'main_py3.py' is not have enough access to run.")
				exit(1)
			elif '[Errno 2] No such file or directory: ' in str(EX):
				print(Fore.RED + '[!] ' + Fore.YELLOW + "'main_py3.py' file deleted or your're using soft/hard links !")
				exit(1)
			else:
				print(Fore.RED + 'G3nius Tools crashed !')
				print(Fore.RED + 'ERROR:')
				print(EX)
				exit(1)
		except:
			exit(0)
	elif str(sys.version_info[0]) == '2':
		try:
			theproc = subprocess.Popen([sys.executable, sys.path[0] + "\\main_py2.py"])
			theproc.communicate()
		except Exception as EX:
			if str(EX) == '[Errno 13] Permission denied':
				print(colored("'main_py2.py' is not have enough access to run.",'yellow'))
				exit(1)
			elif str(EX) == '[Errno 2] No such file or directory':
				print(Fore.RED + '[!] ' + Fore.YELLOW + "'main_py2.py' file deleted or your're using soft/hard links !")
				exit(1)
			else:
				print(Fore.RED + 'G3nius Tools crashed !')
				print(Fore.RED + 'ERROR:')
				print(EX)
				exit(1)
		except:
			exit(0)
	else:
		print('Your python version not supported. Use python version upper or same 2.0.0 .')
