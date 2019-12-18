from random import randint
from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM

HOSTNAME = ''       # blank so any address can be used
PORTNUMBER = 11267  # number for the port
BUFFER = 80         # size of the buffer

DEALER_ADDRESS = (HOSTNAME, PORTNUMBER)
DEALER = Socket(AF_INET, SOCK_STREAM)
DEALER.bind(DEALER_ADDRESS)
DEALER.listen(1)

print('Server waiting for client to connect')
PLAYER, PLAYER_ADDRESS = DEALER.accept()
print('Server accepted connection request from ',\
	PLAYER_ADDRESS)

rock = 1
paper = 2
scissors = 3



while True:
	SECRET = randint(1, 3)
	print('Server waiting for guess')
	GUESS = PLAYER.recv(BUFFER).decode()
	GUESS = int(GUESS)
	print('Server received ', GUESS)

	if GUESS < SECRET:
		REPLY = "You lost"
		

	elif GUESS == SECRET:
		REPLY = "Tied, Try again"
		
	
	else:
		REPLY = 'You won!'
	PLAYER.send(REPLY.encode())
	if REPLY == 'found the secret':
        	break
		

DEALER.close()


