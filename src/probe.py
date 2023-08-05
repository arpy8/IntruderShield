from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import os
import pygame
from PIL import Image
from tkinter import messagebox

dir_path = r'../data/intruder'
file_name = os.listdir(r'../data/intruder/')[-1]
count_txt = open("../data/count.txt", "r").readline()


def play_siren():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/aud.ogg")
    pygame.mixer.music.play()


def dir_count():
    return str(len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))]))


def open_image():
    im = Image.open(f"{dir_path}/{file_name}")
    im.show()


try:
    if count_txt != 0:
        if dir_count() != count_txt:
            play_siren()
            open("../data/count.txt", "w").write(dir_count())
            messagebox.showinfo("Critical Message", f"Trojan file triggered")
            open_image()
    else:
        print("No files found")
except TypeError or FileNotFoundError:
    pass
