# Network Bandwidth Monitor

Network Bandwidth Monitor is a Python tool for analyzing network traffic captured in a packet capture file (PCAP). It calculates metrics such as total bandwidth usage, average packet size, visualizes bandwidth usage over time, and detects anomalies in packet sizes.

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




