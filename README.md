# Network Bandwidth Monitor
The Network Bandwidth Monitor is a Python tool designed to analyze network traffic captured in packet capture files (PCAP). It provides various features to help users understand and visualize network bandwidth usage and packet characteristics. 

`Read and Parse Packet Capture Files (PCAP)`:
- The tool can read and parse packet capture files in PCAP format, which are commonly used to store network traffic data captured by tools like Wireshark or tcpdump.

`Calculate Metrics`:
- It calculates essential network traffic metrics such as total bandwidth usage and average packet size. These metrics provide insights into the overall network activity and the size distribution of packets.

`Visualize Bandwidth Usage Over Time`:
- The tool generates visualizations to show how network bandwidth usage changes over time. This helps users identify patterns, peaks, and trends in network activity.

`Visualize Packet Size Distribution`:
- It visualizes the distribution of packet sizes within the captured network traffic. This histogram allows users to understand the range and frequency of packet sizes, which can be useful for network optimization and troubleshooting.

`Detect Anomalies in Packet Sizes`:
- The tool can detect anomalies in packet sizes based on predefined criteria. Anomalies could indicate potential issues or irregularities in the network traffic, such as unusually large or small packets.

`Visualize Detected Anomalies`:
- It provides visualizations of detected anomalies, making it easier for users to identify and analyze abnormal network behavior. These visualizations can aid in diagnosing network problems and improving network security.

## Features

- Read and parse packet capture files (PCAP).
- Calculate total bandwidth usage and average packet size.
- Visualize network bandwidth usage over time.
- Visualize packet size distribution.
- Detect anomalies in packet sizes.
- Visualize detected anomalies.

## Requirements

- Python 3.x
- Scapy library
- Matplotlib library

## Usage

1. Clone the repository: **git clone https://github.com/yourusername/network-bandwidth-monitor.git**
2. Install the required dependencies: **pip install scapy matplotlib** 
3. Run the `network_bandwidth_monitor.py` script: **python network_bandwidth_monitor.py**
4. Follow the on-screen instructions to analyze your packet capture file.

## File Structure

- `network_bandwidth_monitor.py`: Main Python script for analyzing network traffic.
- `new_synthetic_packet_capture.pcap`: Sample packet capture file for testing.
- `README.md`: Project documentation in Markdown format.
- `bandwidth_plot.png`: Output file containing the visualization of bandwidth usage.
- `packet_size_distribution.png`: Output file containing the visualization of packet size distribution.
- `anomalies_plot.png`: Output file containing the visualization of detected anomalies in packet sizes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




