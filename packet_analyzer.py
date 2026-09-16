"""
Network Packet Analyzer
CodSoft Cyber Security Internship - Task 1

Description:
A simple Python-based network packet analyzer that captures
network packets using Scapy and displays basic information
about each packet.

Educational use only. Capture traffic only on networks
you own or have permission to monitor.
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP


def analyze_packet(packet):
    """Analyze and display information about a captured packet."""

    print("\n" + "=" * 60)

    # Check whether the packet contains an IP layer
    if IP in packet:
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        # Identify the transport/network protocol
        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"
        else:
            protocol = "Other"

        print(f"Source IP      : {source_ip}")
        print(f"Destination IP : {destination_ip}")
        print(f"Protocol       : {protocol}")
        print(f"Packet Length  : {len(packet)} bytes")

        # Display TCP/UDP port information when available
        if TCP in packet:
            print(f"Source Port    : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif UDP in packet:
            print(f"Source Port    : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

    else:
        print("Non-IP Packet")
        print(f"Packet Length  : {len(packet)} bytes")


def main():
    """Start the packet analyzer."""

    print("=" * 60)
    print("             NETWORK PACKET ANALYZER")
    print("=" * 60)
    print("Starting packet capture...")
    print("Capturing 10 packets.")
    print("Press Ctrl+C to stop the capture.\n")

    try:
        sniff(
            prn=analyze_packet,
            count=10
        )

        print("\n" + "=" * 60)
        print("Packet capture completed.")
        print("=" * 60)

    except PermissionError:
        print("\nPermission denied.")
        print("Please run the program with administrator/root privileges.")

    except KeyboardInterrupt:
        print("\n\nPacket capture stopped by user.")

    except Exception as error:
        print(f"\nAn error occurred: {error}")


if __name__ == "__main__":
    main()
