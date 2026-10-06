# CodeAlpha_NetworkSniffer

A basic network packet sniffer built with Python and Scapy, developed for CodeAlpha's Cybersecurity Internship (Task 1).

## Overview

This project captures live network traffic on a chosen interface and breaks each packet down into readable information: source and destination IP addresses, the transport-layer protocol (TCP, UDP, or ICMP) with port numbers where relevant, and a short preview of the packet's actual payload. It also supports optional traffic filtering using BPF (Berkeley Packet Filter) syntax, the same filter language used by tools like tcpdump and Wireshark.

## Features

- Live packet capture using Scapy's sniff() function
- IP layer parsing - extracts source and destination addresses from every captured packet
- Protocol identification - distinguishes TCP, UDP, and ICMP traffic, displaying port numbers for TCP/UDP
- Payload inspection - decodes and previews the first 80 characters of any packet's raw data (e.g. HTTP request headers)
- Optional filtering - pass a BPF expression as a command-line argument to narrow capture to specific traffic

## Requirements

- Python 3
- Scapy (sudo apt install python3-scapy on Debian/Kali-based systems, or pip3 install scapy)
- Root privileges (raw packet capture requires raw socket access, restricted to root on Linux)

## Usage

Capture all traffic on the active interface:
    sudo python3 sniffer.py

Capture only TCP traffic:
    sudo python3 sniffer.py "tcp"

Capture only traffic on a specific port:
    sudo python3 sniffer.py "port 80"

Press Ctrl+C at any time to stop capturing early.

## Example Output (real captured traffic)

Captured live DNS resolution, TCP handshake, and HTTP request/response while running ping and curl against real external hosts:

    [UDP] 10.0.0.2:39261 -> 8.8.8.8:53
    [UDP] 8.8.8.8:53 -> 10.0.0.2:39261
    [TCP] 10.0.0.2:43162 -> 104.20.23.154:80
        Payload preview: Accept: */* curl/8.20.0 / HTTP/1.1
    [TCP] 104.20.23.154:80 -> 10.0.0.2:43162
        Payload preview: Content-Type: text/html; charset=utf-8

Full raw capture saved in capture_evidence.txt.

## How It Works

Every network conversation is broken into small units called packets, each carrying layered headers: an Ethernet layer for local delivery, an IP layer identifying sender and receiver, and (for most traffic) a transport layer such as TCP or UDP identifying the specific service via port numbers. This sniffer inspects each passing packet, checks which layers are present, and prints the relevant fields in a human-readable format, along with a preview of the actual data being transmitted when available.

## Disclaimer

This tool is intended strictly for educational use and for monitoring traffic on networks and systems you own or have explicit permission to test.

## Author

Built as part of the CodeAlpha Cybersecurity Internship (Task 1: Basic Network Sniffer).
