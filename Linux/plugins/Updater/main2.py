#!/usr/bin/python3
# coding: utf-8
try:
	import requests
	import os
	import shutil
	import zipfile
	from termcolor import colored
except:
	print('[!] Failed to update. Some Deepends not installed.')
	print("[+] Run 'pip install os requests shutil zipfile termcolor' to install.")
	End()
URL = 'https://bugzone.ir/Server/G3nius/'
Clear()
print(colored('[+] Checking update...','green'))
try:
	Last_version = str(requests.get(URL + 'Version.Version').content).replace('\n','')
	Size = str(requests.get(URL + 'SizeFile.php').content).replace('\n','')
except:
	print(colored('[!] ','red') + colored('Failed to connect the server. Check your internet Connection.','yellow'))
	End()
if int(Size) / 1048576 > 1:
	Size = str(round(int(Size) / 1048576,2)) + ' MB'
elif int(Size) / 1024 > 1:
	Size = str(round(int(Size) / 1024,2)) + ' KB'
else:
	Size = Size + ' Byte'
if Version == Last_version:
	print(colored("[+] You're now using last version.",'green'))
	del Last_version,Size,URL
	End()
else:
	del Last_version
Clear()
Choose = None
while True:
	Choose = raw_input(colored('[?] ','yellow') + colored('Need to download ' + Size + ', Confirm and update [y/n] ?  ','white'))
	if str.lower(Choose) == 'y' or str.lower(Choose) == 'yes':
		print(colored('[+] Downloading update...','green'))
		try:
			Content = requests.get(URL + 'Lastest.zip').content
		except:
			print(colored('[!] Error: Your internet connection lost! Check your internet.','red'))
		File = open(Location + '/tmp/UPDATE.zip','wb')
		File.write(Content)
		File.close()
		print(colored('[+] Extracting update file...','green'))
		File = zipfile.ZipFile(Location + '/tmp/UPDATE.zip', 'r')
		File.extractall(Location + '/tmp/TMP_UPDATE')
		print(colored('[+] Checking installed plugins...','green'))
		shutil.move(Location + '/tmp/TMP_UPDATE/plugins',Location + '/tmp/')
		print(colored('[+] Updating core...','green'))
		for object in os.listdir(Location + '/tmp/TMP_UPDATE/'):
			if os.path.isdir(Location + '/' + object) and object != 'tmp':
				shutil.rmtree(Location + '/' + object)
			elif os.path.isfile(Location + '/' + object):
				os.remove(Location + '/' + object)
			shutil.move(Location + '/tmp/TMP_UPDATE/' + object, Location + '/' + object)
		print(colored('[+] Updating supported plugins...','green'))
		ListPlugins = os.listdir(Location + '/tmp/plugins')
		for plugin in ListPlugins:
			if os.path.isdir(Location + '/plugins/' + plugin):
				shutil.rmtree(Location + '/plugins/' + plugin)
			elif os.path.isfile(Location + '/plugins/' + plugin):
				os.rename(Location + '/plugins/' + plugin,Location + '/plugins/' + plugin + '~')
			shutil.move(Location + '/tmp/plugins/' + plugin, Location + '/plugins/' + plugin)
		print(colored('Plugins updated: ','white') + colored(ListPlugins,'green'))
		print(colored('[+] Repair access files...','green'))
		for root, dirs, files in os.walk(Location):
			for file in files:
				if file.endswith(".py"):
					os.chmod(os.path.join(root, file),0771)
		print(colored('[+] Updating finished, Restart for use lastest version.','green'))
		break
	elif str.lower(Choose) == 'n' or str.lower(Choose) == 'no':
		print(colored('[+] Update cancelled by user request.','yellow'))
		del Size,Choose,URL
		End()
	else:
		print(colored('[!] Invalid Choose.','yellow'))
del Size,Choose,Content,URL,object,root,files,dirs,file,plugin,ListPlugins
shutil.rmtree(Location + '/tmp')
os.mkdir(Location + '/tmp')
