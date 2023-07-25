import pyautogui
import time as t
n=1
pyautogui.hotkey('alt', 'tab')
while n <= 21:
    pyautogui.hotkey('ctrl', 's')
    t.sleep(1)
    pyautogui.press('enter')
    t.sleep(1)
    
    pyautogui.hotkey('ctrl', 'pgdn')
    n+=1
