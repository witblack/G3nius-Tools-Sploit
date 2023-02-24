"""     libs    """
# Internal
from lib.GPL.File_Workers import gpl_write_to_file
from lib.GPL.attackers.cryptography.base_x import gpl_base64_decode
from lib.GPL.String_Workers import gpl_fix_string_to_uri
from lib.GPL.Command_Managers import gpl_run_OS_command

# External
from adbutils import adb
from os.path import isfile


"""     FACADE     """
from lib.config.ADB_Keycodes import key_codes


"""     GPL     """
# not work or wrote
#
# dumpsys
# forward
# remove password
# show mac
# dump_meminfo
# send sms
# delete sms
# list-forwards
# wpa_supplicant
# logs
# swipe
# battery returns str not dicts
# netstat returns str not dicts
# dump_hierarchy


"""     GPL     """
# Get connected & accepted devices
#
# modules:
# from adbutils import adb
#
# Note:
# Will be return list() of accepted devices
#
# version:
# 1
def gpl_adb_connected_devices():
    return adb.device_list()



# Information about device
#
# version:
# 1
def gpl_adb_device_information(device):
    Information = {
        "Serial": device.serial,
        "Model": device.prop.model,
        "Name": device.prop.name,
        "Device": device.prop.device,
        "Widow_Size": device.window_size(),
        "Rotation": device.rotation(),
        "IP": gpl_adb_wlan_IP(device),
        "Path": device.get_devpath()
    }
    return Information



# Show wlan IP
#
# version:
# 1
def gpl_adb_wlan_IP(device):
    try:
        IP = device.wlan_ip()
    except Exception as ex:
        print(ex)
        return None
    else:
        return IP



# Connect adb to remove device
#
# modules:
# from adbutils import adb
#
# version:
# 1
def gpl_adb_connect_to_IP(IP, port=None):
    try:
        if port:
            adb.connect(IP + ':' + str(port))
        else:
            adb.connect(IP)
    except:
        return False
    else:
        for Device in gpl_adb_connected_devices():
            if Device.serial == IP or Device.serial == IP + ':' + str(port):
                return True
        else:
            return False



# Disconnect adb from remove device
#
# modules:
# from adbutils import adb
#
# version:
# 1
def gpl_adb_disconnect_IP(IP, port=None):
    if port:
        adb.disconnect(IP + ':' + str(port))
    else:
        adb.disconnect(IP)



# Enable/disable Wi-Fi
#
# modules:
# gpl_adb_shell
#
# version:
# 1
def gpl_adb_wifi(device, on=True):
    if on:
        gpl_adb_shell(device, 'svc wifi enable')
    else:
        gpl_adb_shell(device, 'svc wifi disable')




# Get list of installed apps
#
# version:
# 1
def gpl_adb_list_apps(device):
    return device.list_packages()




# Check device rooted or not
#
# modules:
# gpl_adb_shell
#
# version:
# 1
def gpl_adb_is_rooted(device):
    challenge = gpl_adb_shell(device, 'su --help 2> /dev/null | echo "failed"')
    if challenge == 'failed':
        return False
    else:
        return True



# Run os command on device
#
# version:
# 1
def gpl_adb_shell(device, command: str):
    return device.shell(command)



# Install an apk
#
# Note:
# URI is location of APK on your computer (ADB Server)
#
# version:
# 1
def gpl_adb_install_apk(device, URI: str, launch_after_install=False, uninstall_first=False, show_logs=False):
    if isfile(URI):
        try:
            device.install(URI, nolaunch=launch_after_install, uninstall=uninstall_first, silent=(not show_logs))
            return True
        except:
            return False
    else:
        raise Exception('APK file not found!')



# Install an apk from URL
#
# version:
# 1
def gpl_adb_install_URL_APK(device, URL: str, launch_after_install=False, uninstall_first=False, show_logs=False):
    if URL.lower().startswith('http://') or URL.lower().startswith('https://'):
        try:
            device.install(URL, nolaunch=launch_after_install, uninstall=uninstall_first, silent=(not show_logs))
            return True
        except:
            return False
    else:
        raise Exception('Enter a URL!')



# Uninstall app
#
# modules:
# from adbutils import adb
#
# version:
# 1
def gpl_adb_uninstall_app(device, package_name: str):
    if package_name in gpl_adb_list_apps(device):
        Result = device.uninstall(package_name)
        if Result == 'Success':
            return True
        else:
            return False
    else:
        return None



# Open app
#
# version:
# 1
def gpl_adb_open_app(device, package_name: str, activity=None):
    if activity:
        device.app_start(package_name, activity)
    else:
        device.app_start(package_name)



# Close app
#
# version:
# 1
def gpl_adb_close_app(device, package_name: str):
    device.app_stop(package_name)



# Clear data of app
#
# version:
# 1
def gpl_adb_clear_data_app(device, package_name: str):
    device.app_clear(package_name)




# Get information of app
#
# Return simple:
# {
# 	'package_name': 'com.package.name',
# 	'version_name': 'x.x.xx',
# 	'version_code': 'xxxxx',
# 	'flags': ['HAS_CODE','ALLOW_CLEAR_USER_DATA','ALLOW_BACKUP'],
# 	'first_install_time': datetime.datetime(2022, 11, 29, 12, 16, 54),
# 	'last_update_time': datetime.datetime(2023, 2, 16, 14, 41, 18),
# 	'signature': 'xxxxxxxx], past signatures:['
# }
#
# version:
# 1
def gpl_adb_app_info(device, package_name):
    return device.package_info(package_name)



# shutdown device
#
# modules:
# gpl_adb_shell
#
# version:
# 1
def gpl_adb_shutdown(device):
    gpl_adb_shell(device, 'reboot -p')



# shutdown device
#
# modules:
# gpl_adb_shell
#
# version:
# 1
def gpl_adb_reboot(device):
    gpl_adb_shell(device, 'reboot')



# Turn off ADB server
#
# modules:
# from adbutils import adb
#
# version:
# 1
def gpl_adb_kill_server():
    adb.server_kill()



# Transfer file from G3nius to client
#
# version:
# 1
def gpl_adb_transfer_from_client(device, path: str, destination: str):
    device.sync.pull(path, destination)



# Transfer file from client to G3nius
#
# version:
# 1
def gpl_adb_transfer_to_client(device, path: str, destination: str):
    device.sync.push(path, destination)



# Get list of files and directory
#
# version:
# 1
def gpl_adb_list_files_folders(device, path: str):
    return device.sync.list(path)



# On/Off airplane mode
#
# version:
# 1
def gpl_adb_airplane_mode(device, Enable=False):
    device.switch_airplane(Enable)



# Get battery information
#
# modules:
# gpl_adb_shell
#
# version:
# 1
def gpl_adb_battery(device):
    return gpl_adb_shell(device, 'dumpsys battery')



# Netstat - Status of network
#
# modules:
# gpl_adb_shell
#
# version:
# 1
def gpl_adb_netstat(device):
    return gpl_adb_shell(device, 'netstat')



# Change audio volume
#
# modules:
# gpl_adb_run_keycode
#
# version:
# 1
def gpl_adb_volume(device, value, volume_up=True):
    for _ in range(0, value):
        if volume_up:
            gpl_adb_run_keycode(device, key_codes.VOLUME_UP)
        else:
            gpl_adb_run_keycode(device, key_codes.VOLUME_DOWN)



# Check status of screen
#
# version:
# 1
def gpl_adb_is_screen_on(device):
    return device.is_screen_on()



# Mute/Unmute volume
#
# modules:
# gpl_adb_run_keycode
#
# version:
# 1
def gpl_adb_volume_mute_unmute(device):
    gpl_adb_run_keycode(device, key_codes.VOLUME_MUTE)



# Run keycode in device
#
# version:
# 1
def gpl_adb_run_keycode(device, key_code):
    device.keyevent(key_code)



# Open URL in browser
#
# version:
# 1
def gpl_adb_open_browser(device, URL: str):
    device.open_browser(URL)



# Change screen status
#
# version:
# 1
def gpl_adb_change_screen_status(device, status=True):
    device.switch_screen(status)



# Lock screen
#
# modules:
# gpl_adb_run_keycode
#
# version:
# 1
def gpl_adb_lock_screen(device):
    if gpl_adb_is_screen_on(device):
        gpl_adb_run_keycode(device, key_codes.POWER)



# Take screenshot
#
# modules:
# gpl_base64_decode
# gpl_write_to_file
# gpl_adb_shell
#
# version:
# 1
def gpl_adb_screenshot(device, destination_png):
    content = gpl_adb_shell(device, 'screencap -p | base64')
    content = gpl_base64_decode(content)
    gpl_write_to_file(destination_png, content)



# Get list of running process
#
# Return simple:
# [[UID             PID   PPID C STIME TTY          TIME CMD], ...]
#
# modules:
# gpl_adb_shell
#
# version:
# 1
def gpl_adb_list_processes(device):
    return gpl_adb_shell(device, 'ps -ef').split("\n")[1:]



# Extract list of contacts
#
# modules:
# gpl_adb_shell
#
# version:
# 1
def gpl_adb_extract_contacts(device, return_list=False):
    Contacts = gpl_adb_shell(device, 'content query --uri content://contacts/phones/  --projection display_name:number:notes')
    # Fix on new Android versions
    if Contacts == 'No result found.':
        Contacts = gpl_adb_shell(device, 'content query --uri content://com.android.contacts/data --projection display_name:data1:data4:contact_id')
    # Convert to list of option checked
    if return_list:
        Contacts = "\n" + Contacts
        Contacts = Contacts.split("\nRow: ")
        for ID in range(0, len(Contacts)):
            Contacts[ID] = Contacts[ID].split(', ')
        Contacts.pop(0)
    # return final result
    return Contacts



# Extract list of SMS(s)
#
# modules:
# gpl_adb_shell
#
# version:
# 1
def gpl_adb_extract_SMS(device, return_list=False):
    SMSs = gpl_adb_shell(device, 'content query --uri content://sms/ --projection _id:address:date:body')
    if return_list:
        SMSs = "\n" + SMSs
        # Convert to list of option checked
        SMSs = SMSs.split("\nRow: ")
        for ID in range(0, len(SMSs)):
            SMSs[ID] = SMSs[ID].split(', ')
        SMSs.pop(0)
    return SMSs



# Type a text
#
# modules:
# gpl_fix_string_to_uri
# gpl_adb_shell
#
# version:
# 1
def gpl_adb_keyboard_type(device, text):
    text = gpl_fix_string_to_uri(text)
    Result = gpl_adb_shell(device, f'input text "{text}"')
    if len(Result) > 0:
        return False
    return True



# open a tcpIP and connect (remote adb)
#
# modules:
# gpl_adb_connect_to_IP
# gpl_run_OS_command
# gpl_adb_wlan_IP
#
# version:
# 1
def gpl_adb_tcp_IP(device, port: int, auto_connect=True):
    Serial = device.serial
    IP = gpl_adb_wlan_IP(device)
    gpl_run_OS_command('adb -s ' + Serial + ' tcpip ' + str(port))
    if auto_connect and IP != None:
        return gpl_adb_connect_to_IP(IP, port)
