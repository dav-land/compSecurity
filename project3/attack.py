#!/usr/bin/python3

import scapy
from scapy.all import send, conf, L3RawSocket



def inject_pkt(pkt):
    #import dnet
    #dnet.ip().send(pkt)
    conf.L3socket=L3RawSocket
    send(pkt)

######
# edit this function to do your attack
######
def handle_pkt(pkt):
    string = str(pkt)
    if("freeaeskey" in string):
        print(string)
    pass

def main():
    import socket
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0x0300)
    while True:
        pkt = s.recv(0xffff)
        handle_pkt(pkt)

        

if __name__ == '__main__':
    main()
