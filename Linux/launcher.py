#!/usr/bin/python
# coding: utf-8
try:
	import sys
	import os
	import subprocess
	from termcolor import colored
except:
	print("Some libs not installed. run 'pip install -r requires.txt' to install.")
else:
	if str(sys.version_info[0]) == '3':
		try:
			subprocess.call(os.path.dirname(os.path.abspath(__file__)) + '/main_py3.py')
		except Exception as EX:
			if '[Errno 13] Permission denied: ' in str(EX):
				print(colored("'main_py3.py' is not have enough access to run.",'yellow'))
				exit(1)
			elif '[Errno 2] No such file or directory: ' in str(EX):
				print(colored('[!] ','red') + colored("'main_py3.py' file deleted or your're using soft/hard links !",'yellow'))
				exit(1)
			else:
				print(colored('G3nius Tools crashed !','red'))
				print(colored('ERROR:','red'))
				print(EX)
				exit(1)
		except:
			exit(0)
	elif str(sys.version_info[0]) == '2':
		try:
			subprocess.call(os.path.dirname(os.path.abspath(__file__)) + '/main_py2.py')
		except Exception as EX:
			if str(EX) == '[Errno 13] Permission denied':
				print(colored("'main_py2.py' is not have enough access to run.",'yellow'))
				exit(1)
			elif str(EX) == '[Errno 2] No such file or directory':
				print(colored('[!] ','red') + colored("'main_py2.py' file deleted or your're using soft/hard links !",'yellow'))
				exit(1)
			else:
				print(colored('G3nius Tools crashed !','red'))
				print(colored('ERROR:','red'))
				print(EX)
				exit(1)
		except:
			exit(0)
	else:
		print('Your python version not supported. Use python version upper or same 2.0.0 .')
