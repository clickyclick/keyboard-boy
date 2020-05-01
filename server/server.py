from socket import *
import sys


serverPort = 1024 #TCP port we will listen on

#setup TCP socket
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(1)

while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024).decode()
