# NOTE:
# It's also a facade design pattern.

"""     libs        """
# GPL
from lib.GPL.IO import *
from lib.GPL.Timeout import *
from lib.GPL.File_Workers import *
from lib.GPL.Page_Managers import *
from lib.GPL.HTTP_Managers import *
from lib.GPL.String_Workers import *
from lib.GPL.Access_Managers import *
from lib.GPL.Command_Managers import *

# Attackers
# Macro
from lib.GPL.attackers.macro.Mouse import *
from lib.GPL.attackers.macro.Screen import *
from lib.GPL.attackers.macro.Keyboard import *
# Cryptography
from lib.GPL.attackers.cryptography.AES import *
from lib.GPL.attackers.cryptography.HEX import *
from lib.GPL.attackers.cryptography.RSA import *
from lib.GPL.attackers.cryptography.XOR import *
from lib.GPL.attackers.cryptography.MDx import *
from lib.GPL.attackers.cryptography.SHA_x import *
from lib.GPL.attackers.cryptography.base_x import *
# Network
from lib.GPL.attackers.network.ICMP import *
from lib.GPL.attackers.network.IP_Range import *
from lib.GPL.attackers.network.IP_Exists import *
from lib.GPL.attackers.network.IP_To_MAC import *
from lib.GPL.attackers.network.ARP_Spoof import *
from lib.GPL.attackers.network.System_Info import *
from lib.GPL.attackers.network.OS_Detection import *
from lib.GPL.attackers.network.Port_Scanner import *
from lib.GPL.attackers.network.IP_Forwarding import *
from lib.GPL.attackers.network.Hostname_To_IP import *
# Protocol
from lib.GPL.attackers.protocols.SSH import *
from lib.GPL.attackers.protocols.Service_Version_Name_Scanner import *
# IEEE.802.11 (Wi-Fi)
from lib.GPL.attackers.signals.IEEE_802_11_WiFi.Captrue import *
from lib.GPL.attackers.signals.IEEE_802_11_WiFi.Channel import *
from lib.GPL.attackers.signals.IEEE_802_11_WiFi.Monning import *
from lib.GPL.attackers.signals.IEEE_802_11_WiFi.Scanning import *
from lib.GPL.attackers.signals.IEEE_802_11_WiFi.Fake_Packet import *
from lib.GPL.attackers.signals.IEEE_802_11_WiFi.Check_Requirements import *


"""     FACADE      """
from lib.GPL.attackers.macro.Keyboard import Key as Macro_Keyboard_Keys


"""     class       """
class gpl:
    # IO
    def input(*args, **keywords):
        return gpl_input(*args, **keywords)

    def while_input(*args, **keywords):
        return gpl_while_input(*args, **keywords)

    def sleep(*args, **keywords):
        return gpl_sleep(*args, **keywords)

    def confirm(*args, **keywords):
        return gpl_confirm(*args, **keywords)

    # Timeout
    def timeout(*args, **keywords):
        return gpl_timeout(*args, **keywords)

    def raise_timeout(*args, **keywords):
        return raise_timeout(*args, **keywords)

    # Access managers
    class access_managers:
        def check_is_root(*args, **keywords):
            return gpl_check_is_root(*args, ** keywords)

        def check_root_needed_with_error(*args, **keywords):
            return gpl_check_root_needed_with_error(*args, **keywords)

    # HTTP managers
    class HTTP_managers:
        def http_get(*args, **keywords):
            return gpl_http_get(*args, ** keywords)

        def http_post(*args, **keywords):
            return gpl_http_post(*args, **keywords)

    # String workers
    class strings:
        def fix_spases(*args, **keywords):
            return gpl_fix_spases(*args, **keywords)

        def url_encode(*args, **keywords):
            return gpl_url_encode(*args, **keywords)

        def url_decode(*args, **keywords):
            return gpl_url_decode(*args, **keywords)

        def random_string(*args, **keywords):
            return gpl_random_string(*args, **keywords)

        def fix_string_to_uri(*args, **keywords):
            return gpl_fix_string_to_uri(*args, **keywords)

        def convert_to_bytes(*args, **keywords):
            return gpl_convert_to_bytes(*args, **keywords)

        def JSON_loads(*args, **keywords):
            return gpl_JSON_loads(*args, **keywords)

        def JSON_dumps(*args, **keywords):
            return gpl_JSON_dumps(*args, **keywords)

    # Page managers
    class page_managers:
        def clear(*args, **keywords):
            return gpl_clear(*args, **keywords)

        def clear_and_banner(*args, **keywords):
            return gpl_clear_and_banner(*args, **keywords)

        def set_banner_verion(*args, **keywords):
            return gpl_set_banner_verion(*args, **keywords)



    # Command managers
    class command_managers:
        def run_OS_command(*args, **keywords):
            return gpl_run_OS_command(*args, ** keywords)

        def check_command_exists(*args, **keywords):
            return gpl_check_command_exists(*args, **keywords)


    # File Workers
    class file_managers:
        def ask_load_from_file(*args, **keywords):
            return gpl_ask_load_from_file(*args, **keywords)

        def ask_save_to_file(*args, **keywords):
            return gpl_ask_save_to_file(*args, **keywords)

        def read_from_file(*args, **keywords):
            return gpl_read_from_file(*args, **keywords)

        def write_to_file(*args, **keywords):
            return gpl_write_to_file(*args, **keywords)

        def remove_file(*args, **keywords):
            return gpl_remove_file(*args, **keywords)

        def make_directory(*args, **keywords):
            return gpl_make_directory(*args, **keywords)

        def remove_directory(*args, **keywords):
            return gpl_remove_directory(*args, **keywords)


    # Attacker
    class attackers:
        # Cryptography
        class cryptography:
            def xor(*args, **keywords):
                return gpl_xor(*args, **keywords)

            class AES:
                def new_cipher(*args, **keywords):
                    return gpl_AES_new_cipher(*args, **keywords)

                def encrypt(*args, **keywords):
                    return gpl_AES_encrypt(*args, **keywords)

                def decrypt(*args, **keywords):
                    return gpl_AES_decrypt(*args, **keywords)

                def verify(*args, **keywords):
                    return gpl_AES_verify(*args, **keywords)

            class base_x:
                def base16_encode(*args, **keywords):
                    return gpl_base16_encode(*args, **keywords)

                def base16_decode(*args, **keywords):
                    return gpl_base16_decode(*args, **keywords)

                def base32_encode(*args, **keywords):
                    return gpl_base32_encode(*args, **keywords)

                def base32_decode(*args, **keywords):
                    return gpl_base32_decode(*args, **keywords)

                def base64_encode(*args, **keywords):
                    return gpl_base64_encode(*args, **keywords)

                def base64_decode(*args, **keywords):
                    return gpl_base64_decode(*args, **keywords)

                def base85_encode(*args, **keywords):
                    return gpl_base85_encode(*args, **keywords)

                def base85_decode(*args, **keywords):
                    return gpl_base85_decode(*args, **keywords)

            class hex:
                def HEXlify(*args, **keywords):
                    return gpl_HEXlify(*args, **keywords)

                def unHEXlify(*args, **keywords):
                    return gpl_unHEXlify(*args, **keywords)

            class MDx:
                def MD2(*args, **keywords):
                    return gpl_MD2(*args, **keywords)

                def MD5(*args, **keywords):
                    return gpl_MD5(*args, **keywords)

                def MD4(*args, **keywords):
                    return gpl_MD4(*args, **keywords)

            class SHAx:
                def SHA1(*args, **keywords):
                    return gpl_SHA1(*args, **keywords)

                def SHA224(*args, **keywords):
                    return gpl_SHA224(*args, **keywords)

                def SHA256(*args, **keywords):
                    return gpl_SHA256(*args, **keywords)

                def SHA384(*args, **keywords):
                    return gpl_SHA384(*args, **keywords)

                def SHA512(*args, **keywords):
                    return gpl_SHA512(*args, **keywords)

            class RSA:
                def new_keys(*args, **keywords):
                    return gpl_RSA_new_key(*args, **keywords)

                def encrypt(*args, **keywords):
                    return gpl_RSA_encrypt(*args, **keywords)

                def decrypt(*args, **keywords):
                    return gpl_RSA_decrypt(*args, **keywords)


        # Network
        class network:
            def ICMP(*args, **keywords):
                return gpl_icmp(*args, **keywords)

            def ipv4_icmp_exists_check(*args, **keywords):
                return gpl_ipv4_icmp_exists_check(*args, **keywords)

            def IP_to_MAC(*args, **keywords):
                return gpl_ip_to_mac(*args, **keywords)

            def hostname_to_ip(*args, **keywords):
                return gpl_hostname_to_ip(*args, **keywords)

            def OS_detector(*args, **keywords):
                return gpl_OS_detector(*args, **keywords)

            class arp_spoof:
                def fake_once(*args, **keywords):
                    return gpl_arp_spoof_fake_once(*args, **keywords)

                def spoof_thread(*args, **keywords):
                    return gpl_arp_spoof_thread(*args, **keywords)

                def end_attack_thread():
                    return gpl_arp_spoof_end_attack_thread()

            class IP_forwarding:
                def get_ipv4_forward_state():
                    return gpl_get_ipv4_forward_state()

                def set_ipv4_forward_state(*args, **keywords):
                    return gpl_set_ipv4_forward_state(*args, **keywords)

            class range:
                def IPv4_range(*args, **keywords):
                    return gpl_IPv4_range(*args, **keywords)

                def IPv6_range(*args, **keywords):
                    return gpl_IPv6_range(*args, **keywords)

            class port_scanner:
                def port_scanner(*args, **keywords):
                    return gpl_port_scanner(*args, **keywords)

                def is_TCP_open(*args, **keywords):
                    return gpl_is_TCP_open(*args, **keywords)

            class system_info:
                def get_local_system_ip():
                    return gpl_get_local_system_ip()

                def get_remote_system_ip():
                    return gpl_get_remote_system_ip()

                def get_system_hostname():
                    return gpl_get_system_hostname()


        # Macro
        class macro:
            class keyboard:
                def press(*args, **keywords):
                    return gpl_keyboard_press(*args, **keywords)

                def release(*args, **keywords):
                    return gpl_keyboard_release(*args, **keywords)

                def type(*args, **keywords):
                    return gpl_keyboard_type(*args, **keywords)

                def join(*args, **keywords):
                    return gpl_keyboard_join(*args, **keywords)

                def callback(*args, **keywords):
                    return gpl_keyboard_callback(*args, **keywords)

            class mouse:
                def click(*args, **keywords):
                    return gpl_mouse_click(*args, **keywords)

                def move(*args, **keywords):
                    return gpl_mouse_move(*args, **keywords)

                def set_position(*args, **keywords):
                    return gpl_mouse_set_position(*args, **keywords)

                def set_callback(*args, **keywords):
                    return gpl_mouse_set_callback(*args, **keywords)

            class screen:
                def pixel_color(*args, **keywords):
                    return gpl_screen_pixel_color(*args, **keywords)


        # Protocols
        class protocols:
            def find_service_version_name(*args, **keywords):
                return gpl_find_service_version_name(*args, **keywords)

            class SSH:
                def connect(*args, **keywords):
                    return gpl_connect_to_ssh(*args, **keywords)

                def run_command(*args, **keywords):
                    return gpl_run_command_on_SSH(*args, **keywords)

                def disconnect(*args, **keywords):
                    return gpl_disconnect_SSH(*args, **keywords)


        # Signals
        class signals:
            class IEEE_802_11_WiFi:
                def check_requirements(*args, **keywords):
                    return gpl_wifi_check_requirements(*args, **keywords)

                def monning_on():
                    return gpl_wifi_monning_on()

                def monning_off():
                    return gpl_wifi_monning_off()

                def channel(*args, **keywords):
                    return gpl_wifi_channel(*args, **keywords)

                def set_channel(*args, **keywords):
                    return gpl_wifi_set_channel(*args, **keywords)

                def capture_signals(*args, **keywords):
                    return gpl_wifi_capture_signals(*args, **keywords)

                def packet(*args, **keywords):
                    return gpl_wifi_packet(*args, **keywords)

                def scan_signals(*args, **keywords):
                    return gpl_wifi_scan_signals(*args, **keywords)
