#!/usr/bin/python3
# coding: utf-8
try:
	from sys import exit
	import sys
	from colorama import Fore,Back,init
	import os
	import shutil
	import subprocess
	from time import sleep
except:
	print('[!] Some deepends not installed.')
	print('Run "pip install -r requires.txt"')
	exit(1)
init()
try:
	from lib.functionsPyThree import *
except:
	print(Fore.RED + '[!] Failed to load some some local libs.')
	print(Fore.RED + "If you're sure to don't change local files report it.")
	print(Fore.RED + 'Email : admin@bugzone.ir')
	exit(1)
print(Fore.GREEN + '[ *** ] ' + Fore.WHITE + 'Starting G3n!us ..')
Location = sys.path[0]
Menu_Numebrs = 0
Plugins = []
if os.path.isdir(Location + '/tmp'):
	shutil.rmtree(Location + '/tmp')
elif os.path.isfile(Location + '/tmp'):
	os.remove(Location + '/tmp')
os.mkdir(Location + '/tmp')
def Clear():
	global Version
	if OS == 'Windows':
		os.system('cls')
	elif OS == 'Linux':
		print('\033c')
	else:
		print('\033c\x1bc')
	if OS == '':
		tmp_OS = 'Unknown'
	else:
		tmp_OS = OS
	print(Fore.RED + ' _______________________________________________________________________')
	print(Fore.RED + '|' + Fore.MAGENTA + ' ▒███▒ ▒████           █                ' + Fore.RED + '  |' + Fore.WHITE + ' Programmer info:          ' + Fore.RED + '|')
	print(Fore.RED + '|' + Fore.MAGENTA + '░█▒ ░█ █▒  ▓█          █                ' + Fore.RED + '  |---------------------------|')
	print(Fore.RED + '|' + Fore.MAGENTA + '█▒          █ █▒██▒    █    █   █  ▒███▒' + Fore.RED + '  |' + Fore.GREEN + ' Programmed by WitBlack    ' + Fore.RED + '|')
	print(Fore.RED + '|' + Fore.MAGENTA + '█          ▒█ █▓ ▒█    █    █   █  █▒ ░█' + Fore.RED + '  |' + Fore.WHITE + ' Github ~>                 ' + Fore.RED + '|')
	print(Fore.RED + '|' + Fore.MAGENTA + '█   ██   ███░ █   █    █    █   █  █▒░  ' + Fore.RED + '  |' + Fore.BLUE + 'Https://github.com/WitBlack' + Fore.RED + '|')
	print(Fore.RED + '|' + Fore.MAGENTA + '█    █     ▓█ █   █    █    █   █  ░███▒' + Fore.RED + '  |' + Fore.WHITE + ' Website ~>                ' + Fore.RED + '|')
	print(Fore.RED + '|' + Fore.MAGENTA + '█▒   █      █ █   █         █   █     ▒█' + Fore.RED + '  |' + Fore.BLUE + 'Https://BugZone.ir         ' + Fore.RED + '|',)
	print(Fore.RED + '|' + Fore.MAGENTA + '▒█░ ░█ █░  ▓█ █   █    █    █▒ ▓█  █░ ▒█' + Fore.RED + '  |' + Fore.WHITE + ' E-Mail ~>                 ' + Fore.RED + '|')
	print(Fore.RED + '|' + Fore.MAGENTA + ' ▒███▒ ▒████  █   █    █    ▒██▒█  ▒███▒' + Fore.RED + '  |' + Fore.BLUE + 'admin@bugzone.ir           ' + Fore.RED + '|')
	print(Fore.RED + '|' + Fore.RED + '                                 _________|___________________________|')
	print(Fore.RED + '|' + Fore.RED + '________________________________|' + Fore.MAGENTA + '                       ███           ' + Fore.RED + '|')
	print(Fore.RED + '|' + Fore.WHITE + ' Information :                  ' + Fore.RED + '|' + Fore.MAGENTA + ' ███████                 █           ' + Fore.RED + '|')
	print(Fore.RED + '|' + Fore.RED + '--------------------------------' + Fore.RED + '|' + Fore.MAGENTA + '    █                    █           ' + Fore.RED + '|')
	print(Fore.RED + '|' + Fore.BLUE + ' Python Version: ' + Fore.WHITE + '3              ' + Fore.RED + '|' + Fore.MAGENTA + '    █     ███    ███     █    ▒███▒  ' + Fore.RED + '|')
	print(Fore.RED + '|' + Fore.BLUE + " VERSION " + Fore.WHITE + Version + '                  ' + Fore.RED + '|' + Fore.MAGENTA + '    █    █▓ ▓█  █▓ ▓█    █    █▒ ░█  ' + Fore.RED + '|')
	print(Fore.RED + '|' + Fore.BLUE + ' OS: ' + Fore.WHITE + tmp_OS + '			 ' + Fore.RED + '|' + Fore.MAGENTA + '    █    █   █  █   █    █    █▒░    ' + Fore.RED + '|')
	print(Fore.RED + '|' + Fore.WHITE + '                                ' + Fore.RED + '|' + Fore.MAGENTA + '    █    █   █  █   █    █    ░███▒  ' + Fore.RED + '|')
	print(Fore.RED + '|' + Fore.WHITE + '                                ' + Fore.RED + '|' + Fore.MAGENTA + '    █    █   █  █   █    █       ▒█  ' + Fore.RED + '|')
	print(Fore.RED + '|' + Fore.WHITE + '                                ' + Fore.RED + '|' + Fore.MAGENTA + '    █    █▓ ▓█  █▓ ▓█    █░   █░ ▒█  ' + Fore.RED + '|')
	print(Fore.RED + '|' + Fore.WHITE + '                                ' + Fore.RED + '|' + Fore.MAGENTA + '    █     ███    ███     ▒██  ▒███▒  ' + Fore.RED + '|')
	print(Fore.RED + '|________________________________|_____________________________________|')
	print(Fore.RED + '| Warning:' + Fore.YELLOW + " Don't break or kill script while process runing.            " + Fore.RED + '|')
	print(Fore.RED + '|______________________________________________________________________|\n')
	del tmp_OS
def Generate_Menu(Plugin_List):
	ret = Fore.WHITE + 'Select Once:\n\n'
	for Plugin in Plugin_List:
		ret += Fore.GREEN + str(Plugin[0]) + ' ' + Fore.WHITE + Plugin[2]
	return ret
try:
	List = os.listdir(Location+'/plugins')
except:
	print(Fore.RED + "[!] Can't find plugins folder.")
	exit(1)
Name,Title,File,ID = None,None,None,0
for Name in List:
	ID += 1
	if not (os.path.isfile(Location + '/plugins/' + Name + '/main3.py') or os.path.isfile(Location + '/plugins/' + Name + '/main.py')):
		if os.path.isfile(Location + '/plugins/' + Name + '/main2.py'):
			print(Fore.YELLOW + '[!] Failed to load "' + Name + '" plugin.')
			print(Fore.YELLOW + "Becase it's writen for Python2 and you're using Python3.")
		else:
			print(Fore.RED + '[!] Failed to load "' + Name + '" plugin.')
			print(Fore.RED + 'Becase "main2.py" or "main3.py" or "main.py" file in script folder not exists.')
		ID -= 1
		try:
			sleep(2.5)
		except:
			exit(0)
		continue
	if not os.path.isfile(Location + '/plugins/' + Name + '/Title.txt'):
		print(Fore.RED + '[!] Failed to load "' + Name + '" plugin.')
		print(Fore.RED + 'Becase "Title.txt" file in script folder not exists.')
		ID -= 1
		try:
			sleep(2.5)
		except:
			exit(0)
		continue
	try:
		File = open(Location + '/plugins/' + Name + '/Title.txt','r')
		Title = File.read().replace("\n",'') + "\n"
		File.close()
	except:
		print(Fore.RED + '[!] Failed to load "' + Name + '" plugin.')
		print(Fore.RED + 'Becase "Title.txt" file in script folder not have read permission.')
		ID -= 1
		try:
			sleep(2.5)
		except:
			exit(0)
		continue
	if os.path.isfile(Location + '/plugins/' + Name + '/main3.py'):
		try:
			File = open(Location + '/plugins/' + Name + '/main3.py',encoding="ISO-8859-1")
			if File.read()[0:2] == '#!':
				OpenSource = True
			else:
				OpenSource = False
		except:
			print(Fore.RED + '[!] Failed to load "' + Name + '" plugin.')
			print(Fore.RED + 'Becase "main3.py" file in script folder not have read permission.')
			try:
				File.close()
			except:
				pass
			ID -= 1
			try:
				sleep(2.5)
			except:
				exit(0)
			continue
	else:
		try:
			File = open(Location + '/plugins/' + Name + '/main.py',encoding="ISO-8859-1")
			if File.read()[0:2] == '#!':
				OpenSource = True
			else:
				OpenSource = False
		except:
			print(Fore.RED + '[!] Failed to load "' + Name + '" plugin.')
			print(Fore.RED + 'Becase "main.py" file in script folder not have read permission.')
			try:
				File.close()
			except:
				pass
			ID -= 1
			try:
				sleep(2.5)
			except:
				exit(0)
			continue
	Plugins.append([ID,Name,Title,OpenSource])
Menu_Numebrs = ID
Plugins.sort()
del Name,Title,ID,File,OpenSource
if len(Plugins) == 0:
	print(Fore.RED + '[!] ' + Fore.YELLOW + 'No plugins were found health and available, So Exit.')
	exit(1)
print(Fore.GREEN + '[ *** ] G3n!us started successfully.')
while True:
	Clear()
	print(Generate_Menu(Plugins) + Fore.GREEN + str(Menu_Numebrs + 1) + Fore.WHITE + ' Exit')
	try:
		Choose = int(input(Fore.BLUE + '\n\nEnter your number: ' + Fore.WHITE))
	except:
		try:
			print(Fore.YELLOW + 'Invalid Choose')
			sleep(1)
			continue
		except:
			Clear()
			print(Fore.MAGENTA + 'Good by..')
			exit(0)
	if Choose == Menu_Numebrs + 1:
		Clear()
		print(Fore.MAGENTA + 'Good by..')
		exit(0)
	Find = False
	for Plugin in Plugins:
		if Plugin[0] == Choose:
			Find = True
			if Plugin[3]:
				if os.path.isfile(Location + '/plugins/' + Plugin[1] + '/main3.py'):
					try:
						File = open(Location + '/plugins/' + Plugin[1] + '/main3.py','r')
					except:
						print(Fore.RED + 'Runing ' + Plugin[1] + ' failed !')
						print(Fore.RED + 'Becase "main3.py" file in script folder not have read permission.','red')
					else:
						Clear()
						try:
							try:
								exec(File.read())
							except EndScript:
								pass
						except Exception as EX:
							print(Fore.RED + 'Some where plugin get error! Failed job(s).')
							print(Fore.RED + 'Error:')
							print(Fore.RED + str(EX))
						except:
							print(Fore.RED + 'Some where plugin get error! Failed job(s).')
						File.close()
						del File
				else:
					try:
						File = open(Location + '/plugins/' + Plugin[1] + '/main.py','r')
					except:
						print(Fore.RED + 'Runing ' + Plugin[1] + ' failed !')
						print(Fore.RED + 'Becase "main3.py" file in script folder not have read permission.')
					else:
						Clear()
						try:
							try:
								exec(File.read())
							except EndScript:
								pass
						except Exception as EX:
							print(Fore.RED + 'Some where plugin get error! Failed job(s).')
							print(Fore.RED + 'Error:')
							print(Fore.RED + str(EX))
						except:
							print(Fore.RED + 'Some where plugin get error! Failed job(s).')
						File.close()
						del File
			else:
				Clear()
				if os.path.isfile(Location + '/plugins/' + Plugin[1] + '/main3.py'):
					try:
						subprocess.call(Location + '/plugins/' + Plugin[1] + '/main3.py')
					except Exception as EX:
						if str(EX)[0:28] == '[Errno 8] Exec format error:':
							print(Fore.RED + "ERROR: This plugin not optimized for your CPU.")
							print(Fore.RED + "Check lastest update, May by i'ts Ok.")
						else:
							print(Fore.RED + 'Some where plugin get error! Failed job(s).')
							print(Fore.RED + 'Error:')
							print(Fore.RED + str(EX))
					except:
						print(Fore.RED + 'Some where plugin get error! Failed job(s).')
				else:
					try:
						subprocess.call(Location + '/plugins/' + Plugin[1] + '/main.py')
					except Exception as EX:
						if str(EX)[0:28] == '[Errno 8] Exec format error:':
							print(Fore.RED + "ERROR: This plugin not optimized for your CPU.")
							print(Fore.RED + "Check lastest update, May by i'ts Ok.")
						else:
							print(Fore.RED + 'Some where plugin get error! Failed job(s).')
							print(Fore.RED + 'Error:')
							print(Fore.RED + str(EX))
					except:
						print(Fore.RED + 'Some where plugin get error! Failed job(s).')
			break
	if Find:
		try:
			Choose = input(Fore.YELLOW + '[?] ' + Fore.WHITE + ' Work finished. Do you want exit from script ? [y/n] ' + Fore.WHITE)
		except:
			Clear()
			print(Fore.MAGENTA + 'Good by..')
			exit(0)
		if str.lower(Choose) == 'y' or str.lower(Choose) == 'yes' or str.lower(Choose) == 'exit':
			Clear()
			print(Fore.BLUE + 'Good by..')
			exit(0)
	else:
		print(Fore.RED + 'Plugin not found!')
