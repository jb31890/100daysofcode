#!/usr/bin/env python

from tkinter import *

window = Tk()
window.title("miles to km")
#window.minsize(500,300)
window.config(padx=20,pady=20)

def miles_to_km():
    miles = int(miles_entry.get())
    km = miles * 1.609
    km_result.config(text=f"{km:.2f}")

miles = Label(text="Miles")
miles.grid(column=2, row=0)
miles_entry = Entry(width=5)
miles_entry.grid(column=1, row=0)

equals_to = Label(text="is equal to")
equals_to.grid(column=0, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate = Button(text="Calculate", highlightbackground="black", fg="white", command=miles_to_km)
calculate.grid(column=1, row=2)


window.mainloop()
