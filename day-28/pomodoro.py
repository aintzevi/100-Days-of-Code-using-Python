import math
from functools import partial
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

time = 3
def start(time):
    # times 60 for num of seconds
    global reps
    work_sec = WORK_MIN * 60
    
    count_down(time * 60)


def reset():

    # Reset to the working time text
    canvas.itemconfig(timer_text, text=f'{WORK_MIN}')



def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    canvas.itemconfig(timer_text, text=f'{str(count_minutes).zfill(2)}:{str(count_seconds).zfill(2)}')
    if count > 0:
        window.after(1000, count_down, count - 1)


window = Tk()
window.title("Pomodoro")
# padding the view so that the window is larger than the image itself
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

# Things can be layered on the canvas
canvas = Canvas(width=360, height=360, bg=YELLOW, highlightthickness=0)

main_image = PhotoImage(file="tomato.png")
# Centering the image by putting it in half of width and half of height
canvas.create_image(180, 180, image=main_image)

timer_text = canvas.create_text(180, 180, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, command=partial(start, time))
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command=reset)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
