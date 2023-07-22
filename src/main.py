import cv2
import pyautogui
from datetime import datetime


def lock_screen():
    pyautogui.keyDown("win")
    pyautogui.press("d")
    pyautogui.keyUp("win")
    pyautogui.keyDown("alt")
    pyautogui.press("f4")
    pyautogui.keyUp("alt")
    for _ in range(2): pyautogui.press("up")
    pyautogui.press("enter")
    pyautogui.sleep(1)
    pyautogui.press("enter")
    for _ in range(2):
        pyautogui.press("enter")


def click_picture():
    name = datetime.now().strftime("%H.%M.%S  %d-%m-%Y")
    camera = cv2.VideoCapture(0)
    for i in range(1):
        return_value, image = camera.read()
        cv2.imwrite(f'./data/intruder/{name}.png', image)
    del (camera)


click_picture()
lock_screen()