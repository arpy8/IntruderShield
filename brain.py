from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from datetime import datetime
import pyautogui
pyautogui.FAILSAFE = False



def play_siren():
    pygame.mixer.init()
    pygame.mixer.music.load("siren.mp3")
    pygame.mixer.music.play()


def change_tab():
    pyautogui.keyDown("win")
    for _ in range(5):
        pyautogui.press("d")
        pyautogui.sleep(0.1)
    pyautogui.keyUp("win")


def change_window():
    pyautogui.keyDown("alt")
    for _ in range(5): pyautogui.press("tab")
    pyautogui.keyUp("alt")


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


def log_data():
    with open('data/log_file.txt', 'a') as f:
        f.writelines(f'{datetime.now().strftime("%d/%m/%Y - %H:%M:%S")}\n')
        f.close()
