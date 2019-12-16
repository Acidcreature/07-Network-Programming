#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request
	answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]

	print("IP\t\t\t\tMAC Addess\n..................................."
	for element in answered_list:
		print(element[1].psrc + "\t\t" + element[1].hwsrc)


#scan("10.240.234.31")
scan("10.240.234.0/24")
