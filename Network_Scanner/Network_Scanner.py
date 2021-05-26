#!/usr/bin/env python3

import scapy.all as scapy


def scanner(ip):
    '''
    This program broadcast and receive arp packets
    '''

    arp_request = scapy.ARP(pdst=ip) # Creating an ARP Packet
    # print(arp_request.summary()) # This is used to check what ip address is being requested
    # scapy.ls(scapy.ARP())  # This is used to list all the variables in .ARP in order to make changes
    # arp_request.show()
    # Making sure that the arp requested has the ip we want to send (Check the parameters if is correct) 

    broadcast_frame = scapy.Ether(dst='ff:ff:ff:ff:ff:ff') # Creating an Ethernet frame
    # print(broadcast_frame.summary())
    # scapy.ls(scapy.Ether())

    arp_request_broadcast = broadcast_frame/arp_request # Combining ARP packet with broadcast frame
    # print(arp_request_broadcast.summary())
    arp_request_broadcast.show()


scanner('10.0.2.1/24')