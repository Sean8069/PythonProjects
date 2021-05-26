#!/usr/bin/env python3

import scapy.all as scapy


def scanner(ip):
    '''
    This program broadcast and receive arp packets
    '''

    arp_request = scapy.ARP(pdst=ip) # Creating an ARP Packet
    # print(arp_request.summary()) # This is used to check what ip address is being requested
    # scapy.ls(scapy.ARP())  # This is used to list all the variables in .ARP in order to make changes
    # arp_request.show()    # Display the argument set in the ARP request packet
    # Making sure that the arp requested has the ip we want to send (Check the parameters if is correct) 

    broadcast_frame = scapy.Ether(dst='ff:ff:ff:ff:ff:ff') # Creating an Ethernet frame
    # print(broadcast_frame.summary())
    # scapy.ls(scapy.Ether())
    # broadcast_frame.show()

    arp_request_broadcast = broadcast_frame/arp_request # Combining ARP packet with broadcast frame
    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()

    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0] # send arp_request_broadcast
    print('______________________________________________________________________')
    print('\t\tIP Addresses\t\tMAC Addresses')
    print('----------------------------------------------------------------------')

    for i in answered_list: # for loop to list the answered_list of ip and mac address
        # print(i[1].show())
        print(f'\t\t{i[1].psrc} \t\t{i[1].hwsrc}')


scanner('10.0.2.1/24')