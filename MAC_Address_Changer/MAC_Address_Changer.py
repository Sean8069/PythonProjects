#!/usr/bin/env/python3

import subprocess
import argparse


def User_Input():
    '''
    This Function provides option for user input
    '''

    parser = argparse.ArgumentParser(description='This is a MAC Address changer program.')
    parser.add_argument('-i', '--interface', dest='interface', help='interface to change MAC address', metavar='')
    parser.add_argument('-m', '--mac_addr', dest='new_mac', help='new MAC address', metavar='')
    args = parser.parse_args()

    if not args.interface:
        parser.error('[-] Error Interface: Please input a valid interface, refer --help for more information.')
    elif not args.new_mac:
        parser.error('[-] Error MAC: Please input a valid MAC address, refer --help for more information.')
    else:
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
