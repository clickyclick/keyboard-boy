from socket import *
import sys


serverPort = int(sys.argv[1]) #port we will listen on

#setup UDP socket
udpSocket = socket(AF_INET,SOCK_DGRAM)
udpSocket.bind(('', serverPort))

while True:
    #connectionSocket, addr = serverSocket.accept()
    message, serverAddress = udpSocket.recvfrom(2048)
    print(message.decode())
    print(serverAddress[0])
    with open("./logs/" + serverAddress[0] + ".log", "a") as f:
        f.write(message.decode())