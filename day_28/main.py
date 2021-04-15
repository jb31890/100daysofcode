#!/usr/bin/env python

import tkinter
from math import floor

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

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_pomodoro():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(10)
        #count_down(long_break_sec)
        timer_title.config(text="Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 50, "bold"))
    elif reps % 2 == 0:
        count_down(5)
        #count_down(short_break_sec)
        timer_title.config(text="Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 50, "bold"))
    else:
        count_down(7)
        #count_down(work_sec)
        timer_title.config(text="Twerk", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))


def reset_pomodoro():
    global reps
    reps = 0
    marks = ""
    checks.config(text=marks, bg=YELLOW, fg=GREEN)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_title.config(text="Timer")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(time):
    global timer
    minutes = int(time / 60)
    seconds = int(time % 60)
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    if time > 0:
        timer = window.after(1000, count_down, time - 1)
    else:
        start_pomodoro()
        marks = ""
        for _ in range(floor(reps/2)):
            marks += "✓"
        checks.config(text=marks, bg=YELLOW, fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tkinter.PhotoImage(file="tomato.gif")
canvas.create_image(100,112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)

timer_title = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
timer_title.grid(column=1, row=0)

start = tkinter.Button(text="Start", highlightbackground=RED, command=start_pomodoro)
start.grid(column=0,row=2)

reset = tkinter.Button(text="Reset", highlightbackground=RED, fg=RED, command=reset_pomodoro)
reset.grid(column=2,row=2)

checks = tkinter.Label(bg=YELLOW, fg=GREEN)
checks.grid(column=1,row=3)


window.mainloop()
