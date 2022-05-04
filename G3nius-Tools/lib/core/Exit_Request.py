"""		libs		"""
# external
from sys import exit

# internal
from lib.packages.termcolor import colored
from lib.GPL.Page_Managers import gpl_clear_and_banner
from lib.core.main.Clean_Temp_Dir import Clean_Temp_Dir

"""		exit request		"""
def Exit_Request(Error_Code, clear_and_banner=True, text_after_clear=None):
	if clear_and_banner:
		gpl_clear_and_banner()
	if text_after_clear:
		print(text_after_clear)
	# clean tmp folder
	Clean_Temp_Dir()
	print(colored('Good by..', 'magenta'))
	exit(Error_Code)