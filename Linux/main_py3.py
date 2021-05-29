#!/usr/bin/python3
# coding: utf-8
print("\x1b[6;32m[ *** ] \x1b[0m\x1b[0;38m Starting G3n!us .. \x1b[0m\n")
try:
	try:
		from termcolor import colored
	except:
		from lib.Packages.termcolor import colored
	import os
	import sys
	import shutil
	import subprocess
	from time import sleep
except:
	try:
		print(colored('[!] Some deepends not installed.','red'))
		print(colored('Run "pip install -r requires.txt"','red'))
	except:
		print('\x1b[0;31m[!] ERROR:    Internal and external libs dameged :(\x1b[0m')
	exit(1)
try:
	from lib.functionsPyThree import *
except:
	print(colored('[!] Failed to load some some local libs.','red'))
	print(colored("If you're sure to don't change local files report it.",'red'))
	print(colored('Email : admin@bugzone.ir','red'))
	exit(1)
Location = os.path.dirname(os.path.abspath(__file__))
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
		print(os.popen('cls').read())
	elif OS == 'Linux':
		print('\033c')
	else:
		print('\033c\x1bc')
	if OS == '':
		tmp_OS = 'Unknown'
	else:
		tmp_OS = OS
	print(colored(' _______________________________________________________________________','red'))
	print(colored('|','red') + colored(' ▒███▒ ▒████           █                ','magenta') + colored('  |','red') + colored(' Programmer info:          ','white') + colored('|','red'))
	print(colored('|','red') + colored('░█▒ ░█ █▒  ▓█          █                ','magenta') + colored('  |','red') + colored('---------------------------|','red'))
	print(colored('|','red') + colored('█▒          █ █▒██▒    █    █   █  ▒███▒','magenta') + colored('  |','red') + colored(' Programmed by WitBlack    ','green') + colored('|','red'))
	print(colored('|','red') + colored('█          ▒█ █▓ ▒█    █    █   █  █▒ ░█','magenta') + colored('  |','red') + colored(' Github ~>                 ','white') + colored('|','red'))
	print(colored('|','red') + colored('█   ██   ███░ █   █    █    █   █  █▒░  ','magenta') + colored('  |','red') + colored('Https://github.com/WitBlack','blue') + colored('|','red'))
	print(colored('|','red') + colored('█    █     ▓█ █   █    █    █   █  ░███▒','magenta') + colored('  |','red') + colored(' Website ~>                ','white') + colored('|','red'))
	print(colored('|','red') + colored('█▒   █      █ █   █         █   █     ▒█','magenta') + colored('  |','red') + colored('Https://BugZone.ir         ','blue') + colored('|','red'))
	print(colored('|','red') + colored('▒█░ ░█ █░  ▓█ █   █    █    █▒ ▓█  █░ ▒█','magenta') + colored('  |','red') + colored(' E-Mail ~>                 ','white') + colored('|','red'))
	print(colored('|','red') + colored(' ▒███▒ ▒████  █   █    █    ▒██▒█  ▒███▒','magenta') + colored('  |','red') + colored('admin@bugzone.ir           ','blue') + colored('|','red'))
	print(colored('|','red') + colored('                                 _________|___________________________|','red'))
	print(colored('|','red') + colored('________________________________|','red') + colored('                       ███           ','magenta') + colored('|','red'))
	print(colored('|','red') + colored(' Information :                  ','white') + colored('|','red') + colored(' ███████                 █           ','magenta') + colored('|','red'))
	print(colored('|','red') + colored('--------------------------------','red') + colored('|','red') + colored('    █                    █           ','magenta') + colored('|','red'))
	print(colored('|','red') + colored(' Python Version: ','blue') + colored('3              ','white') + colored('|','red') + colored('    █     ███    ███     █    ▒███▒  ','magenta') + colored('|','red'))
	print(colored('|','red') + colored(' LICENSE: ','blue') + colored(FixSpase(License,22),'white') + colored('|','red') + colored('    █    █▓ ▓█  █▓ ▓█    █    █▒ ░█  ','magenta') + colored('|','red'))
	print(colored('|','red') + colored(' VERSION: ','blue') + colored(FixSpase(Version,22),'white') + colored('|','red') + colored('    █    █   █  █   █    █    █▒░    ','magenta') + colored('|','red'))
	print(colored('|','red') + colored(' OS: ','blue') + colored(FixSpase(tmp_OS,27),'white') + colored('|','red') + colored('    █    █   █  █   █    █    ░███▒  ','magenta') + colored('|','red'))
	print(colored('|','red') + colored('                                ','white') + colored('|','red') + colored('    █    █   █  █   █    █       ▒█  ','magenta') + colored('|','red'))
	print(colored('|','red') + colored('                                ','white') + colored('|','red') + colored('    █    █▓ ▓█  █▓ ▓█    █░   █░ ▒█  ','magenta') + colored('|','red'))
	print(colored('|','red') + colored('                                ','white') + colored('|','red') + colored('    █     ███    ███     ▒██  ▒███▒  ','magenta') + colored('|','red'))
	print(colored('|________________________________|_____________________________________|','red'))
	print(colored('| Warning:','red') + colored(" Don't break or kill script while process runing.            ",'yellow') + colored('|','red'))
	print(colored('|______________________________________________________________________|\n','red'))
	del tmp_OS
def Generate_Menu(Plugin_List):
	ret = colored('Select Once:\n\n','white')
	for Plugin in Plugin_List:
		ret += colored(str(Plugin[0]),'green') + ' ' + colored(Plugin[2],'white')
	return ret
if len(sys.argv) > 1:
	Exit_Code = 0
	if '-p' in sys.argv or '--python' in sys.argv:
		print(colored("If you want use another of python versions should run 'launcher.py -p <2_or_3>'.",'red'))
		print(colored("Not run 'main_py3.py' it's only for python version 3.",'red'))
		Exit_Code = 1
	elif '-h' in sys.argv or '--help' in sys.argv:
		print(colored('HELP PAGE:', 'white'))
		print(colored('\n	Parameters:', 'white'))
		print(colored('\n		-h ', 'green') + colored(',', 'magenta') + colored(' --help', 'green') + colored('\n		Get help page.', 'blue'))
		print(colored('\n		-m <Module_Name>', 'green') + colored(',', 'magenta') + colored(' --module <Module_Name> ', 'green') + colored('\n		Run a module without run main script.', 'blue'))
		print(colored('\n		-l ', 'green') + colored(',', 'magenta') + colored(' --list ', 'green') + colored('\n		Show list of plugins (Python 2 and 3).', 'blue'))
		print(colored('\n		-u ', 'green') + colored(',', 'magenta') + colored(' --update ', 'green') + colored('\n		Update to lastest version.', 'blue'))
		print(colored('\n		-p <Python_Version>', 'green') + colored(',', 'magenta') + colored(' --python <Python_Version>', 'green') + colored('\n		Use another version of python (2 or 3).', 'blue'))
	elif '-l' in sys.argv or '--list' in sys.argv:
		print(colored('\nList of plugins:','white'))
		List = os.listdir(Location + '/plugins')
		for name in List:
			if os.path.isfile(Location + '/plugins/' + name + '/Title.txt'):
				try:
					file = open(Location + '/plugins/' + name + '/Title.txt', 'r')
					title = file.read().replace("\n", '')
				except:
					try:
						file.close()
					except:
						pass
					continue
				file.close()
				if (not os.path.isfile(Location + '/plugins/' + name + '/main.py')) and not (os.path.isfile(Location + '/plugins/' + name + '/main3.py') and os.path.isfile(Location + '/plugins/' + name + '/main2.py')):
					if os.path.isfile(Location + '/plugins/' + name + '/main3.py'):
						print(colored('	' + FixSpase(name, 20), 'green') + colored('~~>	', 'magenta') + colored(title,'blue') + colored(' (Only for Python3)','yellow'))
					if os.path.isfile(Location + '/plugins/' + name + '/main2.py'):
						print(colored('	' + FixSpase(name, 20), 'green') + colored('~~>	', 'magenta') + colored(title,'blue') + colored(' (Only for Python2)','yellow'))
				else:
					print(colored('	' + FixSpase(name,20),'green') + colored('~~>	','magenta') + colored(title,'blue'))
		del name
		try:
			del file
		except:
			pass
	elif '-m' in sys.argv or '--module' in sys.argv:
		try:
			name = sys.argv[sys.argv.index('-m') + 1]
		except:
			print(colored('ERROR:','red'))
			print(colored('	Use like this: -m <MODULE_NAME>','yellow'))
			Exit_Code = 1
		else:
			if os.path.isfile(Location + '/plugins/' + name + '/Title.txt'):
				if os.path.isfile(Location + '/plugins/' + name + '/main3.py'):
					File = open(Location + '/plugins/' + name + '/main3.py','r')
					try:
						Data = File.read()
					except:
						try:
							subprocess.call(Location + '/plugins/' + name + '/main3.py')
						except Exception as EX:
							if str(EX)[0:28] == '[Errno 8] Exec format error:':
								print(colored("ERROR: This plugin not optimized for your CPU.", 'red'))
								print(colored("Check lastest update, May by it's Ok.", 'red'))
								Exit_Code = 1
							else:
								print(colored('Some where plugin get error! Failed job(s).', 'red'))
								print(colored('Error:', 'red'))
								print(colored(EX, 'red'))
								Exit_Code = 1
						except:
							print(colored('Some where plugin get error! Failed job(s).', 'red'))
							Exit_Code = 1
					else:
						try:
							try:
								exec(Data)
							except EndScript:
								pass
						except Exception as EX:
							print(colored('Some where plugin get error! Failed job(s).','red'))
							print(colored('Error:','red'))
							print(colored(EX,'red'))
							Exit_Code = 1
						except:
							print(colored('Some where plugin get error! Failed job(s).', 'red'))
							Exit_Code = 1
					File.close()
					del File
					try:
						del Data
					except:
						pass
				elif os.path.isfile(Location + '/plugins/' + name + '/main.py'):
					File = open(Location + '/plugins/' + name + '/main.py', 'r')
					try:
						Data = File.read()
					except:
						try:
							subprocess.call(Location + '/plugins/' + name + '/main.py')
						except Exception as EX:
							if str(EX)[0:28] == '[Errno 8] Exec format error:':
								print(colored("ERROR: This plugin not optimized for your CPU.", 'red'))
								print(colored("Check lastest update, May by it's Ok.", 'red'))
								Exit_Code = 1
							else:
								print(colored('Some where plugin get error! Failed job(s).', 'red'))
								print(colored('Error:', 'red'))
								print(colored(EX, 'red'))
								Exit_Code = 1
						except:
							print(colored('Some where plugin get error! Failed job(s).', 'red'))
							Exit_Code = 1
					else:
						try:
							try:
								exec(Data)
							except EndScript:
								pass
						except Exception as EX:
							print(colored('Some where plugin get error! Failed job(s).', 'red'))
							print(colored('Error:', 'red'))
							print(colored(EX, 'red'))
							Exit_Code = 1
						except:
							print(colored('Some where plugin get error! Failed job(s).', 'red'))
							Exit_Code = 1
					File.close()
					del File
					try:
						del Data
					except:
						pass
				elif os.path.exists(Location + '/plugins/' + name + '/main2.py'):
					print(colored('ERROR:','yellow'))
					print(colored("	This plugin programmed for Python2 and you're not using Python3.",'yellow'))
					Exit_Code = 1
				else:
					print(colored('ERROR:','red'))
					print(colored("	Plugin named as '" + name + "' exists, But not have 'main.py' or 'main3.py' file.",'red'))
					print(colored("	It may be damaged or not programmed for G3nius-Tools.",'red'))
					Exit_Code = 1
			else:
				print(colored('ERROR:','red'))
				print(colored('	Plugin with name ','yellow') + colored(name,'magenta') + colored(' not found!','yellow'))
				print(colored('	Use -l or --list to see all plugins.','yellow'))
				Exit_Code = 1
			del name
	elif '-u' in sys.argv or '--update' in sys.argv:
		File = open(Location + '/plugins/Updater/main3.py')
		try:
			try:
				exec(File.read())
			except EndScript:
				pass
		except Exception as EX:
			print(colored('Some where plugin get error! Failed job(s).', 'red'))
			print(colored('Error:', 'red'))
			print(colored(EX, 'red'))
		except:
			print(colored('Some where plugin get error! Failed job(s).', 'red'))
		File.close()
		del File
	else:
		print(colored('[-] Unknown parameter.','yellow'))
		print(colored('Use -h or --help to see all parameters.','yellow'))
		sys.exit(1)
	print(colored('\n[+] ', 'green') + colored('Done.', 'white'))
	sys.exit(Exit_Code)
try:
	List = os.listdir(Location+'/plugins')
except:
	print(colored("[!] Can't find plugins folder.",'red'))
	exit(1)
Name,Title,File,ID = None,None,None,0
for Name in List:
	ID += 1
	if not (os.path.isfile(Location + '/plugins/' + Name + '/main3.py') or os.path.isfile(Location + '/plugins/' + Name + '/main.py')):
		if os.path.isfile(Location + '/plugins/' + Name + '/main2.py'):
			print(colored('[!] Failed to load "','red') + colored(Name,'magenta') + colored('" plugin.','red'))
			print(colored("Becase it's writen for Python2 and you're using Python3.",'yellow'))
			print(colored("You can use '",'yellow') + colored('g3nius-tools -p 2','blue') + colored("' to run g3nius-tools with Python3.",'yellow'))
		else:
			print(colored('[!] Failed to load "' + Name + '" plugin.','red'))
			print(colored('Becase "main2.py" or "main3.py" or "main.py" file in script folder not exists.','red'))
		ID -= 1
		try:
			sleep(2.5)
		except:
			exit(0)
		continue
	if not os.path.isfile(Location + '/plugins/' + Name + '/Title.txt'):
		print(colored('[!] Failed to load "' + Name + '" plugin.','red'))
		print(colored('Becase "Title.txt" file in script folder not exists.','red'))
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
		print(colored('[!] Failed to load "' + Name + '" plugin.','red'))
		print(colored('Becase "Title.txt" file in script folder not have read permission.','red'))
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
			print(colored('[!] Failed to load "' + Name + '" plugin.','red'))
			print(colored('Becase "main3.py" file in script folder not have read permission.','red'))
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
			print(colored('[!] Failed to load "' + Name + '" plugin.', 'red'))
			print(colored('Becase "main.py" file in script folder not have read permission.', 'red'))
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
	print(colored('[!] ','red') + colored('No plugins were found health and available, So Exit.','yellow'))
	exit(1)
print(colored('[ *** ] G3n!us started successfully.','green'))
while True:
	Clear()
	print(Generate_Menu(Plugins) + colored(str(Menu_Numebrs + 1),'green') + colored(' Exit','white'))
	try:
		Choose = int(input(colored('\n\nEnter your number: ','blue')))
	except:
		try:
			print(colored('Invalid Choose','yellow'))
			sleep(1)
			continue
		except:
			Clear()
			if os.path.isdir(Location + '/tmp'):
				shutil.rmtree(Location + '/tmp')
			elif os.path.isfile(Location + '/tmp'):
				os.remove(Location + '/tmp')
			os.mkdir(Location + '/tmp')
			print(colored('Good by..', 'magenta'))
			exit(0)
	if Choose == Menu_Numebrs + 1:
		Clear()
		if os.path.isdir(Location + '/tmp'):
			shutil.rmtree(Location + '/tmp')
		elif os.path.isfile(Location + '/tmp'):
			os.remove(Location + '/tmp')
		os.mkdir(Location + '/tmp')
		print(colored('Good by..', 'magenta'))
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
						print(colored('Runing ' + Plugin[1] + ' failed !','red'))
						print(colored('Becase "main3.py" file in script folder not have read permission.','red'))
					else:
						Clear()
						try:
							try:
								exec(File.read())
							except EndScript:
								pass
						except Exception as EX:
							print(colored('Some where plugin get error! Failed job(s).','red'))
							print(colored('Error:','red'))
							print(colored(EX,'red'))
						except:
							print(colored('Some where plugin get error! Failed job(s).','red'))
						File.close()
						del File
				else:
					try:
						File = open(Location + '/plugins/' + Plugin[1] + '/main.py','r')
					except:
						print(colored('Runing ' + Plugin[1] + ' failed !','red'))
						print(colored('Becase "main3.py" file in script folder not have read permission.','red'))
					else:
						Clear()
						try:
							try:
								exec(File.read())
							except EndScript:
								pass
						except Exception as EX:
							print(colored('Some where plugin get error! Failed job(s).','red'))
							print(colored('Error:','red'))
							print(colored(EX,'red'))
						except:
							print(colored('Some where plugin get error! Failed job(s).','red'))
						File.close()
						del File
			else:
				Clear()
				if os.path.isfile(Location + '/plugins/' + Plugin[1] + '/main3.py'):
					try:
						subprocess.call(Location + '/plugins/' + Plugin[1] + '/main3.py')
					except Exception as EX:
						if str(EX)[0:28] == '[Errno 8] Exec format error:':
							print(colored("ERROR: This plugin not optimized for your CPU.",'red'))
							print(colored("Check lastest update, May by it's Ok.",'red'))
						else:
							print(colored('Some where plugin get error! Failed job(s).','red'))
							print(colored('Error:','red'))
							print(colored(EX,'red'))
					except:
						print(colored('Some where plugin get error! Failed job(s).','red'))
				else:
					try:
						subprocess.call(Location + '/plugins/' + Plugin[1] + '/main.py')
					except Exception as EX:
						if str(EX)[0:28] == '[Errno 8] Exec format error:':
							print(colored("ERROR: This plugin not optimized for your CPU.",'red'))
							print(colored("Check lastest update, May by it's Ok.",'red'))
						else:
							print(colored('Some where plugin get error! Failed job(s).','red'))
							print(colored('Error:','red'))
							print(colored(EX,'red'))
					except:
						print(colored('Some where plugin get error! Failed job(s).','red'))
			break
	if Find:
		try:
			Choose = input(colored('[?] ', 'yellow') + colored(' Work finished. Do you want exit from script ? [y/n] ', 'white'))
		except:
			Clear()
			if os.path.isdir(Location + '/tmp'):
				shutil.rmtree(Location + '/tmp')
			elif os.path.isfile(Location + '/tmp'):
				os.remove(Location + '/tmp')
			os.mkdir(Location + '/tmp')
			print(colored('Good by..', 'magenta'))
			exit(0)
		if str.lower(Choose) == 'y' or str.lower(Choose) == 'yes' or str.lower(Choose) == 'exit':
			Clear()
			if os.path.isdir(Location + '/tmp'):
				shutil.rmtree(Location + '/tmp')
			elif os.path.isfile(Location + '/tmp'):
				os.remove(Location + '/tmp')
			os.mkdir(Location + '/tmp')
			print(colored('Good by..', 'blue'))
			exit(0)
	else:
		print(colored('Plugin not found!','red'))
