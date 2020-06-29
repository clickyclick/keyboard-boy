from socket import *
import sys


serverPort = 1024 #TCP port we will listen on

#setup TCP socket
udpSocket = socket(AF_INET,SOCK_DGRAM)
udpSocket.bind(('', serverPort))

while True:
    #connectionSocket, addr = serverSocket.accept()
    message = udpSocket.recv(2048).decode()
    print(message)
