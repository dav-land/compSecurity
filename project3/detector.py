from scapy.all import *
from collections import Counter

synAckRatio = 3
infile = 'proj3.pcap'

pkt_count = 0
countSYN = Counter()
countACK = Counter()

for packet in PcapReader(infile):
    if TCP in packet and packet[TCP].flags & 2 and not packet[TCP].flags & 16:  # TCP SYN packet
    # if TCP in packet and packet[TCP].flags == 'S':  # TCP SYN packet
        src = packet.sprintf('{IP:%IP.src%}{IPv6:%IPv6.src%}')
        countSYN[src] += 1
    if TCP in packet and packet[TCP].flags & 2 and packet[TCP].flags & 16: # TCP SYN+ACK packet
    # if TCP in packet and packet[TCP].flags == 'SA': # TCP SYN+ACK packet
        src = packet.sprintf('{IP:%IP.src%}{IPv6:%IPv6.src%}')
        countACK[src] += 1

print(countSYN)
print(countACK)

# with open('SYN.txt', 'w') as file:
#      file.write(json.dumps(countSYN))
#
# with open('ACK.txt', 'w') as file1:
#      file1.write(json.dumps(countACK))


# for IP in list(countSyn):
#     if countACK[IP]:
#         countSyn[IP] /= countACK[IP]

for IP in countSYN:
    if IP in countACK:
        if (countSYN[IP] > 3 * (countACK[IP])):
            print(IP)
    elif countSYN[IP] >= 3:
        print(IP)
