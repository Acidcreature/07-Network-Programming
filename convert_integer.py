import socket

def convert_integer():
	data = 1234
	#32 bit
	print("Original: %s => Long host byte order: %s, Network byte order: %s" %(data, socket.ntohl(data), socket))
	#16 bit
	print("Original: %s => Long host byte order: %s, Network byte order: %s" %(data, socket.ntohs(data), socket))

if __name__ == '__main__':
	convert_integer()
