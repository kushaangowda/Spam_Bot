import pyautogui
import time
import keyboard
time.sleep(10)

f = open('godzilla.txt','r')

for word in f:
	pyautogui.typewrite(word)
	pyautogui.press('enter')
	