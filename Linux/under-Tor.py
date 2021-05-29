#!/usr/bin/python
# coding: utf-8
try:
	from sys import exit
	import os
except:
	print("\x1b[0;31mSome Deepends not installed. run 'pip install -r requires.txt'\x1b[0m")
else:
	if '' in os.popen('proxychains').read():
		os.system('proxychains ./launcher.py')
	else:
		print("\x1b[0;31m[!] proxychains script not installed. install and retry.\x1b[0m")
		exit(1)
