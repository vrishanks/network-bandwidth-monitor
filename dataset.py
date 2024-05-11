from scapy.all import Ether, IP, TCP, wrpcap
import random

def generate_packet_capture_data(file_path):
    packets = []
    for i in range(800):
        src_ip = "172.16." + ".".join(str(random.randint(0, 255)) for _ in range(2))
        dst_ip = "192.168." + ".".join(str(random.randint(0, 255)) for _ in range(2))
        packet_size = random.randint(64, 2000)
        
        packet = Ether() / IP(src=src_ip, dst=dst_ip) / TCP() / ("X" * packet_size)
        packets.append(packet)
    
    wrpcap(file_path, packets)

generate_packet_capture_data("new_synthetic_packet_capture.pcap")
