"""
Network Packet Analyzer - Demo Mode
CodSoft Cyber Security Internship - Task 1

This educational demo uses sample packet data to demonstrate
how a packet analyzer displays network information.

Note: This version does not perform live packet capture.
"""

import time


# Sample packet data for demonstration
sample_packets = [
    {
        "source": "192.168.1.10",
        "destination": "142.250.183.14",
        "protocol": "TCP",
        "source_port": 52341,
        "destination_port": 443,
        "length": 66
    },
    {
        "source": "192.168.1.10",
        "destination": "8.8.8.8",
        "protocol": "UDP",
        "source_port": 54321,
        "destination_port": 53,
        "length": 74
    },
    {
        "source": "192.168.1.10",
        "destination": "192.168.1.1",
        "protocol": "ICMP",
        "source_port": "-",
        "destination_port": "-",
        "length": 98
    },
    {
        "source": "192.168.1.10",
        "destination": "151.101.1.69",
        "protocol": "TCP",
        "source_port": 52342,
        "destination_port": 443,
        "length": 60
    },
    {
        "source": "192.168.1.1",
        "destination": "192.168.1.10",
        "protocol": "UDP",
        "source_port": 67,
        "destination_port": 68,
        "length": 342
    }
]


def analyze_packet(packet, packet_number):
    """Display information about one sample packet."""

    print("\n" + "=" * 60)
    print(f"Packet #{packet_number}")
    print("=" * 60)

    print(f"Source IP       : {packet['source']}")
    print(f"Destination IP  : {packet['destination']}")
    print(f"Protocol        : {packet['protocol']}")
    print(f"Packet Length   : {packet['length']} bytes")

    if packet["protocol"] in ["TCP", "UDP"]:
        print(f"Source Port     : {packet['source_port']}")
        print(f"Destination Port: {packet['destination_port']}")


def main():
    """Run the packet analyzer demonstration."""

    print("=" * 60)
    print("             NETWORK PACKET ANALYZER")
    print("=" * 60)
    print("Mode: DEMONSTRATION / SAMPLE PACKETS")
    print("Analyzing sample network packet data...")

    for number, packet in enumerate(sample_packets, start=1):
        time.sleep(0.5)
        analyze_packet(packet, number)

    print("\n" + "=" * 60)
    print("Packet analysis completed.")
    print("=" * 60)


if __name__ == "__main__":
    main()
