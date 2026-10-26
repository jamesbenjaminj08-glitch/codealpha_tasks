Basic Network Sniffer

CodeAlpha Cybersecurity Internship — Task 1

Project Overview

This project is a basic network sniffer developed using Python and Scapy. It captures a limited number of IP packets from the computer's Wi-Fi interface and displays basic packet information.

Features

Captures up to 10 IP packets or runs for a maximum of 30 seconds.

Identifies TCP, UDP, and ICMP packets.

Displays source IP address and destination IP address.

Displays packet length in bytes.

Does not intentionally display packet payload contents.

Technologies Used

Python

Scapy

Npcap (for packet capture on Windows)

Requirements

Windows

Python

Scapy

Npcap

Installation

Install Scapy by running:

python -m pip install scapy

Install Npcap from the official website: https://npcap.com/

Usage

Connect to your own Wi-Fi network or another network you are authorised to inspect.

Open Command Prompt in the project folder.

Run:

python network_sniffer.py

The program displays packet metadata and finishes after capturing up to 10 packets or reaching the 30-second timeout.

Sample Output

Basic Network Sniffer
Capturing up to 10 packets on Wi-Fi...
Press Ctrl+C to stop early.

UDP 192.168.0.111 -> [remote IP] Length: 1287
TCP 192.168.0.111 -> [remote IP] Length: 55

Capture finished.

The sample output is illustrative; actual addresses, protocols, and packet lengths will vary.

Ethical Use

This tool is intended for educational and defensive cybersecurity learning. Capture traffic only on devices and networks you own or have explicit permission to inspect.

Internship

Completed as part of the CodeAlpha Cybersecurity Internship.
