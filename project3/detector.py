from scapy.all import *
from collections import Counter
import json

synAckRatio = 3
infile = 'proj3.pcap'

pkt_count = 0
countSyn = Counter()
countACK = Counter()

for packet in PcapReader(infile):
    if TCP in packet and packet[TCP].flags & 2:  # TCP SYN packet
        src = packet.sprintf('{IP:%IP.src%}{IPv6:%IPv6.src%}')
        countSyn[src] += 1
#        print(type(src))
    if TCP in packet and packet[TCP].flags & 16: # TCP ACK packet
        src = packet.sprintf('{IP:%IP.src%}{IPv6:%IPv6.src%}')
        countACK[src] += 1

print(countSyn)
print(countACK)

# with open('SYN.txt', 'w') as file:
#      file.write(json.dumps(countSYN))
#
# with open('ACK.txt', 'w') as file1:
#      file1.write(json.dumps(countACK))


for IP in list(countSyn):
    if countACK[IP]:
        countSyn[IP] /= countACK[IP]


print(countSyn)
