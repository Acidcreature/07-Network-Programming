#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
	scapy.arping(ip)

#scan("10.240.234.31")
scan("10.240.234.0/24")
