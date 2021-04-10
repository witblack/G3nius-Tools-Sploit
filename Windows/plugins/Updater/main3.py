#!/usr/bin/python3
# coding: utf-8
try:
	import requests
	import os
	import shutil
	import zipfile
	from sys import exit
	from colorama import Fore,Back,init
except:
	print('[!] Failed to update. Some Deepends not installed.')
	print("[+] Run 'pip install os requests shutil zipfile colorama' to install.")
	End()
init()
URL = 'https://bugzone.ir/Server/G3nius/Windows/'
Clear()
print(Fore.GREEN + '[+] Checking update...')
try:
	Last_version = requests.get(URL + 'Version.Version').content.decode('utf-8').replace("\n",'')
	Size = requests.get(URL + 'SizeFile.php').content.decode('utf-8').replace("\n",'')
except:
	print(Fore.YELLOW + '[!] Failed to connect the server. Check your internet Connection.')
	End()
if Size == '!502!':
	print(Fore.YELLOW + "We're now working on server. New updates coming soon!")
	print(Fore.YELLOW + "Try again 10 min later.")
	End()
if int(Size) / 1024 / 1024 >= 1:
	Size = str(round(int(Size) / 1024 / 1024,2)) + ' MB'
elif int(Size) / 1024 >= 1:
	Size = str(round(int(Size) / 1024,2)) + ' KB'
else:
	Size = Size + ' Byte'
if Version == Last_version:
	print(Fore.GREEN + "[+] You're now using last version.")
	del Last_version,Size,URL
	End()
else:
	del Last_version
Clear()
Choose = None
while True:
	Choose = input(Fore.YELLOW + '[?] ' + Fore.WHITE + 'Need to download ' + Size + ', Confirm and update [y/n] ? ')
	if str.lower(Choose) == 'y' or str.lower(Choose) == 'yes':
		print(Fore.GREEN + '[+] Downloading update...')
		try:
			Content = requests.get(URL + 'Lastest.zip').content
		except:
			print(Fore.RED + '[!] Error: Your internet connection lost! Check your internet.')
		File = open(Location + '/tmp/UPDATE.zip','wb')
		File.write(Content)
		File.close()
		print(Fore.GREEN + '[+] Extracting update file...')
		File = zipfile.ZipFile(Location + '/tmp/UPDATE.zip', 'r')
		File.extractall(Location + '/tmp/TMP_UPDATE')
		print(Fore.GREEN + '[+] Checking installed plugins...')
		shutil.move(Location + '/tmp/TMP_UPDATE/plugins',Location + '/tmp/')
		print(Fore.GREEN + '[+] Updating core...')
		for object in os.listdir(Location + '/tmp/TMP_UPDATE/'):
			if os.path.isdir(Location + '/' + object) and object != 'tmp':
				shutil.rmtree(Location + '/' + object)
			elif os.path.isfile(Location + '/' + object):
				os.remove(Location + '/' + object)
			shutil.move(Location + '/tmp/TMP_UPDATE/' + object, Location + '/' + object)
		print(Fore.GREEN + '[+] Updating supported plugins...')
		ListPlugins = os.listdir(Location + '/tmp/plugins')
		for plugin in ListPlugins:
			if os.path.isdir(Location + '/plugins/' + plugin):
				shutil.rmtree(Location + '/plugins/' + plugin)
			elif os.path.isfile(Location + '/plugins/' + plugin):
				os.rename(Location + '/plugins/' + plugin,Location + '/plugins/' + plugin + '~')
			shutil.move(Location + '/tmp/plugins/' + plugin, Location + '/plugins/' + plugin)
		print(Fore.WHITE + 'Plugins updated: ' + Fore.GREEN + ListPlugins)
		print(Fore.GREEN + '[+] Repair access files...')
		for root, dirs, files in os.walk(Location):
			for file in files:
				if file.endswith(".py"):
					os.chmod(os.path.join(root, file),0o771)
		print(Fore.GREEN + '[+] Updating finished, Restarting for use lastest version. Run again.')
		break
	elif str.lower(Choose) == 'n' or str.lower(Choose) == 'no':
		print(Fore.YELLOW + '[+] Update cancelled by user request.')
		del Size,Choose,URL
		End()
	else:
		print(Fore.YELLOW + '[!] Invalid Choose.')
del Size,Choose,Content,URL,object,root,files,dirs,file,plugin,ListPlugins
shutil.rmtree(Location + '/tmp')
os.mkdir(Location + '/tmp')
exit(0)
