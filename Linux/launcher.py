#!/usr/bin/python
# coding: utf-8
import time

try:
	import sys
	import os
except:
	print("\x1b[0;31m[!] Some libs not installed. run 'pip install -r requires.txt' to install.\x1b[0m")
else:
	if '-p' in sys.argv or '--python' in sys.argv:
		try:
			if '-p' in sys.argv:
				Python_Version = sys.argv[sys.argv.index('-p') + 1]
			else:
				Python_Version = sys.argv[sys.argv.index('--python') + 1]
		except:
			print('\x1b[0;33mPython version not found. Use Like:')
			print('	g3nius-tools -p <2_or_3>\x1b[0m')
			sys.exit(1)
		else:
			if '-p' in sys.argv:
				del sys.argv[sys.argv.index('-p') + 1]
				sys.argv = list(filter(('-p').__ne__, sys.argv))
			else:
				del sys.argv[sys.argv.index('--python') + 1]
				sys.argv = list(filter(('--python').__ne__, sys.argv))
	else:
		Python_Version = str(sys.version_info[0])
		if Python_Version == '2' and os.popen('python3 -V').read()[:6] == 'Python':
			Python_Version = '3'
	args = ''
	for arg in sys.argv[1:]:
		args += ' ' + arg
	if not (os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + '/main_py3.py') and os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + '/main_py2.py')):
		print("\x1b[0;31m[!]\x1b[0m\x1b[0;33m 'main_py3.py' or 'main_py2.py' file deleted, or your're using soft/hard links !\x1b[0m")
		exit(1)
	if Python_Version == '3':
		try:
			os.system('python3 "' + os.path.dirname(os.path.abspath(__file__)).replace('"','\\"') + '/main_py3.py"' + args)
		except Exception as EX:
			if '[Errno 13] Permission denied: ' in str(EX):
				print("\x1b[0;33mmain_py3.py' is not have enough access to run.\x1b[0m")
				exit(1)
			else:
				print('\x1b[0;31mG3nius Tools crashed !')
				print('ERROR:')
				print(EX + '\x1b[0m')
				exit(1)
		except:
			exit(0)
	elif Python_Version == '2':
		try:
			os.system('python2 "' + os.path.dirname(os.path.abspath(__file__)).replace('"','\\"') + '/main_py2.py"' + args)
		except Exception as EX:
			if str(EX) == '[Errno 13] Permission denied':
				print("\x1b[0;33m'main_py2.py' is not have enough access to run.\x1b[0m")
				exit(1)
			else:
				print('\x1b[0;31mG3nius Tools crashed !')
				print('ERROR:')
				print(EX + "\x1b[0m")
				exit(1)
		except:
			exit(0)
	else:
		print('\x1b[0;31mYour python version not supported. Use python version upper or same 2.0.0 .\x1b[0m')
