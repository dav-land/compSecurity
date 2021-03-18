from scapy.all import *
from collections import Counter

countSYN = Counter()
countACK = Counter()

def main():
    infile = sys.argv[1]
    # Code for parsing and flag extraction used from following link:
    # https://stackoverflow.com/questions/38154662/how-can-i-extract-tcp-syn-flag-from-pcap-file-and-detect-syn-flood-attack-using
    for packet in PcapReader(infile):
        # check for SYN flag in packet
        if TCP in packet and packet[TCP].flags == 'S':
            src = packet.sprintf('{IP:%IP.src%}{IPv6:%IPv6.src%}')
            countSYN[src] += 1

        # check for SYN+ACK flag in packet
        if TCP in packet and packet[TCP].flags == 'SA':
            src = packet.sprintf('{IP:%IP.dst%}{IPv6:%IPv6.dst%}')
            countACK[src] += 1

    # return IP of packet with at least 3x as many SYN as SYN+ACK
    for IP in countSYN:
        if countACK[IP]:
            if countSYN[IP] > (3 * countACK[IP]):
                print(IP)
        else:
            print(IP)

if __name__ == '__main__':
    main()
