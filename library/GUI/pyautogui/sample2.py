import pyautogui as pag
import time
pag.click(1400,100)
pag.hotkey("ctrl","a")
pag.press("backspace")

naiyou = ["import random\n",'print("random!")\n',"print(random.randint(1,6))"]


for i in naiyou:
    pag.typewrite(i)
    pag.keyDown("shiftright")
    pag.keyUp("shiftright")
    time.sleep(1)
    pag.press("enter")


pag.press("esc")
pag.hotkey("ctrl","shift","b")
