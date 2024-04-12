from scapy.all import rdpcap
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

def read_packet_capture_file(file_path):
    print("Reading packet capture file...")
    packets = rdpcap(file_path)
    print("Packet capture file read successfully.")
    return packets

def calculate_metrics(packets):
    print("\nCalculating metrics...")
    total_bytes = sum(len(packet) for packet in packets)
    total_packets = len(packets)
    bandwidth = total_bytes / 1024
    avg_packet_size = total_bytes / total_packets if total_packets > 0 else 0
    print("Metrics calculated successfully.")
    return bandwidth, avg_packet_size

def visualize_bandwidth(packets, data):
    print("\nVisualizing bandwidth usage...")
    num_packets = len(packets)
    print("Number of Packets:", num_packets)
    
    plt.plot(data, label='Bandwidth')
    plt.xlabel("Packet Number")
    plt.ylabel("Bandwidth (KB)")
    plt.title("Network Bandwidth Usage")
    plt.legend()
    plt.savefig("bandwidth_plot.png")
    print("Bandwidth usage visualization saved as 'bandwidth_plot.png'.")

def visualize_packet_size_distribution(packets):
    print("\nVisualizing packet size distribution...")
    packet_sizes = [len(packet) for packet in packets]
    plt.hist(packet_sizes, bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Packet Size (bytes)')
    plt.ylabel('Frequency')
    plt.title('Packet Size Distribution')
    plt.legend(['Packet Size Distribution'])
    plt.savefig('packet_size_distribution.png')
    print("Packet size distribution visualization saved as 'packet_size_distribution.png'.")

def detect_anomalies(packets, avg_packet_size):
    print("\nDetecting anomalies...")
    anomalies = []
    for packet in packets:
        packet_size = len(packet)
        if packet_size > 2 * avg_packet_size or packet_size < 0.5 * avg_packet_size:
            anomalies.append(packet)
    print("Anomalies detected successfully.")
    return anomalies

def visualize_anomalies(anomalies):
    print("\nVisualizing detected anomalies...")
    plt.figure(figsize=(10, 5))
    plt.scatter(range(len(anomalies)), [len(packet) for packet in anomalies], color='red', label='Anomalies')
    plt.xlabel('Packet Index')
    plt.ylabel('Packet Size (bytes)')
    plt.title('Detected Anomalies in Packet Sizes')
    plt.legend()
    plt.savefig('anomalies_plot.png')
    print("Detected anomalies visualization saved as 'anomalies_plot.png'.")

def analyze_flows(packets):
    print("\nAnalyzing flows...")
    flow_packet_sizes = [len(packet) for packet in packets]
    plt.figure(figsize=(10, 5))
    plt.hist(flow_packet_sizes, bins=20, color='orange', edgecolor='black')
    plt.xlabel('Packet Size (bytes)')
    plt.ylabel('Frequency')
    plt.title('Flow Packet Size Distribution')
    plt.savefig('flow_packet_size_distribution.png')
    print("Flow packet size distribution visualization saved as 'flow_packet_size_distribution.png'.")

def main():
    packets = read_packet_capture_file("new_synthetic_packet_capture.pcap")

    bandwidth, avg_packet_size = calculate_metrics(packets)
    print("\nTotal Bandwidth (KB):", bandwidth)
    print("Average Packet Size (bytes):", avg_packet_size)

    data = [len(packet) / 1024 for packet in packets]
    visualize_bandwidth(packets, data)

    visualize_packet_size_distribution(packets)

    anomalies = detect_anomalies(packets, avg_packet_size)
    print("Number of Detected Anomalies:", len(anomalies))

    visualize_anomalies(anomalies)

    analyze_flows(packets)

    print("Analysis completed successfully.")

if __name__ == "__main__":
    main()


# rm anomalies_plot.png bandwidth_plot.png packet_size_distribution.png new_synthetic_packet_capture.pcap
# python dataset.py
# python packet-capture.py
