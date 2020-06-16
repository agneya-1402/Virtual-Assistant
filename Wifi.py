import pyautogui
import time
#print(pyautogui.position())
#1143,759
#1278,268
#1178,179
#1276,278
def off():
    pyautogui.click(1143, 749)
    time.sleep(5)
    pyautogui.click(1278, 268)
def on():
    pyautogui.click(1143,749)
    time.sleep(5)
    pyautogui.click(1178,179)
    time.sleep(1)
    pyautogui.click(1276,278)
