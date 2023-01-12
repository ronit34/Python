import time

import pyautogui
import random

time.sleep(5)
for i in range(10):

    A = 95
    B = random.randint(11111111,99999999)
    pyautogui.typewrite(str(A)+str(B))
    pyautogui.press("Enter")