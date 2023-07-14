from pynput.keyboard import Key, Controller, Listener
import time

keyboard = Controller()

# Flag to control the spamming action
spamming = False

def on_press(key):
    global spamming

    # Start or stop spamming when 'p' key is pressed
    if key.char == 'p':
        spamming = not spamming

# This thread listens to key presses
listener = Listener(on_press=on_press)
listener.start()

while True:
    # If spamming is enabled, spam the down arrow and enter
    if spamming:
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        time.sleep(0.1)  # You can adjust the delay as needed

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.1)  # You can adjust the delay as needed

listener.join()
