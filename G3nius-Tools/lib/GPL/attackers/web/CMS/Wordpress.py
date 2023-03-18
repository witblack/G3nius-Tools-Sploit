"""     libs    """
from lib.GPL.HTTP_Managers import gpl_http_get

# configs
from lib.config.GPL import Wordpress_Theme_Path


"""     GPL     """
# connect to SSH server
#
# internal:
# gpl_http_get
#
# version
# 1
def gpl_wordpress_exists(URL):
    Request = gpl_http_get(URL)
    if Request.status_code == 200 and Wordpress_Theme_Path in Request.text:
        return True
    else:
        return False
