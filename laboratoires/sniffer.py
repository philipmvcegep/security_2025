import sys
from scapy.all import sniff, IP

def packet_callback(packet):
    """
    Processes captured packets and prints relevant information.
    """
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print(f"[*] IP Packet: {ip_layer.src} -> {ip_layer.dst} (Protocol: {ip_layer.proto})")

def start_sniffer(interface="eth0", count=20):
    """
    Starts sniffing on the specified interface.
    """
    print(f"[*] Starting sniffer on {interface}. Capturing {count} packets...")
    # sniff() continuously captures packets until 'count' is reached or Ctrl+C is pressed
    sniff(iface=interface, prn=packet_callback, filter="ip", count=count, store=0)

if __name__ == "__main__":
    # --- IMPORTANT ---
    # 1. Ensure your arp_poison.py is running in a separate window.
    # 2. You must run this script with elevated privileges (sudo).
    
    # You may need to change 'eth0' to your actual interface name (e.g., 'ens33', 'wlan0')
    start_sniffer(interface="eth0", count=50)
