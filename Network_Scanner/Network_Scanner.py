#!/usr/bin/env python3

import scapy.all as scapy


def scanner(ip):
    '''
    This function broadcast and receive arp packets
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

    return scapy.srp(arp_request_broadcast, timeout=1)[0] # send arp_request_broadcast
    
def output(answered_list):
    '''
    This function prints the output of recevied arp packets
    '''
    print('______________________________________________________________________')
    print('\t\tIP Addresses\t\tMAC Addresses')
    print('----------------------------------------------------------------------')

    client_list = []
    for element in answered_list:   # for loop to store all the ip and mac address in list dictionary to make it more organize
        # print(element[1].show())  # information about the arp packets received
        client_dict ={'ip' : element[1].psrc, 'mac' : element[1].hwsrc} 
        client_list.append(client_dict)
    
    for dict_set in client_list:    # for loop to iterate and print out the dict value in the list
        print(f'\t\t{dict_set["ip"]}\t\t{dict_set["mac"]}')
        
    print('----------------------------------------------------------------------\n')


answered_list = scanner('10.0.2.1/24')
output(answered_list)
