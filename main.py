import random
import tkinter as tk

window = tk.Tk()

# Position of virtual pet
screen_width = window.winfo_screenwidth()
pet_width = 48
pos = (screen_width - pet_width) // 2

cycle = 0
current_state = 1
default_num = [1, 2, 3, 4]
event_num = random.randrange(1, 3, 1)
impath = 'C:\\Users\\kkaiyu\\Downloads\\'

# Default gif (8 frames)
default = [tk.PhotoImage(file=impath+'default.gif', format = 'gif -index %i' %(i)) for i in range(8)]

# Assigning Number to event
def event(cycle, current_state, event_num, pos):
    if event_num in default_num:
        check = 0
        print("default")
        window.after(400, update, cycle, current_state, event_num, pos)

# Moving the GIF
def gif_work(cycle, frame, event_num, first, last):
    if cycle < len(frame) - 1:
        cycle += 1
    else:
        cycle = 0
        event_num = random.randrange(first, last + 1, 1)
    return cycle, event

def update(cycle, current_state, event, pos):
    if current_state == 0: # default
        frame = default[cycle]
        cycle, event_num = gif_work(cycle, default, event_num, 1, 9)


window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor', 'white')

label = tk.Label(window, bd=0, bg='white')
label.pack()
window.after(1, update, cycle, current_state, event_num, pos)
window.mainloop()


