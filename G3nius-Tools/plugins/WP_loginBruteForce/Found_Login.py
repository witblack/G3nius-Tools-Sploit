"""     libs    """
from lib.classes.gpl import gpl_write_to_file


"""     Save login      """
def Found_Login(Filename, URL, Username, Password):
    Data = f"\n\nLogin Found:\n\tURL:\t{URL}\n\tUsername:\t{Username}\n\tPassword:\t{Password}"
    gpl_write_to_file(Filename, Data, append=True)
