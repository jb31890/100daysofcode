#!/usr/bin/env python

# please dont use this for managing passwords

from tkinter import Tk, Label, Entry, Canvas, PhotoImage, Button
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    pass

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.gif")
canvas.create_image(100,100, image=logo)

# website label 0,1 and entry 1,1 columnspan 2 width 35
website_label = Label(text="Website:")
website_entry = Entry(width=35)

# email/user label 0,2 and entry 1,2 columnspan 2 width 35
user_label = Label(text="Email/User:")
user_entry = Entry(width=35)

# password label 0,3 and entry 1,3 width 21 and generate password button 2,3
password_label = Label(text="Password:")
password_entry = Entry(width=21)
password_button = Button(text="Generate Password", command=generate_password, highlightbackground="black")

# add button 1,4 columnspan 2 width 36
add_button = Button(text="Add:", command=save_password, highlightbackground="#AA5588", width=36)

#grid layout
canvas.grid(column=1,row=0)
website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1, columnspan=2)
user_label.grid(column=0, row=2)
user_entry.grid(column=1, row=2, columnspan=2)
password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3)
password_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

#help(Button())

window.mainloop()


