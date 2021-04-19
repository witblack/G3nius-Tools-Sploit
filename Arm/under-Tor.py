#!/usr/bin/python
# coding: utf-8
try:
	from sys import exit
	import os
	from termcolor import colored
except:
	print("Some Deepends not installed. run 'pip install -r requires.txt'")
else:
	if '' in os.popen('proxychains').read():
		os.system('proxychains ./launcher.py')
	else:
		print(colored("[!] proxychains script not installed. install and retry.",'red'))
		exit(1)
