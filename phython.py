import keyboard
import pyautogui
import sys


def on_key_press(event):
    if event.name == 'h':
        #TODO make a line changing between True and false
        
        pyautogui.press('backspace')
        pyautogui.write('Hello')
        pyautogui.press('enter')
        
    elif event.name == '+':
        pyautogui.press('backspace')
        print("Exiting program...")
        sys.exit()
    elif event.name == 'k':
        pyautogui.press('backspace')
        pyautogui.write('Bye')
        pyautogui.press('enter')
keyboard.on_press(on_key_press)

    

while True:
    pass  
