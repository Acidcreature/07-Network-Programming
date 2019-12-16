#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
	arp_request = scapy.ARP(pdst=ip)
	#arp_request.pdst = ip
	print(arp_request.summary())

scan("10.240.234.31")
#scan("10.240.234.0/24")
