import pyautogui
import time

time.sleep(5)

f = open("@everyone", "r")

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")