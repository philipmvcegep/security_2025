import sys
from scapy.all import *

def scapy_traceroute(target_host, max_hops=30):
    """
    Performs a custom traceroute using Scapy.

    :param target_host: The domain name or IP address of the target.
    :param max_hops: The maximum TTL (hops) to check.
    """
    print(f"Traceroute to {target_host} (Max Hops: {max_hops}):")
    
    # Resolve the IP once
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print("Error: Could not resolve target host name.")
        return

    for ttl in range(1, max_hops + 1):
        # 1. Craft the packet: IP layer with current TTL, stacked with ICMP
        packet = IP(dst=target_ip, ttl=ttl) / ICMP()
        
        # 2. Send the packet and wait for a single response (verbose=0 suppresses output)
        reply = sr1(packet, timeout=1, verbose=0)
        
        # 3. Process the reply
        
        if reply is None:
            # No response received within the timeout
            print(f" {ttl:<2}  * * *")
        
        elif reply.haslayer(ICMP):
            icmp_layer = reply[ICMP]
            
            if icmp_layer.type == 11 and icmp_layer.code == 0:
                # Type 11, Code 0 is 'Time-to-live exceeded' (TTL=0 at a router)
                # The source IP of this reply is the router's address
                print(f" {ttl:<2}  {reply.src}")
                
            elif icmp_layer.type == 0:
                # Type 0 is 'Echo reply' (Destination reached)
                print(f" {ttl:<2}  {reply.src} (Destination Reached)")
                
                # Exit the loop once the destination is reached
                break
                
            else:
                # Other ICMP types (e.g., Destination Unreachable)
                print(f" {ttl:<2}  {reply.src} (ICMP Type {icmp_layer.type})")
        
        else:
            # Received a non-ICMP packet (e.g., UDP/TCP depending on the original probe)
            # Standard traceroute uses UDP or ICMP, but we'll stick to ICMP here
            print(f" {ttl:<2}  {reply.src} (Non-ICMP Response)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: sudo python3 traceroute_script.py <target_host>")
        sys.exit(1)
        
    # NOTE: You must run this script with elevated privileges (sudo) 
    # to send custom Layer 3 (IP) packets.
    target = sys.argv[1]
    scapy_traceroute(target)
