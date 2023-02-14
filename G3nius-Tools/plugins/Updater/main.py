# import G3nius-Tools
# coding: utf-8

"""		external libs		"""
from os.path import join, isdir, isfile
from shutil import move, rmtree
from os import popen, chmod, remove, rename, listdir, walk

"""		internal libs		"""
# config
import lib.config.Error_Levels as Error_Levels
from lib.config.Main_Configs import Version
# core
from lib.core.End_Plugin import End_Plugin
from lib.core.Error_Handler import Handler
from lib.core.G3nius_Location import G3nius_Location
from lib.core.main.Restart_G3nius import Restart_G3nius
from lib.core.Check_Supported_OS import Check_Supported
# GPL
from lib.GPL.HTTP_Managers import gpl_http_get
from lib.GPL.IO import gpl_confirm
from lib.GPL.Page_Managers import gpl_clear_and_banner, gpl_set_banner_verion
from lib.GPL.File_Workers import gpl_write_to_file
from lib.GPL.String_Workers import gpl_fix_string_to_uri

"""		check supporting OS		"""
if not Check_Supported(Linux=True):
	Handler(Error_Levels.Failed_Job, "Only Linux users can use online Updater plugin!", "Download and reinstall new version of G3nius-Tools.")


"""		local varibles		"""
URL = 'https://api.BugZone.ir/G3nius/'
Plugin_Version = '2.0.7'
Location = G3nius_Location()

# collect data from server
gpl_set_banner_verion(Plugin_Version)
del Plugin_Version
gpl_clear_and_banner()
Handler(Error_Levels.Info, "Checking update...")

Busy_Server_Text = 'Update server is very busy. auto retry.. (If take many times, Use CTRL+C and retry later)'
Last_version = gpl_http_get(URL + 'Version.Version', ok_http_codes=[200], on_invalid_http_code_retry_text=Busy_Server_Text)
Size = gpl_http_get(URL + 'SizeFile.php', ok_http_codes=[200], on_invalid_http_code_retry_text=Busy_Server_Text)
del Busy_Server_Text

# check valid
if Size == None or Last_version == None:
	Handler(Error_Levels.Failed_Job, 'Failed to connect server. Check your internet Connection.')
	End_Plugin()
else:
	# fix spase/encoding/etc..
	Last_version = Last_version.content.decode('utf-8').replace("\n", '')
	Size = Size.content.decode('utf-8').replace("\n", '')
	# check server closed
	if Size == '!502!':
		Handler(Error_Levels.Alert, "We're now working on server. New updates coming soon!", "Try again 10 min later.")
		End_Plugin()

	# calculate download size
	if int(Size) / 1024 / 1024 >= 1:
		Size = str(round(int(Size) / 1024 / 1024, 2)) + ' MB'
	elif int(Size) / 1024 >= 1:
		Size = str(round(int(Size) / 1024, 2)) + ' KB'
	else:
		Size = Size + ' Byte'

	# checking update avalible
	if Version == Last_version:
		Handler(Error_Levels.Alert, "You're now using last version.")
		del Last_version, Size, URL
		End_Plugin()
	else:
		del Last_version

	# ask from user
	Choose = None
	while True:
		Choose = gpl_confirm('Need to download ' + Size + ', Confirm and update')
		# yes, goes update
		if Choose:
			# download update and write on file
			Handler(Error_Levels.Alert, 'Downloading update...')
			Content = gpl_http_get(URL + 'Lastest.zip', ok_http_codes=[200]).content
			if Content == None:
				Handler(Error_Levels.High, 'Error: Your internet connection lost! Check your internet.')
				End_Plugin()

			# write to file
			Result = gpl_write_to_file(Location + '/tmp/UPDATE.zip', Content)
			if Result == False or Result == None:
				End_Plugin()

			# extracting downloaded zip
			Handler(Error_Levels.Alert, 'Extracting update file...')
			if 'UnZip' in popen('unzip -v').read():
				popen('unzip ' + gpl_fix_string_to_uri(Location) + '/tmp/UPDATE.zip -d ' + gpl_fix_string_to_uri(Location) + '/tmp/TMP_UPDATE').read()
			else:
				Handler(Error_Levels.High, '"unzip" command not installed.', 'Run: 		apt install unzip')
				End_Plugin()
			# check extract ok
			if not isdir(Location + '/tmp/TMP_UPDATE'):
				Handler(Error_Levels.High, "Can't extract zip file!")
				End_Plugin()
			remove(Location + '/tmp/UPDATE.zip')

			# split plugins
			Handler(Error_Levels.Alert, 'Checking installed plugins...')
			move(Location + '/tmp/TMP_UPDATE/plugins', Location + '/tmp/')

			# updating core
			Handler(Error_Levels.Alert, 'Updating core...')
			for Item in listdir(Location + '/tmp/TMP_UPDATE/'):
				if isdir(Location + '/' + Item) and Item != 'tmp':
					rmtree(Location + '/' + Item)
				elif isfile(Location + '/' + Item):
					remove(Location + '/' + Item)
				move(Location + '/tmp/TMP_UPDATE/' + Item, Location + '/' + Item)

			# updating plugins
			Handler(Error_Levels.Alert, 'Updating supported plugins...')
			ListPlugins = listdir(Location + '/tmp/plugins')
			for plugin in ListPlugins:
				if isdir(Location + '/plugins/' + plugin):
					rmtree(Location + '/plugins/' + plugin)
				elif isfile(Location + '/plugins/' + plugin):
					# rename file if same plugin name
					rename(Location + '/plugins/' + plugin, Location + '/plugins/' + plugin + '~')
				move(Location + '/tmp/plugins/' + plugin, Location + '/plugins/' + plugin)
				Handler(Error_Levels.Alert, "Plugin '" + plugin + "' Updated.")

			# change access
			Handler(Error_Levels.Alert, 'Repair access files...')
			for root, dirs, files in walk(Location):
				for file in files:
					if file.endswith(".py") or file.endswith(".pl") or file.endswith(".js") or file.endswith(".sh"):
						chmod(join(root, file), 0o771)

			# get ready for exit
			Handler(Error_Levels.Alert, 'Updating finished, Restarting G3nius-Tools...')
			Restart_G3nius()

		# no, don't update
		else:
			# cancel update
			Handler(Error_Levels.Failed_Job, 'Update cancelled by user request.')
			del Size, Choose, URL
			End_Plugin()

	# go back to normally
	del Size, Choose, Content, URL, Item, root, files, dirs, file, plugin, ListPlugins