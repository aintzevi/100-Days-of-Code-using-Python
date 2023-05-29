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

reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps, timer
    # Stop previous countdown
    reps = 0
    timer_label.config(text="TIMER", fg=GREEN)
    # Reset to the working time text
    canvas.itemconfig(timer_text, text=f'{WORK_MIN}:00')
    check_marks.config(text="")
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0:
        timer_label.config(text="Short break", fg=PINK, bg=YELLOW)
        count_down(short_break_sec)
    elif reps % 8 == 0:
        timer_label.config(text="Long break", fg=RED)
        count_down(long_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps, timer
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    canvas.itemconfig(timer_text, text=f'{str(count_minutes).zfill(2)}:{str(count_seconds).zfill(2)}')
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

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

timer_text = canvas.create_text(180, 180, text=f'{WORK_MIN}:00', fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, highlightbackground=  YELLOW, command=partial(start_timer))
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
