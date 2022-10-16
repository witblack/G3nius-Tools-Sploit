#!/usr/bin/python3
# coding: utf-8
try:
	"""		starting banner		"""
except:
	from time import sleep
	print("G3nius-Tools updated successfully :D\nThanks!")
	try:
		sleep(2)
	except:
		pass
print("\x1b[6;32m[ *** ] \x1b[0m\x1b[0;38m Starting G3n!us .. \x1b[0m\n")

"""		check python 3 version		"""
from sys import version_info, exit
if version_info[0] != 3:
	print("This file is only for Python3. Don't run with Python2!")
	exit(1)

"""		external libs and termcolor		"""
try:
	# internal termcolor
	from lib.packages.termcolor import colored

	# import external libs
	from shutil import rmtree
	from subprocess import call
	from threading import Thread
	from sys import argv, exc_info
	from os.path import split, isdir, isfile
	from os import remove, mkdir, listdir, system

	# don't needed at launcher.py
	# just import to check installed or not
	from json import loads
	from requests import get
	from scapy.all import IP
	from importlib import reload
	from nmap import PortScanner
	from psutil import Process
except:
	# failed to load external
	try:
		print(colored('[!] ', 'red') + colored('Some depends not installed.', 'yellow'))
		print(colored('Run as root/administrator: "pip install -r requires.txt"', 'blue'))
	except:
		print('\x1b[0;31m[!] ERROR:    Internal "termcolor" package damaged :(\x1b[0m')
	exit(1)

# load configs
try:
	import lib.config.Exit_Codes as Exit_Codes
	import lib.config.Error_Levels as Error_Levels
	import lib.config.Main_Configs as Main_Configs
except:
	print(colored('[!] ', 'red') + colored('Failed to load configs! Invalid syntax.', 'yellow'))
	exit(1)

"""		internal libs		"""
try:
	# load core libs
	from lib.core.OS_Detector import OS
	from lib.core.Error_Handler import Handler
	from lib.core.Exit_Request import Exit_Request
	from lib.core.main.Do_On_Startup import Startup
	from lib.core.G3nius_Location import G3nius_Location
	from lib.core.main.Clean_Temp_Dir import Clean_Temp_Dir
	from lib.core.End_Plugin import End_Plugin, EndScript_Class

	# load core main libs
	from lib.core.main.Statistics import Send_Statistics
	from lib.core.main.Generate_Menu import Generate_Menu
	from lib.core.Check_Supported_OS import Check_Supported
	from lib.core.main.Plugin_Launcher import Plugin_Launcher

	# installers
	from lib.core.installers.check import Check_Installtion_G3nius
	from lib.core.installers.installer_uninstaller import Install_G3nius, Uninstall_G3nius

	# load GPL libs
	from lib.GPL.File_Workers import gpl_read_from_file
	from lib.GPL.IO import gpl_input, gpl_sleep, gpl_confirm
	from lib.GPL.Access_Managers import gpl_check_root_needed_with_error
	from lib.GPL.String_Workers import gpl_fix_spases, gpl_fix_string_to_uri
	from lib.GPL.Page_Managers import gpl_clear_and_banner, gpl_set_banner_verion, gpl_clear
except Exception as EX:
	exc_type, exc_obj, exc_tb = exc_info()
	FileName = split(exc_tb.tb_frame.f_code.co_filename)[1]
	Line_Number = exc_tb.tb_lineno
	print(colored('[!] Failed to load some local libs.', 'red'))
	print(colored("Crashed at:\t" + FileName + ' line ' + str(Line_Number), 'yellow'))
	print(colored("Exception:\t" + str(EX), 'yellow'))
	print(colored("If you sure don't change local files, report it.", 'red'))
	print(colored('Email : admin@bugzone.ir', 'blue'))
	exit(Exit_Codes.Crash)

"""		Do startup works	"""
Startup()

"""		send statisctic usage		"""
# NOTE:
# This feature is optional and just for statistics.
# You can set False to don't send reports.
thread = Thread(target=Send_Statistics, args=(Main_Configs.Statistics_Reports,))
thread.start()
del thread

"""		local varibles and detect OS		"""
Location = G3nius_Location()
Menu_Numebrs = 0
Plugins = []

"""		clean tmp folder		"""
Clean_Temp_Dir()

"""		manage CTRL+C CTRL+D	"""
try:
	"""		set version		"""
	gpl_set_banner_verion(Main_Configs.Version)

	# terms and rules
	if not isfile(Location + '/lib/agree'):
		while True:
			gpl_clear_and_banner()
			print(colored('You should agree terms and rules before using ', 'green') + colored('G3nius-Tools', 'magenta') + colored('.', 'green'))
			print(colored('\nTerm and rules:', 'white'))
			print(colored("	1. ", 'magenta') + colored("It's a semi-open source app.\n\tYou can't copy source code or use them.", 'cyan'))
			print(colored("	2. ", 'magenta') + colored("This app is only for showing weakness of security and\n\tpenetration test. You don't should damage to other people.\n\tIt's needed for a better world.", 'cyan'))
			print(colored("	3. ", 'magenta') + colored("You don't should use cracked versions or try to reverse engineering.\n\tAlso, we may be use some APIs, You don't should do any attacks on us.", 'cyan'))
			print(colored("	4. ", 'magenta') + colored("We're collecting some data from your system\n\t(like: run times count. G3nius-Tools errors etc…) to improve G3nius.\n\tThis is optional,\n\tYou can set to 'False' value in 'lib/config/Main_Configs.py' file.", 'cyan'))
			choose = gpl_input("Type 'yes' to agree terms & rules: ", clear_and_banner_before=False)
			if choose.lower() == 'yes':
				try:
					open(Location + '/lib/agree', 'w').close()
				except:
					Handler(Error_Levels.Critical, "Can't create file! check access of folder.")
				break
			else:
				Handler(Error_Levels.Failed_Job, 'Type "yes" to agree.')
				gpl_sleep(1)

	# checking if give parameters
	if len(argv) > 1:
		Delete_TMP_Folder = True
		if '-h' in argv or '--help' in argv:
			print(colored('HELP PAGE:', 'white'))
			print(colored('\n	Parameters:', 'white'))
			print(colored('\n		-h ', 'green') + colored(',', 'magenta') + colored(' --help', 'green') + colored('\n		Get help page.', 'blue'))
			print(colored('\n		-m <Module_Name>', 'green') + colored(',', 'magenta') + colored(' --module <Module_Name> ', 'green') + colored('\n		Run a module without run main script.', 'blue'))
			print(colored('\n		-l ', 'green') + colored(',', 'magenta') + colored(' --list ', 'green') + colored('\n		Show list of plugins (Python 2 and 3).', 'blue'))
			print(colored('\n		-u ', 'green') + colored(',', 'magenta') + colored(' --update ', 'green') + colored('\n		Update to lastest version.', 'blue'))
			print(colored('\n		-i ', 'green') + colored(',', 'magenta') + colored(' --install ', 'green') + colored('\n		Install on your Linux system.', 'blue'))
			print(colored('\n		-un ', 'green') + colored(',', 'magenta') + colored(' --uninstall ', 'green') + colored('\n		Uninstall on your Linux system.', 'blue'))
			print(colored('\n		-c ', 'green') + colored(',', 'magenta') + colored(' --check-install ', 'green') + colored('\n		Chcek installationon on your Linux system.', 'blue'))
		elif '-l' in argv or '--list' in argv:
			Handler(Error_Levels.NoStyle, colored('List of plugins:\n', 'white'))
			Plugins_List = listdir(Location + '/plugins')
			for Plugin_Name in Plugins_List:
				Base_Address = Location + '/plugins/' + Plugin_Name
				# read title
				if isfile(Base_Address + '/Title.txt'):
					Title = gpl_read_from_file(Base_Address + '/Title.txt').replace("\n", '')
					if not Title:
						Handler(Error_Levels.NoStyle, "\t" + gpl_fix_spases(Plugin_Name, 20) + colored('~~>     ', 'magenta') + colored("(Damaged - Can't read Title.txt)", 'red'))
					elif isfile(Base_Address + '/main.py'):
						Handler(Error_Levels.NoStyle, colored("\t" + gpl_fix_spases(Plugin_Name, 20), 'green') + colored('~~>     ', 'magenta') + colored(Title, 'blue'))
					else:
						Handler(Error_Levels.NoStyle, colored("\t" + gpl_fix_spases(Plugin_Name, 20), 'green') + colored('~~>     ', 'magenta') + colored(Title, 'blue') + colored('Damaged - main.py not exists.', 'red'))
				else:
					Handler(Error_Levels.NoStyle, "\t" + gpl_fix_spases(Plugin_Name, 20) + colored('~~>     ', 'magenta') + colored("(Damaged - Title.txt file not exists)", 'red'))
			del Plugin_Name, Plugins_List
		elif '-m' in argv or '--module' in argv:
			try:
				Plugin_Name = argv[argv.index('-m') + 1]
			except:
				Handler(Error_Levels.High, 'Invalid Syntax. Use like this: -m <MODULE_NAME>')
				Exit_Request(Exit_Codes.InvalidArgument, clear_and_banner=False)
			else:
				# detect plugin
				Base_Address = Location + '/plugins/' + Plugin_Name
				if not isdir(Base_Address):
					Handler(Error_Levels.Critical, 'Plugin "' + Plugin_Name + "\" not exists!", 'Use -l or --list to see list of plugins with info.', False)
				if isfile(Base_Address + '/Title.txt'):
					Title = gpl_read_from_file(Base_Address + '/Title.txt')
					if Title:
						if isfile(Base_Address + '/main.py'):
							File_Address = Base_Address + '/main.py'
						else:
							Handler(Error_Levels.Critical, "main.py plugin file not exists!", Clear_Page=False)
						Soucrce_Code = gpl_read_from_file(File_Address)
						if Soucrce_Code:
							if Soucrce_Code[:len(Main_Configs.Include_G3nius_Libs_At_Plugin_Start_With)] == Main_Configs.Include_G3nius_Libs_At_Plugin_Start_With:
								Import_G3nius = True
							else:
								Import_G3nius = False
							Plugin_Launcher({'ID': 0, 'Name': Plugin_Name, 'Title': Title, 'File_Address': File_Address, 'Import_G3nius': Import_G3nius})
						else:
							Handler(Error_Levels.Critical, "Can't read 'Title.txt' of '" + Plugin_Name + "' plugin!", 'Add read access to file.' ,False)
					else:
						Handler(Error_Levels.Critical, "Can't read 'Title.txt' of '" + Plugin_Name + "' plugin!", 'Add read access to file.' ,False)
		elif '-u' in argv or '--update' in argv:
			File_Address = Location + '/plugins/Updater/main.py'
			# check plugin exists
			if not isfile(File_Address):
				Handler(Error_Levels.High, "Updater plugin not found!")
				Exit_Request(Exit_Codes.CommandNotFound, clear_and_banner=False)
			# run
			File = open(File_Address)
			try:
				try:
					exec(File.read())
				except EndScript_Class:
					pass
			except Exception as EX:
				Handler(Error_Levels.Critical, "Can't update, plugin crashed!", str(EX), Clear_Page=False)
			except:
				Handler(Error_Levels.Critical, "Can't update, plugin crashed!", Clear_Page=False)
			File.close()
			del File, File_Address
		elif '-c' in argv or '--check' in argv or '-i' in argv or '--install' in argv or '-un' in argv or '--uninstall' in argv:
			# check access & dont clean tmp
			Delete_TMP_Folder = False
			if not Check_Supported(Linux=True):
				Handler(Error_Levels.Critical, "Only Linux users can install G3nius-Tools.", "It's not problem, Run on your system and use G3nius-Tools.")
			gpl_check_root_needed_with_error(exit_code=Exit_Codes.CanNotExecute)
			if '-i' in argv or '--install' in argv:
				# install
				Install_G3nius()
			elif '-un' in argv or '--uninstall' in argv:
				# uninstall
				Uninstall_G3nius()
			else:
				# check installation
				Check_Installtion_G3nius()
		else:
			Handler(Error_Levels.High, 'Unknown parameter.', 'Use -h or --help to see all parameters.')
			Exit_Request(Exit_Codes.InvalidArgument, clear_and_banner=False)
		Exit_Request(Exit_Codes.Normal, clear_and_banner=False, clear_tmp_folder=Delete_TMP_Folder)

	"""		get list of plugins		"""
	# check directory exists
	if not isdir(Location + '/plugins'):
		if isfile(Location + '/plugins'):
			Handler(Error_Levels.Critical, "plugins folder not exists. File replaced with.")
		else:
			mkdir(Location + '/plugins')
	# list of plugins
	try:
		List = listdir(Location + '/plugins')
	except:
		Handler(Error_Levels.Critical, "Can't access to plugins folder.")

	"""		check plugins		"""
	# sort by directory name
	List.sort()
	# checking
	ID = 0
	for Name in List:
		Base_Address = Location + '/plugins/' + Name
		# check "Title.txt" file exists
		if not isfile(Base_Address + '/Title.txt'):
			Handler(Error_Levels.Failed_Job, 'Plugin "' + Name + "\" can't load.", '"Title.txt" file in script folder not exists.')
			gpl_sleep(Main_Configs.Sleep_When_Plugin_Failed_Load)
			continue
		# check main.py exists
		if isfile(Base_Address + '/main.py'):
			File_Address = Base_Address + '/main.py'
		else:
			# plugin damaged
			Handler(Error_Levels.Failed_Job, 'Plugin "' + Name + "\" can't load.", '"main.py" file in script folder not exists.')
			gpl_sleep(Main_Configs.Sleep_When_Plugin_Failed_Load)
			continue
		# read title
		Title = gpl_read_from_file(Base_Address + '/Title.txt', on_access_failed_text="Plugin '" + Name + "' can't load.", on_access_failed_description_text='Because "Title.txt" file in script folder not have read permission.')
		if not Title:
			gpl_sleep(Main_Configs.Sleep_When_Plugin_Failed_Load)
			continue
		Title = Title.replace("\n", '')
		# check # import G3nius-Tools
		Source_Code = gpl_read_from_file(File_Address, on_access_failed_text='Plugin "' + Name + '" Can\'t load.', on_access_failed_description_text='Because "main.py" file in script folder not have read permission.', encoding="ISO-8859-1")
		if Source_Code != None:
			if Source_Code[:len(Main_Configs.Include_G3nius_Libs_At_Plugin_Start_With)] == Main_Configs.Include_G3nius_Libs_At_Plugin_Start_With:
				Import_G3nius = True
			else:
				Import_G3nius = False
		else:
			gpl_sleep(Main_Configs.Sleep_When_Plugin_Failed_Load)
			continue
		ID += 1
		# Stractrue:
		# [ {'ID': 1, 'Name': 'ddos', 'Title': 'do ddos', ,'File_Address': '/path/to/main.py', 'Import_G3nius': False} , ... ]
		Plugins.append({'ID': ID, 'Name': Name, 'Title': Title, 'File_Address': File_Address, 'Import_G3nius': Import_G3nius})
		del Name, Title, Source_Code, Base_Address, File_Address, Import_G3nius
	Menu_Numebrs = ID
	del ID

	# checking if empty plugins
	if len(Plugins) == 0:
		Handler(Error_Levels.High, 'No plugins were found health and available, So exit.')
		Exit_Request(Exit_Codes.Normal)

	# main
	print(colored('[ *** ] G3n!us started successfully.', 'green'))
	while True:
		gpl_set_banner_verion(Main_Configs.Version)
		gpl_clear_and_banner()
		Menu_String = Generate_Menu(Plugins, Menu_Numebrs)
		print(Menu_String)
		Choose = gpl_input(colored('\n\n-={', 'cyan') + colored('Enter number ', 'green') + colored('~', 'red') + colored('>> ', 'magenta'), dont_style=True, get_int=True, on_invalid_sleep_by_sec=Main_Configs.Sleep_When_Invalid_Plugin_Number, clear_and_banner_before=False, on_invalid_after_clear_text=Menu_String)
		if Choose > Menu_Numebrs + 1 or Choose < 1:
			Handler(Error_Levels.High, 'Invalid number!')
			gpl_sleep(Main_Configs.Sleep_When_Invalid_Plugin_Number)
			continue
		if Choose == Menu_Numebrs + 1:
			Exit_Request(Exit_Codes.Normal)
		"""		run plugin		"""
		gpl_clear()
		Plugin_Launcher(Plugins[Choose - 1])
		"""		end work plugin		"""
		Choose = gpl_confirm('Work finished. Do you want exit from G3nius-Tools', clear_and_banner_before=False, default_return_value=False)
		if Choose:
			Exit_Request(Exit_Codes.Normal)
except (KeyboardInterrupt, EOFError):
	Exit_Request(Exit_Codes.CTRL_C, text_after_clear=colored('Exit with user request.', 'yellow'))
except Exception as EX:
	exc_type, exc_obj, exc_tb = exc_info()
	FileName = split(exc_tb.tb_frame.f_code.co_filename)[1]
	Line_Number = exc_tb.tb_lineno
	Handler(Error_Levels.Failed_Job, "Crashed at:\t" + FileName + ' line ' + str(Line_Number))
	Handler(Error_Levels.Failed_Job, "Exception:\t" + str(EX))
	Handler(Error_Levels.High, "If you sure don't change local files, report it.")
	Handler(Error_Levels.Critical, 'Email : admin@bugzone.ir', Clear_Page=False)