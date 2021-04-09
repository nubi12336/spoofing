from scapy.all import *
import time

A= "192.168.30.1"
B= "192.168.20.1"
C= RandShort()
D= 53

data= ('32 ff 00 58 00 00 00 01 28 db 00 00 45 00 00 54 00 00 40 00 40 00')
data_list= data.split(" ")
data_s= ''.join(data_list).decode('hex')

start = time.time()
while (time.time() - start < 10):
    spoofed_packet = IP(src=A, dst=B) / UDP(sport=C, dport=D) / data_s
    send(spoofed_packet)
