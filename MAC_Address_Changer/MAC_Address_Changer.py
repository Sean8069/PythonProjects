#!/usr/bin/env/python3

import subprocess
import argparse


def User_Input():
    '''
    This Function provides option for user input
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', dest='interface', help='interface to change MAC address')
    parser.add_argument('-m', '--mac_addr', dest='new_mac', help='new MAC address')
    args = parser.parse_args()
    return args


def MAC_Changer(interface, new_mac):

    '''
    This Function is to Change MAC Address of an Interface   
    '''

    subprocess.run(['ifconfig', interface, 'down'])
    subprocess.run(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.run(['ifconfig', interface, 'up'])

    print(f'[+] MAC Address has successfully changed to {new_mac}')


value = User_Input()
MAC_Changer(value.interface, value.new_mac)
