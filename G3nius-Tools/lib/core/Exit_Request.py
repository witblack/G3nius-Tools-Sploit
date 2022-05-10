"""		libs		"""
# external
from sys import exit

# internal
from lib.packages.termcolor import colored
from lib.GPL.Page_Managers import gpl_clear_and_banner
from lib.core.main.Clean_Temp_Dir import Clean_Temp_Dir

"""		exit request		"""
def Exit_Request(Error_Code, clear_and_banner=True, text_after_clear=None, clear_tmp_folder=True):
	if clear_and_banner:
		gpl_clear_and_banner()
	if text_after_clear:
		print(text_after_clear)
	# clean tmp folder
	if clear_tmp_folder:
		Clean_Temp_Dir(False)
	print(colored('Good by..', 'magenta'))
	exit(Error_Code)