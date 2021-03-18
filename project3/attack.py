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
    print(pkt.encode('hex'))
    pass

def main():

    # s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0x0300)
    # while True:
    #     pkt = s.recv(0xffff)
    #     handle_pkt(pkt)
    sniff(filter="ip", prn=handle_pkt)
        

if __name__ == '__main__':
    main()
