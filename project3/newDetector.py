import dpkt, socket
from collections import Counter
import sys

countSYN = Counter()
countACK = Counter()

def main():
    filename = 	sys.argv[1]
    file = open(filename, 'rb')
    pcap = dpkt.pcap.Reader(file)

    # used code from "https://jon.oberheide.org/blog/2008/10/15/dpkt-tutorial-2-parsing-a-pcap-file/" for iteration
    # used "https://dpkt.readthedocs.io/en/latest/_modules/examples/print_http_requests.html" for flag extraction
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
                # use source
                if (tcp.flags & dpkt.tcp.TH_SYN) and not(tcp.flags & dpkt.tcp.TH_ACK):
                    countSYN[ip.src] += 1
                # Count SYN+ACK flags per IP
                # use destination
                if (tcp.flags & dpkt.tcp.TH_SYN) and (tcp.flags & dpkt.tcp.TH_ACK):
                    countACK[ip.dst] += 1

    # used example code from "https://dpkt.readthedocs.io/en/latest/_modules/examples/print_packets.html#mac_addr"
    for IP in countSYN:
        if IP in countACK:
            if (countSYN[IP] > 3 * (countACK[IP])):
                try:
                    print(socket.inet_ntop(socket.AF_INET, IP))
                except ValueError:
                    print(socket.inet_ntop(socket.AF_INET6, IP))
        else:
            try:
                print(socket.inet_ntop(socket.AF_INET, IP))
            except ValueError:
                print(socket.inet_ntop(socket.AF_INET6, IP))

if __name__ == '__main__':
    main()
