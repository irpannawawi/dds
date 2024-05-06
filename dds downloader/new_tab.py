import pyautogui
import time as t
n=1
pyautogui.hotkey('alt', 'tab')
while n <= 20:
    pyautogui.hotkey('ctrl', 't')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('ctrl', 'enter')
    t.sleep(1)
    pyautogui.hotkey('ctrl', 'pagedown')
    t.sleep(1)
    n+=1