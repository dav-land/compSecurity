import dpkt, socket
from collections import Counter

file = open('proj3.pcap', 'rb')
pcap = dpkt.pcap.Reader(file)

countSYN = Counter()
countACK = Counter()

# used code from "https://jon.oberheide.org/blog/2008/10/15/dpkt-tutorial-2-parsing-a-pcap-file/" for iteration
for ts, buf in pcap:
    #ignore malformed packets
    try:
        eth = dpkt.ethernet.Ethernet(buf)
    except dpkt.dpkt.NeedData:
        pass

    #only use IP packets
    if type(eth.data) == dpkt.ip.IP:
        ip = eth.data

        #only use TCP packets
        if type(ip.data) == dpkt.tcp.TCP:
            tcp = ip.data

            # Count SYN flags per IP
            if (tcp.flags & dpkt.tcp.TH_SYN) and not(tcp.flags & dpkt.tcp.TH_ACK):
                countSYN[ip.src] += 1

            # Count SYN+ACK flags per IP
            if (tcp.flags & dpkt.tcp.TH_SYN) and (tcp.flags & dpkt.tcp.TH_ACK):
                countACK[ip.dst] += 1

for IP in countSYN:
    if IP in countACK:
        if (countSYN[IP] > 3*(countACK[IP])):
            print(socket.inet_ntoa(IP))
        else:
            print(socket.inet_ntoa(IP))
