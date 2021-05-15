from tkinter import *
from tkinter.ttk import *
from time import strftime

Clock = Tk()
Clock.title("Clock")

def time():
    string = strftime('%H:%M:%S %P')
    label.config(text=string)
    label.after(1000, time)
label = Label(Clock, font=("ds-digital", 80), background="black",foreground="cyan")
label.pack(anchor="center")
time()
mainloop()