import dpkt, socket, sys
from collections import Counter

file = open('proj3.pcap', 'rb')
pcap = dpkt.pcap.Reader(file)

countSYN = Counter()
countACK = Counter()

for ts, buf in pcap:

    if dpkt.dpkt.NeedData:
        continue
    eth = dpkt.ethernet.Ethernet(buf)

    if isinstance(eth.data, dpkt.ip.IP):
        ip = eth.data

        if isinstance(ip.data, dpkt.tcp.TCP):
            tcp = ip.data

            if (tcp.flags & dpkt.tcp.TH_SYN) and not(tcp.flags & dpkt.tcp.TH_ACK):
                if ip.src in countSYN:
                    countSYN[ip.src] += 1
            if (tcp.flags & dpkt.tcp.TH_SYN) and (tcp.flags & dpkt.tcp.TH_ACK):
                if ip.dst in countACK:
                    countACK[ip.dst] += 1

for IP in countSYN:
    if IP in countACK:
        if (countSYN[IP] > 3*(countACK[IP])):
            print(socket.inet_ntoa(IP))
        else:
            print(socket.inet_ntoa(IP))
