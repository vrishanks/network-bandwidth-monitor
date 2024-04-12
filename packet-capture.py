from scapy.all import sniff

def capture_and_parse_packets():
    packets = sniff(iface="eth0", count=10)
    for packet in packets:
        print(packet.summary()) 
capture_and_parse_packets()
