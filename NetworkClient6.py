#!/usr/bin/python3

import socket

host = '::1'

mysock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
addr = (host,9898)  
mysock.connect(addr)

try:
	msg = b"hi, this is a test\n"
	mysock.sendall(msg)

except socket.errno as e:
	print("Socket error ", e)

finally:
	mysock.close()
