import random
import tkinter as tk
from pathlib import Path
import platform

# Using pathlib.Path to have general paths regardless of OS
RAW_IDLE_PATH = Path("assets/idle.gif")
IDLE_PATH = RAW_IDLE_PATH.resolve()
IDLE_PATH = "assets/idle.gif"
RIGHT_PATH = "assets/ghost_right_move.gif"
LEFT_PATH = "assets/ghost_left_move.gif"
ANIMATION_DELAY = 150
WINDOW_SIZE = 100
OFFSET = 300

window = tk.Tk()

# position of virtual pet
screen_width = window.winfo_screenwidth()
pet_width = 48
pos = (screen_width - pet_width) // 2

cycle = 0
current_state = 0
default_num = [1, 2, 3, 4]
right_num = [5, 6, 7]
left_num = [8, 9, 10]
event_num = random.randrange(1, 3, 1)

# gif inputs
default = [
    tk.PhotoImage(file=IDLE_PATH, format="gif -index %i" % (i)).zoom(2, 2)
    for i in range(8)
]

walk_right = [
    tk.PhotoImage(file=RIGHT_PATH, format="gif -index %i" % (i)).zoom(2, 2)
    for i in range(8)
]

walk_left = [
    tk.PhotoImage(file=LEFT_PATH, format="gif -index %i" % (i)).zoom(2, 2)
    for i in range(8)  
]

# event number


def event(cycle, current_state, event_num, pos, pet_widget):
    if event_num in default_num:
        current_state = 0
        window.after(0, update, cycle, current_state, event_num, pos, pet_widget)

    elif event_num in right_num:
        current_state = 2
        window.after(0, update, cycle, current_state, event_num, pos, pet_widget)

    elif event_num in left_num:
        current_state = 3
        window.after(0, update, cycle, current_state, event_num, pos, pet_widget)


# gif movement


def move(cycle, frame, event_num, first, last, pet_widget):
    if cycle < len(frame) - 1:
        cycle += 1
    else:
        cycle = 0
        event_num = random.randrange(first, last + 1, 1)
    return cycle, event_num


def update(cycle, current_state, event_num, pos, pet_widget):
    frame = None
    if current_state == 0:  # default
        frame = default[cycle]
        cycle, event_num = move(cycle, default, event_num, 1, 9, pet_widget)

    elif current_state == 1: # move right
        frame = walk_right[cycle]
        cycle, event_num = move(cycle, walk_right, event_num, 1, 9, pet_widget)
        pos += 3

    elif current_state == 2: # move left
        frame = walk_left[cycle]
        cycle, event_num = move(cycle, walk_left, event_num, 1, 9, pet_widget)
        pos -= 3

    # window.geometry("100x100+" + str(pos) + "+300")
    # label.configure(image=frame)
    canvas.itemconfig(pet_widget, image=frame)
    window.after(ANIMATION_DELAY, event, cycle, current_state, event_num, pos, pet_widget)

def openChatGPTInput(event):
    print('open')
    textInput = tk.Toplevel(window)
    textInput.geometry('200x200')


canvas = tk.Canvas(window, width=100, height=100)
canvas.bind('<Button-1>', openChatGPTInput)
canvas.pack()
canvas.focus_set()

pet_widget = canvas.create_image(
    WINDOW_SIZE / 2, WINDOW_SIZE / 2, image=default[0]
)


# label = tk.Label(window, bd=0)
# label.pack()

# For different OS systems
if platform.system() == "Darwin":
    window.config(bg="systemTransparent")
    window.wm_attributes("-transparent", True)
elif platform.system() == "Windows":
    window.config(bg="white")
    window.attributes('-alpha', 1)

window.overrideredirect(True)
window.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}+" + str(pos) + f"+{OFFSET}")
window.wm_attributes("-topmost", True)
window.wm_attributes("-transparent", True)
window.after(0, update, cycle, current_state, event_num, pos, pet_widget)
window.mainloop()
