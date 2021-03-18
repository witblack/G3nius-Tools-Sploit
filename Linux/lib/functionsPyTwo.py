#!/usr/bin/python2
# coding: utf-8
import os
import random
import time
from termcolor import colored
OS = None
Location = os.path.dirname(os.path.abspath(__file__))
Version = '1.0.3'
Type = 'Linux' # can be : ARM - Windows - Linux
if str.lower(os.name) == 'nt':
	OS = 'Windows'
elif str.lower(os.name) == 'posix':
	OS = 'Linux'
else:
	OS = ''
	print(colored('[!] ', 'red') + colored('Your os not support, Sometimes it may be not working. Continue after 7 S..'))
	time.sleep(7)
class EndScript(Exception):
	pass
def End():
	raise EndScript
def FixSpase(String,Lenth):
	if len(String) < Lenth:
		return String + (' ' * ( Lenth - len(String)))
	else:
		return String
def randStr(Size,Chars=['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']):
	return ''.join(random.choice([Chars]) for _ in range(Size))
