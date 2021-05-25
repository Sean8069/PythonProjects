#!/usr/bin/env python3

import subprocess
import argparse
import re


def user_input():
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


def mac_changer(interface, new_mac):

    '''
    This Function is to Change MAC Address of an Interface   
    '''

    subprocess.run(['ifconfig', interface, 'down'])
    subprocess.run(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.run(['ifconfig', interface, 'up'])

    print(f'[+] Changing MAC Address to {new_mac}')

def get_current_mac(interface):
    '''
    This Function will return the current MAC address
    '''
    ifconfig_result = subprocess.check_output(['ifconfig', interface], text=True)
    current_mac = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)
    
    if current_mac:
        return current_mac.group(0)  # return the first occurance of ifconfig result
    else:
        print('[-] Failed to read MAC Address.')



value = user_input()
current_mac = get_current_mac(value.interface)
print(f'Current MAC is {current_mac} ')
mac_changer(value.interface, value.new_mac)




# Check if the MAC Address is changed

current_mac = get_current_mac(value.interface)
if current_mac == value.new_mac:
    print(f'[+] MAC Address has successfully changed to {value.new_mac}')
else:
    print('[-] MAC Address Failed to change')


