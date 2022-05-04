# import libs
from os import name
from time import sleep
from lib.packages.termcolor import colored
from lib.config.Main_Configs import Sleep_On_Unknown_OS


"""		detect os		"""
# can be once : ['Linux','Windows','Unknown']
if str.lower(name) == 'nt':
	OS = 'Windows'
elif str.lower(name) == 'posix':
	OS = 'Linux'
else:
	OS = 'Unknown'
	print(colored('[!] ', 'red') + colored('Your os not support, Sometimes it may be not working. Continue after ' + str(Sleep_On_Unknown_OS) + ' S..'))
	sleep(Sleep_On_Unknown_OS)