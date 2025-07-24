import pyperclip
import keyboard
import time
import traceback

import os 
logPath = os.path.dirname(os.path.abspath(__file__)) + '\\log.txt'

DELAY = 0.025
HOTKEY = 'ctrl+`'
EXIT_KEY = 'ctrl+shift+`'

from datetime import datetime

text = ''

def on_win_z():
    global text
    text = pyperclip.paste()
    while True:
        if not keyboard._pressed_events:  # low-level API
            break
        time.sleep(DELAY)
    for char in text:
        if char=='\n':
            keyboard.press_and_release('shift+enter')
            time.sleep(DELAY)
        else:
            keyboard.write(char, delay=DELAY)
    

# Register global hotkey
keyboard.add_hotkey(HOTKEY, on_win_z)
print('<hotkeys active>: ')
print('paste: ', HOTKEY)
print('exit : ', EXIT_KEY)

try:
    keyboard.wait(EXIT_KEY)
except Exception:
    dt = datetime.now().isoformat()
    text = '\ntime={}\ntext={}\nError={}'.format(dt, text, traceback.format_exc())
    with open(logPath, 'a', encoding='utf-8') as f:
        f.write(text)

