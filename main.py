from pyautogui import *
from tkinter import messagebox
from brain import play_siren, lock_screen, change_tab, change_window, log_data

box1 = messagebox.askyesno("Yandre.exe", "Hello cutie, I'm your personal assistant shall we continue?")
while not box1:
    messagebox.showwarning("Yandre.exe",
                           "Oopsie Woopsie!\nSeems like you pressed the wrong button. Let's try it once again, "
                           "shall we?")
    box1 = messagebox.askyesno("Yandre.exe", "Hello cutie, I'm your personal assistant shall we continue?")

messagebox.showinfo("Yandre.exe", "Let's begin then, I'm very excited for this.")

log_data()
for i in range(80):
    press("volumeup")
play_siren()

for i in range(4):
    change_tab()
    sleep(0.1)
    change_window()

lock_screen()
