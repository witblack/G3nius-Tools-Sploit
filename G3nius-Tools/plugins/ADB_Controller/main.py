# import G3nius-Tools
# coding: utf-8

"""     libs       """
# GPL
import pprint

from lib.classes.gpl import gpl_set_banner_verion, gpl_clear_and_banner
from lib.classes.gpl import gpl_input, gpl_while_input
from lib.classes.gpl import Error_Levels, Handler

# GPL ADB & Start daemon
from lib.classes.gpl import gpl
adb = gpl.attackers.macro.ADB
adb.connected_devices()

# termcolor
from lib.packages.termcolor import colored

# configs
from lib.config.Main_Configs import Product_Name

# plugin
from plugins.ADB_Controller.Commands_Config import Help_Commands, Known_Commands
from plugins.ADB_Controller.Args_Manager import Manage_args, Join_args
from plugins.ADB_Controller.Show_Device import Show_Device

# external
from os.path import isfile

""""    Version     """
gpl_set_banner_verion("2.0.0")


"""     Command     """
gpl_clear_and_banner()
# Holders
Selected_Devices = []
Spliter = colored(" -\t", 'cyan')
# UI
Handler(Error_Levels.Plus, "First time run `select` command to select operating device(s).", "Commands will execute on every selected devices.")
while True:
    args = gpl_input("\n\n" + colored("Command ", 'blue') + colored('(`?` to help)', 'magenta') + colored(" ~> ", 'red'), clear_and_banner_before=False).split(' ')
    Command = args[0]
    args = args[1:]
    """     Commands    """
    # Error blocker
    try:
        if Command not in Known_Commands:
            # Command not found
            Handler(Error_Levels.Minus, "Command not found! Enter `?` to help.")
        elif Command == '?' or Command == 'help':
            # Help Page
            Handler(Error_Levels.Star, "List of all commands:\n\n")
            for Key in Help_Commands:
                Handler(Error_Levels.NoStyle, colored("~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~", 'red'))
                Handler(Error_Levels.Plus, Key)
                Handler(Error_Levels.Plus, Help_Commands[Key])
        elif Command == 'clear':
            gpl_clear_and_banner()
        elif Command == 'select':
            # [serial number]
            # List of serials
            Devices = adb.connected_devices()
            Serials = []
            for Device in Devices:
                # can be select if not selected
                if Device not in Selected_Devices:
                    Serials.append(Device.prop.model + Spliter + Device.serial)
            Serials.append('Cancel selection.')
            # if unselected device not found
            if len(Serials) == 1:
                Handler(Error_Levels.Minus, "A device with selected capability was not found!", "May be already selected or not connected.")
                continue
            # select
            Choose = gpl_while_input("Select device for add to selected devices.", Serials, exit_option=False)
            if Choose <= len(Devices):
                # select device
                Selected_Devices.append(Devices[Choose - 1])
                gpl_clear_and_banner()
                Handler(Error_Levels.Plus, 'Device selected. Also you can select more devices.')
            else:
                gpl_clear_and_banner()
                Handler(Error_Levels.Minus, 'Selection cancelled.')
            pass
        elif Command == 'devices':
            Devices = adb.connected_devices()
            if len(Devices) > 0:
                for Device in Devices:
                    Show_Device(Device)
            else:
                Handler(Error_Levels.Minus, "No one ADB device connected. Connect your phone and turn on ADB.")
        elif Command == 'connect':
            # [IP | IP:Port]
            arg = Join_args(args)
            if adb.connect_to_IP(arg):
                Handler(Error_Levels.Plus, f"Successfully connected to {arg}.")
            else:
                Handler(Error_Levels.Plus, f"Failed to connect {arg}.")
        else:
            # Check selected devices list
            if len(Selected_Devices) == 0:
                Handler(Error_Levels.Minus, 'No device selected! First run `select` command to select device(s).')
                continue
            # Do job on every selected devices
            for Device in Selected_Devices:
                # Device name
                Full_Name = Device.prop.name + Spliter + Device.serial
                Handler(Error_Levels.NoStyle, "\n")
                # Process
                if Command == 'list-selected' or Command == 'device_info':
                    Show_Device(Device)
                elif Command == 'unselect':
                    # generate list of selected devices serial
                    Serials = []
                    for Device in Selected_Devices:
                        Serials.append(Device.prop.model + Spliter + Device.serial)
                    Serials.append('Cancel unselection.')
                    # select by user
                    Device_ID = gpl.while_input("Select a device to unselect:", Serials, exit_option=False)
                    # unselect
                    if Device_ID >= (len(Selected_Devices) + 1):
                        Selected_Devices.remove(Selected_Devices[Device_ID - 1])
                        Handler(Error_Levels.Plus, f"{Selected_Devices[Device_ID-1].serial} ~> Disconnected.")
                    else:
                        gpl_clear_and_banner()
                        Handler(Error_Levels.Minus, 'Unselection cancelled.')
                    del Device_ID
                    break
                elif Command == 'wlan_IP':
                    IP = adb.wlan_IP(Device)
                    Handler(Error_Levels.Plus, f"{Full_Name} ~> {IP}")
                elif Command == 'tcp_IP':
                    # [Port]
                    arg = Join_args(args)
                    try:
                        arg = int(arg)
                    except:
                        Handler(Error_Levels.Minus, f"Invalid port number! try like: tcp_IP 4444")
                    else:
                        Result = adb.tcp_IP(Device, arg)
                        if Result:
                            # OK & Connected
                            Handler(Error_Levels.Plus, f"{Full_Name} ~> TCP IP opened and automatically connected.")
                        else:
                            Handler(Error_Levels.Minus, f"{Full_Name} ~> Can't auto connect to TCP IP! Check port {arg}.", "Check network of device connected to your network.")
                        del Result
                elif Command == 'disconnect':
                    adb.disconnect_IP(Device.serial)
                    Selected_Devices.remove(Device)
                    Handler(Error_Levels.Plus, f"{Full_Name} ~> Try to disconnect, unselected.", "Only WLAN ADB will disconnected.")
                elif Command == 'wifi':
                    # [off | on]
                    arg = Manage_args(args[0], ['on', 'off'])
                    if arg == 'on':
                        adb.wifi(Device, True)
                        Handler(Error_Levels.Plus, f"{Full_Name} ~> Wi-Fi turn on.")
                    elif arg == 'off':
                        adb.wifi(Device, False)
                        Handler(Error_Levels.Plus, f"{Full_Name} ~> Wi-Fi turn off.")
                elif Command == 'list_apps':
                    Handler(Error_Levels.Plus, f"{Full_Name}:")
                    for Package_Name in adb.list_apps(Device):
                        Handler(Error_Levels.Star, Package_Name, Print_Before="\t")
                    del Package_Name
                elif Command == 'is_rooted':
                    if adb.is_rooted(Device):
                        Handler(Error_Levels.Plus, f"{Full_Name} ~> Root on device found.")
                    else:
                        Handler(Error_Levels.Plus, f"{Full_Name} ~> Device not rooted!")
                elif Command == 'command':
                    # [command]
                    Output = adb.shell(Device, Join_args(args))
                    Handler(Error_Levels.Plus, f"{Full_Name} output ~> \n{Output}")
                    del Output
                elif Command == 'install':
                    # [APK path]
                    URI = Join_args(args)
                    if isfile(URI):
                        # APK exists
                        if adb.install_apk(Device, URI):
                            Handler(Error_Levels.Plus, f"{Full_Name} ~> App installed.")
                        else:
                            Handler(Error_Levels.Minus, f"{Full_Name} ~> Failed to install APK.")
                    else:
                        Handler(Error_Levels.Minus, "APK file not exists!")
                    del URI
                elif Command == 'install_URL':
                    # [APK URL]
                    URL = Join_args(args)
                    if adb.install_URL_APK(Device, URL):
                        Handler(Error_Levels.Plus, f"{Full_Name} ~> App installed.")
                    else:
                        Handler(Error_Levels.Minus, f"{Full_Name} ~> Failed to install APK from URL.", "Check your URL.")
                    del URL
                elif Command == 'uninstall':
                    # [package name]
                    Package_Name = Join_args(args)
                    if adb.uninstall_app(Device, Package_Name):
                        Handler(Error_Levels.Plus, f"{Full_Name} ~> Application uninstalled.")
                    else:
                        Handler(Error_Levels.Minus, f"{Full_Name} ~> Failed to uninstall application.", "May be app not installed.")
                elif Command == 'open':
                    # [package name]
                    Package_Name = args[0]
                    Activity = Join_args(args[1:])
                    # Check &
                    if Activity.replace(' ', '') != '':
                        adb.open_app(Device, Activity)
                        Handler(Error_Levels.Plus, f"{Full_Name} ~> Application opened.")
                    else:
                        adb.open_app(Device, Activity)
                        Handler(Error_Levels.Plus, f"{Full_Name} ~> Application opened at {Activity}.")
                    adb.open_app(Device, args[0])
                elif Command == 'close':
                    # [package name]
                    Package_Name = Join_args(args)
                    adb.close_app(Device, Package_Name)
                    Handler(Error_Levels.Plus, f"{Full_Name} ~> App closed.")
                elif Command == 'clear_data':
                    # [package name]
                    Package_Name = Join_args(args)
                    if len(Package_Name) > 1:
                        adb.clear_data_app(Device, Package_Name)
                        Handler(Error_Levels.Plus, f"{Full_Name} ~> Data reset on {Package_Name} app.")
                    else:
                        Handler(Error_Levels.Plus, f"{Full_Name} ~> Invalid package name!")
                elif Command == 'app_info':
                    # [package name]
                    Package_Name = Join_args(args)
                    Info = adb.app_info(Device, Package_Name)
                    Handler(Error_Levels.Plus, f"{Full_Name} ~> App info:\n")
                    for Key in Info:
                        Handler(Error_Levels.Star, f"{Key}:\t{Info[Key]}", Print_Before="\t")
                    del Info, Key
                elif Command == 'shutdown':
                    adb.shutdown(Device)
                    Selected_Devices.remove(Device)
                    Handler(Error_Levels.Plus, f"{Full_Name} ~> Shutdown.")
                elif Command == 'reboot':
                    adb.reboot(Device)
                    Selected_Devices.remove(Device)
                    Handler(Error_Levels.Plus, f"{Full_Name} ~> Shutdown.")
                elif Command == 'kill_server':
                    adb.kill_server()
                    Handler(Error_Levels.Plus, f"{Product_Name} ADB killed. Selected devices reset.")
                    Selected_Devices = []
                elif Command == 'download':
                    # [file path on device]
                    arg = Join_args(args)
                    adb.transfer_from_client(Device, arg, './')
                    Handler(Error_Levels.Plus, f"{Full_Name} ~> File {arg} transformed to G3nius, See files here.")
                elif Command == 'upload':
                    # [file path on hacker PC]
                    arg = Join_args(args)
                    adb.transfer_to_client(Device, arg, '/storage/self/primary/')
                    Handler(Error_Levels.Plus, f"{Full_Name} ~> File {arg} transformed to client, See files on internal device storage.")
                elif Command == 'ls':
                    # [path]
                    arg = Join_args(args)
                    Files_Dir = adb.list_files_folders(Device, arg)
                    Handler(Error_Levels.Plus, f"{Full_Name} ~> List of files/directories:\n")
                    Handler(Error_Levels.NoStyle, f"\nName\tSize (Byte)\tMode\tlast_modify\n")
                    for File_Dir in Files_Dir:
                        Handler(Error_Levels.NoStyle, f"{File_Dir.name}{Spliter}{File_Dir.size}{Spliter}{File_Dir.mode}{Spliter}{File_Dir.mtime}")
                        del File_Dir
                    del Files_Dir
                elif Command == 'airplane':
                    # [off  | on]
                    arg = Manage_args(args[0], ['on', 'off'])
                    if arg == 'on':
                        adb.airplane_mode(Device, True)
                        Handler(Error_Levels.Plus, f"{Full_Name} ~> Airplane mode turn on.")
                    elif arg == 'off':
                        adb.airplane_mode(Device, False)
                        Handler(Error_Levels.Plus, f"{Full_Name} ~> Airplane mode turn off.")
                elif Command == 'battery':
                    Output = adb.battery(Device)
                    Handler(Error_Levels.NoStyle, f"{Full_Name} Battery status:\n{Output}")
                    del Output
                elif Command == 'netstat':
                    Output = adb.netstat(Device)
                    Handler(Error_Levels.NoStyle, f"{Full_Name} Netstat:\n{Output}")
                    del Output
                elif Command == 'volume':
                    # [up | down]
                    arg = Manage_args(args[0], ['up', 'down'])
                    if arg:
                        Volume = gpl.input("Enter value to decrease/increase volume (MAX: 10): ", clear_and_banner_before=False, get_int=True)
                        if arg == 'up':
                            adb.volume(Device, Volume)
                        else:
                            adb.volume(Device, Volume, False)
                elif Command == 'screen_status':
                    if adb.is_screen_on(Device):
                        Handler(Error_Levels.Plus, f"{Full_Name} ~> Screen is on.")
                    else:
                        Handler(Error_Levels.Plus, f"{Full_Name} ~> Screen is off.")
                elif Command == 'mute-unmute':
                    adb.volume_mute_unmute(Device)
                    Handler(Error_Levels.Plus, f"{Full_Name} ~> Mute/Unmute.")
                elif Command == 'run_keycode':
                    # [keycode numbers, ...]
                    for Keycode in args:
                        # run list of keycodes
                        try:
                            Keycode = int(Keycode)
                        except:
                            Handler(Error_Levels.Minus, f"{Full_Name} ~> Invalid ADB keycode!")
                        else:
                            adb.run_keycode(Device, Keycode)
                            Handler(Error_Levels.Plus, f"{Full_Name} ~> ")
                            del Keycode
                elif Command == 'browser':
                    # [URL]
                    URL = Join_args(args)
                    adb.open_browser(Device, URL)
                    del URL
                elif Command == 'screen':
                    # [on | off]
                    arg = Manage_args(args[0], ['on', 'off'])
                    if arg == 'on':
                        adb.change_screen_status(Device, True)
                        Handler(Error_Levels.Plus, f"{Full_Name} ~> Screen turn on.")
                    elif arg == 'off':
                        adb.change_screen_status(Device, False)
                        Handler(Error_Levels.Plus, f"{Full_Name} ~> Screen turn off.")
                    del arg
                elif Command == 'screen-lock':
                    adb.lock_screen(Device)
                    Handler(Error_Levels.Plus, f"{Full_Name} ~> Screen locked.")
                elif Command == 'screenshot':
                    # [PNG path]
                    Destination = Join_args(args)
                    if adb.screenshot(Device, f"{Destination}-{Full_Name}.png"):
                        Handler(Error_Levels.Plus, f"{Full_Name} ~> Screenshot saved.")
                    else:
                        Handler(Error_Levels.Minus, f"{Full_Name} ~> Failed to do screenshot.")
                    del Destination
                elif Command == 'ps':
                    Process = adb.list_processes(Device, return_list=False)
                    Process = Process[2:-2].replace("', '", "/n")
                    Handler(Error_Levels.NoStyle, f"{Full_Name} List of process:\n{Process}")
                    del Process
                elif Command == 'contacts':
                    Contacts = adb.extract_contacts(Device, return_list=False)
                    Handler(Error_Levels.NoStyle, f"{Full_Name} List of contacts:\n{Contacts}")
                    del Contacts
                elif Command == 'sms':
                    SMSs = adb.extract_SMS(Device, return_list=False)
                    Handler(Error_Levels.NoStyle, f"{Full_Name} List of process:\n{SMSs}")
                    del SMSs
                else:
                    # Type [Text]
                    arg = Join_args(args)
                    adb.keyboard_type(Device, arg)
                    Handler(Error_Levels.Plus, f"{Full_Name} Text typed in device.")
    except IndexError:
        # args not found
        Handler(Error_Levels.Minus, "Invalid syntax, run `?` to see command usage.")
    except Exception as EX:
        EX = str(EX)
        if "' not found" in EX:
            Serial = EX.replace("' not found", '').replace("device '", '')
            Handler(Error_Levels.High, f"Device with serial {Serial} disconnected, Removed form selected. :(")
            Handler(Error_Levels.High, "Your command not executed, Please retry.")
            # unselect
            for Device in Selected_Devices:
                if Device.serial == Serial:
                    Selected_Devices.remove(Device)
        else:
            Handler(Error_Levels.Minus, "Failed to process command!", EX)
