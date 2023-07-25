import pyautogui
import time as t
# n = tgl awal
n=11
pyautogui.hotkey('alt', 'tab')
libur = [16, 23]
while n <= 25:
    if n in libur:
        n+=1
        continue
    else:
        tgl = '2023-07-'
        if(len(str(n))<2):
            tgl = tgl+'0'+str(n)
        else:
            tgl = tgl+str(n)

        pyautogui.write(tgl) # type: ignore
        pyautogui.press('enter')
        pyautogui.write(tgl) # type: ignore
        pyautogui.press('enter')
        pyautogui.write(tgl) # type: ignore
        pyautogui.press('enter')
        pyautogui.write(tgl) # type: ignore
        pyautogui.press('enter')
        pyautogui.write(tgl) # type: ignore
        pyautogui.press('enter')
        pyautogui.write(tgl) # type: ignore
        pyautogui.press('enter')
        n+=1
