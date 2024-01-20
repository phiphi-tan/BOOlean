import random
import tkinter as tk
from pathlib import Path
import platform

# Using pathlib.Path to have general paths regardless of OS
RAW_IDLE_PATH = Path("assets/idle.gif")
IDLE_PATH = RAW_IDLE_PATH.resolve()
ANIMATION_DELAY = 150

window = tk.Tk()

# Position of virtual pet
screen_width = window.winfo_screenwidth()
pet_width = 48
pos = (screen_width - pet_width) // 2

cycle = 0
current_state = 0
default_num = [1, 2, 3, 4]
event_num = random.randrange(1, 3, 1)

# Default gif (8 frames)
default = [
    tk.PhotoImage(file=IDLE_PATH, format="gif -index %i" % (i)).zoom(2, 2)
    for i in range(8)
]

# Assigning Number to event


def event(cycle, current_state, event_num, pos):
    if event_num in default_num:
        current_state = 0
        window.after(0, update, cycle, current_state, event_num, pos)


# Moving the GIF


def gif_work(cycle, frame, event_num, first, last):
    if cycle < len(frame) - 1:
        cycle += 1
    else:
        cycle = 0
        # event_num = random.randrange(first, last + 1, 1)
    return cycle, event_num


def update(cycle, current_state, event_num, pos):
    if current_state == 0:  # default
        frame = default[cycle]
        cycle, event_num = gif_work(cycle, default, event_num, 1, 9)

    window.geometry("100x100+" + str(pos) + "+300")
    label.configure(image=frame)
    window.after(ANIMATION_DELAY, event, cycle, current_state, event_num, pos)


label = tk.Label(window, bd=0)
label.pack()

# For different OS systems
if platform.system() == "Darwin":
    window.config(bg="systemTransparent")
    window.wm_attributes("-transparent", True)
elif platform.system() == "Windows":
    window.config(bg="white")
    window.attributes('-alpha', 1)

window.overrideredirect(True)
window.wm_attributes("-topmost", True)

window.after(0, update, cycle, current_state, event_num, pos)
window.mainloop()
