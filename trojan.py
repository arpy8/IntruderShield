from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pyautogui import *
from tkinter import messagebox

FAILSAFE = False

def play_siren():
    pygame.mixer.init()
    pygame.mixer.music.load("siren.mp3")
    pygame.mixer.music.play()


def change_tab():
    keyDown("win")
    for _ in range(5):
        press("d")
        sleep(0.1)
    keyUp("win")


def change_window():
    keyDown("alt")
    for _ in range(5): press("tab")
    keyUp("alt")


def lock_screen():
    keyDown("win")
    press("d")
    keyUp("win")
    keyDown("alt")
    press("f4")
    keyUp("alt")
    for _ in range(2): press("up")
    press("enter")


box1 = messagebox.askyesno("Yandre.exe", "Hello cutie, I'm your personal assistant shall we continue?")
while not box1:
    messagebox.showwarning("Yandre.exe",
                           "Oopsie Woopsie!\nSeems like you pressed the wrong button. Let's try it once again, "
                           "shall we?")
    box1 = messagebox.askyesno("Yandre.exe", "Hello cutie, I'm your personal assistant shall we continue?")

messagebox.showinfo("Yandre.exe", "Let's begin then, I'm very excited for this.")

play_siren()

for i in range(4):
    change_tab()
    sleep(0.1)
    change_window()
lock_screen()

