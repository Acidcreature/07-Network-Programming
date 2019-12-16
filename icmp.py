#!/usr/bin/python

from scapy.all import *

dst_ip = "10.240.234.31"

pkt = IP(dst=dst_ip)/ICMP()/"hello world"
send(pkt)
