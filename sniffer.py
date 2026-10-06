import sys
from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def handle_packet(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]

        if packet.haslayer(TCP):
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            print(f"[TCP] {ip_layer.src}:{sport} -> {ip_layer.dst}:{dport}")

        elif packet.haslayer(UDP):
            sport = packet[UDP].sport
            dport = packet[UDP].dport
            print(f"[UDP] {ip_layer.src}:{sport} -> {ip_layer.dst}:{dport}")

        elif packet.haslayer(ICMP):
            print(f"[ICMP] {ip_layer.src} -> {ip_layer.dst}")

        else:
            print(f"[OTHER] {ip_layer.src} -> {ip_layer.dst}  (protocol #{ip_layer.proto})")

        if packet.haslayer(Raw):
            payload = packet[Raw].load
            try:
                text = payload.decode("utf-8", errors="replace")
            except Exception:
                text = str(payload)
            preview = text.strip().replace("\n", " ")[:80]
            if preview:
                print(f"    Payload preview: {preview}")
    else:
        print("Non-IP packet:", packet.summary())

if __name__ == "__main__":
    bpf_filter = sys.argv[1] if len(sys.argv) > 1 else ""
    iface = "eth0"

    print(f"Starting sniffer on iface={iface}  filter='{bpf_filter or 'none'}' ... press Ctrl+C to stop.")
    sniff(prn=handle_packet, iface=iface, filter=bpf_filter if bpf_filter else None, store=False, count=20)
