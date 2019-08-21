#This is small automation python script to scan network interface(show Interface, Mac address, IP address)
#Under Microsoft Windows 10
#Created by Tommas Huang
#Created date: 2019/08/21

import netifaces
#It’s been annoying me for some time that there’s no easy way to get the address(es) of the machine’s network interfaces from Python.

x = netifaces.interfaces()
#netifaces reads: full Ethernet/IP/IPv6-Information. But no meaningful interface-names

for i in x:
    if i != 'lo':
     print('\nInterface: ' + i)
	 #print netifaces.ifaddresses(interface)
    mac = netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']
	#the keys in the dictionary returned by netiface.ifaddresses are protocol numbers, and there are named constants in the netifaces module for each of these. 
	#So instead of asking for result[17], ask for result[netifaces.AF_LINK].
    print('Mac addr: ' + mac)

    try:
        ip = netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']
		#A pair (host, port) is used for the AF_INET address family, where host is a string representing either a hostname in Internet domain notation

        print('IP addr: {0} '.format(ip))
    except KeyError:
        print('NO IP')
        continue