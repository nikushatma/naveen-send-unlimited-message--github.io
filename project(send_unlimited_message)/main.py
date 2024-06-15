# install these packages
# ->pip install pyautogui
# ->pip install time


import pyautogui as gui
import time

message = input("enter thr messege->")
number = input("enter the numbe->")

time.sleep(10)

for i in range(int(number)):
    gui.typewrite(message)
    gui.press('Enter')


