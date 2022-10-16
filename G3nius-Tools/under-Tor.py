#!/usr/bin/python3
# coding: utf-8
try:
	from sys import exit
	from os import system, popen
	from os.path import basename, abspath
except:
	print("\x1b[0;31mSome Depends not installed. Run as root/administrator: 'pip install -r requires.txt'\x1b[0m")
else:
	if 'ProxyChains' in popen('proxychains').read():
		system('proxychains ./launcher.py')
	else:
		print("\x1b[0;31m[!] proxychains script not installed. install and retry.\x1b[0m")
		exit(1)