
"""
CodeAlpha Cybersecurity Internship
Project: Basic Network Sniffer

Captures a short sample of packet headers on the
computer's own Wi-Fi interface.
Use only on networks you are authorised to inspect.
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP

def show_packet(packet):
    if IP not in packet:
        return

    source = packet[IP].src
    destination = packet[IP].dst
    protocol = packet[IP].proto
    length = len(packet)

    if TCP in packet:
        protocol_name = "TCP"
    elif UDP in packet:
        protocol_name = "UDP"
    elif ICMP in packet:
        protocol_name = "ICMP"
    else:
        protocol_name = f"IP protocol {protocol}"

    print(
        f"{protocol_name:15} "
        f"{source:16} -> {destination:16} "
        f"Length: {length}"
    )

if __name__ == "__main__":
    print("Basic Network Sniffer")
    print("Capturing up to 10 packets on Wi-Fi...")
    print("Press Ctrl+C to stop early.\n")

    try:
        sniff(
            iface="Intel(R) Dual Band Wireless-AC 8260",
            prn=show_packet,
            store=False,
            count=10,
            timeout=30
        )
    except PermissionError:
        print("Permission denied. Try running Command Prompt as administrator.")
    except Exception as error:
        print(f"Capture error: {error}")

    print("\nCapture finished.")