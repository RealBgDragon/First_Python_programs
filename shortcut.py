from pynput.keyboard import Key, Controller, Listener
import time
import threading

keyboard = Controller()

# Flag to control the spamming action
spamming = False

def on_press(key):
    global spamming

    try:
        # Toggle spamming when 'p' key is pressed
        if key.char == 'p':
            if spamming:
                spamming = False
            else:
                spamming = True
                # Start a new thread for the spamming action
                threading.Thread(target=spam_keys).start()
    except AttributeError:
        # Ignore the exception if it's not a character key
        pass

def spam_keys():
    while spamming:
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        time.sleep(0.1)  # You can adjust the delay as needed

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.1)  # You can adjust the delay as needed

# This thread listens to key presses
with Listener(on_press=on_press) as listener:
    listener.join()
