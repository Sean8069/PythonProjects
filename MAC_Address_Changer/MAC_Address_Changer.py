#!/usr/bin/env/python3

import subprocess

def MAC_Changer():

    '''
    This Function is to Change MAC Address of an Interface   
    '''

    subprocess.run(['ifconfig', 'eth0', 'down'])
    subprocess.run(['ifconfig', 'eth0', 'hw', 'ether', '00:11:22:33:44:55'])
    subprocess.run(['ifconfig', 'eth0', 'up'])

    print(f'[+] MAC Address has successfully changed to 00:11:22:33:44:55')


MAC_Changer()
