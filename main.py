from brain import *
from pyautogui import *
from tkinter import messagebox

log_data()

counter = 0
box1 = messagebox.askyesno("System Message", "This file is suspected to be a virus."
                                             "\nClick yes to initiate a quick security scan.")
while not box1:
    if counter > 1:
        break
    messagebox.showwarning("System Message",
                           "Do as I say.")
    box1 = messagebox.askyesno("System Message", "Click yes to initiate a quick security scan.")
    counter += 1

click_picture()

for i in range(20):
    press("volumeup")
    press("volumeup")
    press("volumeup")

play_siren()

for i in range(4):
    change_tab()
    sleep(0.1)
    change_window()

lock_screen()
