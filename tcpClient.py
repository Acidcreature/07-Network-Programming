from socket import *
import argparse

HOST = 'localhost'
PORT = 666
BUFFSIZE = 1024
ADDR = (HOST, PORT)

tcpClientSock = socket(AF_INET, SOCK_STREAM)
tcpClientSock.connect(ADDR)

while True:
	data = raw_input('> ')
	if not data:
		break

	tcpClientSock.send(data)
	data = tcpClientSock.recv(BUFFSIZE)
	if not data:
		break
	print data

tcpClientSock.close()
