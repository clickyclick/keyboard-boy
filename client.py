from socket import *
import sys

hostName = sys.argv[1]
serverPort = int(sys.argv[2])

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((hostName, serverPort))

for i in range(10):
    message = "hello"
    clientSocket.send(message.encode())
