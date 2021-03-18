#!/usr/bin/python3
import socket
import scapy
from scapy.all import *

def inject_pkt(pkt):
    #import dnet
    #dnet.ip().send(pkt)
    conf.L3socket=L3RawSocket
    send(pkt)

######
# edit this function to do your attack
######
def handle_pkt(pkt):
    if("GET / HTTP/1.1" in str(pkt)):
        badPack = IP(src=pkt[IP].src, dst=pkt[IP].dst)
        print(badPack)


def main():
    sniff(prn=handle_pkt, filter="ip")
        

if __name__ == '__main__':
    main()
