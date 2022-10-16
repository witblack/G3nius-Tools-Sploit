"""     libs        """
from lib.GPL.attackers.signals.IEEE_802_11_WiFi.Fake_Packet import gpl_wifi_packet

# attacker
def IEEE_802_11_Attacker(BSSID, Count):
    gpl_wifi_packet(BSSID, Count=Count)